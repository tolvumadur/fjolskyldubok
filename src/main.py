#!/usr/bin/env python3

import auth
import sys
import projects

def main():

    print("Welcome to fjollskyldu indexing AI helper")

    print("Obtaining OAuth2 Token")

    try:
        session = auth.get_OAuth_Session()
        #session = auth._get_static_session()
        assert auth.test_session(session), "Failed to log in with current API token."
    except Exception as err:
        die(err)

    print("OAuth2 token loaded & successfully tested")

    print("Current Indexing Batches:")

    projects.list_available_projects(session)

    return 0


def die(err, errno=1):
    sys.stderr.write(str(err))
    exit(errno)

main()

