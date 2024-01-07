# Fjölskyldbók
Integration with familysearch API for AI-assisted digitization of record images.

[API reference](https://www.familysearch.org/developers/docs/api/resources)


## Get Started

Clone this repo and set up the following config file at `~/.familysearch/config.json`:

```
{
    "ClientID" : "FILL_IN_YOUR_CLIENT_ID",
    "Username" : "PUT_USERNAME_HERE",
    "AppKey" : "APP_KEY_HERE"
}
```

Then install dependencies:

```
pip3 install requests requests_oauthlib
TODO Dependency List
```

Then run `python3 main.py`