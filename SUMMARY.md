**A Semantically Annotated 15-Class Ground Truth Dataset for Substation Equipment** is a dataset for semantic segmentation, object detection, and object detection tasks. It is used in the energy industry. 

The dataset consists of 1660 images with 50604 labeled objects belonging to 15 different classes including *porcelain_pin_insulator*, *closed_blade_disconnect_switch*, *recloser*, and other: *glass_disc_insulator*, *current_transformer*, *lightning_arrester*, *power_transformer*, *breaker*, *potential_transformer*, *closed_tandem_disconnect_switch*, *open_tandem_disconnect_switch*, *tripolar_disconnect_switch*, *muffle*, *fuse_disconnect_switch*, and *open_blade_disconnect_switch*.

Images in the Substation Equipment dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 6 (0% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Note, that *background* class has been removed due to possible misinterpretation of data. The dataset was released in 2023 by the Universidade Tecnológica Federal do Paraná, Pontifícia Universidade Católica do Rio de Janeiro, and Paranaense de Energia SA (Copel).

Here are the visualized examples for some of the 15 classes:

[Dataset classes](https://github.com/dataset-ninja/substation-equipment/raw/main/visualizations/classes_preview.webm)
