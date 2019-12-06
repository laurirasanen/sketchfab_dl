# sketchfab_dl
### A small Python module for downloading models from Sketchfab.

## Usage
```python
from sketchfab_dl import set_api_token, download_model, search_results

# You can find your Sketchfab API Token at:
# https://sketchfab.com/settings/password
API_TOKEN = "xxx"

# Search parameters,
# see: https://docs.sketchfab.com/data-api/v3/index.html#/search
params = {
	"type": "models",
	"q": "cybertruck", 
	"downloadable": True,
	"count": 1
}

# Get a collection of models from the search API
models = search_results(params)
if len(models) == 0:
    print("No models found")
    exit()

# Downloading requires authentication
set_api_token(API_TOKEN)

# Download a model with UID to a folder
download_model(models[0]["uid"], "./cybertruck")
```