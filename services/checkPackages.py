import os
import requests
import json

def check_and_update_package(cdn_url, path):
    response = requests.get(cdn_url)

    if response.status_code == 200:
        cdn_content = response.text

        #if file exists
        if os.path.isfile(path):
            with open(path, 'r') as file:
                path_content = file.read()
        else:
            path_content = ""

        #compare cdn to local file
        if cdn_content != path_content:
            #update if not the same version
            with open(path, "w") as file:
                file.write(cdn_content)
            print(f"{path}: package updated\n")
        else:
            print(f"{path}: package up to date\n")

    else:
        print(f"Could not get the file from {cdn_url}. Status code: {response.status_code}\n")


def update_from_json_list(path):
    #load json file
    with open(path) as json_file:
        data = json.load(json_file)

    #foreach package check and update
    for package in data["packages"]:
        name = package["name"]
        print(f"Package {name}:\n")
        check_and_update_package(
            package["cdn_url"],
            os.path.join(os.getcwd(), "static", "js", package["path"])
        )