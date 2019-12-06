# sketchfab_dl
### A small Python module for downloading models from Sketchfab.

## Usage
```python
from sketchfab_dl import set_api_token, download_model

# You can find your Sketchfab API Token at:
# https://sketchfab.com/settings/password
set_api_token("xxx")

# Download a model with UID to a folder
download_model("9b747732a7de4db6b1d21e18e0071802", "./cybertruck")
```