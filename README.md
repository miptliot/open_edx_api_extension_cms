# open_edx_api_extension_cms

API extension for Open edX CMS 

Installation:
```bash
sudo -Hu edxapp /edx/bin/pip.edxapp install -e git+https://github.com/miptliot/open_edx_api_extension_cms@release-2017-07-04#egg=open_edx_api_extension_cms
```

Set `EDX_API_KEY` in `cms.auth.json`

Add into file `cms/envs/npoed.py`
```python
EDX_API_KEY = AUTH_TOKENS.get("EDX_API_KEY")
INSTALLED_APPS += (
    'open_edx_api_extension_cms',
)
```

Add into file `cms/urls.py`
```python
urlpatterns += (
    url(r'^api/extended/', include('open_edx_api_extension_cms.urls', namespace='api_extension')),
)
```
