import supervisely as sly
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, file_exists
from supervisely.io.json import load_json_file
import shutil

from tqdm import tqdm

def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:        
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path
    
def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    dataset_path = "substation-semantic-dataset"
    imgs_path = os.path.join(dataset_path, "images")
    json_anns_path = os.path.join(dataset_path, "labels_json")
    batch_size = 50


    def swap_cords(cords):
        for cord in cords:
            cord[0], cord[1] = cord[1], cord[0]
        return cords


    def create_ann(image_path):
        labels = []
        file = os.path.basename(image_path)
        filename = get_file_name(file)
        json_ann = os.path.join(json_anns_path, f"{filename}.json")
        if file_exists(json_ann):
            ann = load_json_file(json_ann)
            img_height = ann["imageHeight"]
            img_wight = ann["imageWidth"]
            for label in ann["shapes"]:
                label_name = label["label"]
                if label_name == "Background":
                    continue
                fixed_label_name = label_name.lower()
                fixed_label_name = "_".join(fixed_label_name.split(" "))
                cords = label["points"]
                fixed_cords = swap_cords(cords)
                geometry = sly.Polygon(fixed_cords)
                obj_class = meta.get_obj_class(fixed_label_name)
                curr_label = sly.Label(geometry, obj_class)
                labels.append(curr_label)
            return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


    categories = {
        "open_blade_disconnect_switch": (162, 0, 255),
        "closed_blade_disconnect_switch": (97, 16, 162),
        "open_tandem_disconnect_switch": (81, 162, 0),
        "closed_tandem_disconnect_switch": (48, 97, 165),
        "breaker": (121, 121, 121),
        "fuse_disconnect_switch": (255, 97, 178),
        "glass_disc_insulator": (154, 32, 121),
        "porcelain_pin_insulator": (255, 255, 125),
        "muffle": (162, 243, 162),
        "lightning_arrester": (143, 211, 255),
        "recloser": (40, 0, 186),
        "power_transformer": (255, 182, 0),
        "current_transformer": (138, 138, 0),
        "potential_transformer": (162, 48, 0),
        "tripolar_disconnect_switch": (162, 0, 96)
    }
    obj_classes = [sly.ObjClass(cat, sly.Polygon, categories[cat]) for cat in categories]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, "ds", change_name_if_conflict=True)

    images = os.listdir(imgs_path)

    progress = sly.Progress("Create dataset {}".format("ds"), len(images))

    for index_batch in sly.batched(images, batch_size=batch_size):
        img_paths = [os.path.join(imgs_path, file) for file in index_batch]
        img_names_batch = [os.path.basename(img_path) for img_path in img_paths]
        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_paths)
        img_ids = [im_info.id for im_info in img_infos]
        anns_batch = [create_ann(image_path) for image_path in img_paths]
        api.annotation.upload_anns(img_ids, anns_batch)
        progress.iters_done_report(len(img_names_batch))

    return project
