import config
from requests_oauthlib import OAuth2Session

BASE_URL = "https://identint.familysearch.org" # Targeting Integration ENV for now
REDIRECT_URI = ""
CLIENT_ID = config.get_appkey() #config.get_client_id()
RESPONSE_TYPE = "code"
USERNAME = config.get_username()
PASSWORD = config.get_password()
SCOPE=["family_search"]

AUTHORIZATION_URL = BASE_URL + "/cis-web/oauth2/v3/authorization"
TOKEN_URL = BASE_URL + "/cis-web/oauth2/v3/token"
GETUSER_URL = "https://api-integ.familysearch.org/platform/users/current" # Targeting Integration ENV

def get_OAuth_Session():
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_URL)
    print('Please go to %s and authorize access.' % authorization_url)
    authorization_response = input('Enter the full callback URL')
    token = oauth.fetch_token(
        TOKEN_URL,
        authorization_response=authorization_response,
        include_client_id=True)
    
    # FamilySearch invents a nonexistent Token Type
    oauth.token["token_type"] = "Bearer"
    token["token_type"] = "Bearer"
    oauth._client.token_type = "Bearer"

    return oauth

def _get_static_session():
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    static_token = "FILL IN AND USE TO SAVE TIME IN TESTING"
    return set_token(static_token, oauth)
    
def set_token(token, oauth):
    oauth.token = dict()
    oauth.token["access_token"] = token
    oauth.token["token_type"] = "Bearer"
    oauth._client.access_token = token
    oauth._client.token_type = "Bearer"
    return oauth

def test_session(oauth):
    assert oauth.authorized, "OAuth Failed."

    r = oauth.get(GETUSER_URL)

    assert r.status_code == 200

    return True

