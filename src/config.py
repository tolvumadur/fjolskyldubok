import os
import json
from pathlib import Path

def get_home_dir():
    return Path.home()

def _get_config_file_path():
    return get_home_dir() / ".familysearch" / "config.json"

def _check_config_file_exists():
    return os.path.exists(_get_config_file_path())

def get_client_id():
    assert _check_config_file_exists(), "No config file found at ~/.familysearch/config.json. See README for details."
    with open(_get_config_file_path()) as f:
        config = json.load(f)
        return config["ClientID"]
    
def get_username():
    assert _check_config_file_exists(), "No config file found at ~/.familysearch/config.json. See README for details."
    with open(_get_config_file_path()) as f:
        config = json.load(f)
        return config["Username"]

def get_appkey():
    assert _check_config_file_exists(), "No config file found at ~/.familysearch/config.json. See README for details."
    with open(_get_config_file_path()) as f:
        config = json.load(f)
        return config["AppKey"]
    
def get_password():
    assert _check_config_file_exists(), "No config file found at ~/.familysearch/config.json. See README for details."
    with open(_get_config_file_path()) as f:
        config = json.load(f)
        if "Password" in config:
            return config["AppKey"]
        else: 
            return input("Please type your password")