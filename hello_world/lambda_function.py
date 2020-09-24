import json
import yaml
import os

# import requests


def lambda_handler(event, context):
    file_path = (os.path.dirname(__file__))+"/sqldatabase.yml"
    with open(file_path, "r") as file:
        try:
            loaded = yaml.safe_load(file)
            print(loaded)
        except yaml.YAMLError as exc:
            print(exc)
    loaded["metadata"]["name"] = event["servicename"]
    loaded["metadata"]["namespace"] = event["namespace"]
    loaded["spec"]["instanceRef"]["name"] = loaded["metadata"]["name"] + "-sqlinstance-" + loaded["metadata"]["namespace"]

    file_path = (os.path.dirname(__file__))+"/sqlinstance.yml"
    with open(file_path, "r") as file:
        try:
            loaded2 = yaml.safe_load(file)
            print(loaded2)
        except yaml.YAMLError as exc:
            print(exc)
    loaded2["metadata"]["name"] = event["servicename"]
    loaded2["metadata"]["namespace"] = event["namespace"]
    all_manifests = yaml.dump(loaded,default_flow_style=False)
    all_manifests = all_manifests + "---\n"
    all_manifests = all_manifests + yaml.dump(loaded2,default_flow_style=False)
    #return {
    #    "statusCode": 200,
    #    "body": yaml.dump(loaded, default_flow_style=False),
    #}
    return all_manifests
