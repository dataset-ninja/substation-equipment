Dataset **Substation Equipment** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/g/D/LO/MsNDtM5llTX5H6SSybxBYDFjjX8tShb5UDgxAto8uX6orVf2wiUDGhexF1FTVkWmjBRb8HFvqNjn9ucbwAeZz6XQzE70rnzu5Bh39q0FqNoqgR8TbcR5SxVlWsjM.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Substation Equipment', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/7884270).