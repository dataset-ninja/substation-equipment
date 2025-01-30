Dataset **Substation Equipment** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzIxMzRfU3Vic3RhdGlvbiBFcXVpcG1lbnQvc3Vic3RhdGlvbi1lcXVpcG1lbnQtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAieUJRL0ZvNUViSmJpMUZ1Rk95UkNkMlNQcWlSdHFyVTI2ZW54YkFUMTV5TT0ifQ==)

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