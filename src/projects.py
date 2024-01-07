import requests

INDEXING_BASE_URL = "https://sg30p0.familysearch.org"
INDEXING_PROJECTS_LIST_URL = INDEXING_BASE_URL + "/service/indexing/project/projects/search?asc=true&page=1&pagesize=2000&sort=creationTime"

def list_available_projects(oauth):
    params = {
        "category" : "indexingOrReview",
        "facet" : "batchAvailability",
        "keyword" : None,
        "language" : None,
        "region" : None,
        "state" : "ACTIVE",
        "type" : "INDEXING",
        "userAccessible" : True
    }
    r = oauth.post(INDEXING_PROJECTS_LIST_URL, json=params)

    print(r)
    print(r.text)
    exit()

    return