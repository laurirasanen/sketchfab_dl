import requests

API_SEARCH_URL = "https://api.sketchfab.com/v3/search"


def search_results(params):
    """Search for results.

    Keyword arguments:
    params -- Paremeters to use for search,
        see: https://docs.sketchfab.com/data-api/v3/index.html#/search
    """
    r = requests.get(API_SEARCH_URL, params)

    data = None
    try:
        data = r.json()
    except ValueError:
        pass

    assert r.ok, f"Search failed: {r.status_code} - {data}"

    return r.json()["results"]
