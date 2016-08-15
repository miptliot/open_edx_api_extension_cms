# open_edx_api_extension_cms

API extension for Open edX CMS 

Installation:
```bash
pip install -e git+http://mpetrov@kallithea.local/ru/npoed/open_edx_api_extension_cms@develop#egg=open_edx_api_extension_cms
```

Add in file `cms/envs/common.py`
```python
INSTALLED_APPS = (
    ...
    'open_edx_api_extension_cms',
)
```

Add in file `cms/urls.py`
```python
urlpatterns = (
    ...
    url(r'^api/extended/', include('open_edx_api_extension_cms.urls', namespace='api_extension')),
)
```

Add in file `cms/envs/aws.py`
```python
EDX_API_KEY = AUTH_TOKENS.get("EDX_API_KEY")
```

Set `EDX_API_KEY` in `cms.auth.json`
