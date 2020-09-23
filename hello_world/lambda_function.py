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
    
    #return {
    #    "statusCode": 200,
    #    "body": yaml.dump(loaded, default_flow_style=False),
    #}
    return yaml.dump(loaded, default_flow_style=False)
