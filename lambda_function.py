import json
import yaml

print('Loading function')

def lambda_handler(event, context):

    with open("sqldatabase.yml", "r") as file:
        try:
            loaded = yaml.safe_load(file)
            print(loaded)
        except yaml.YAMLError as exc:
            print(exc)
    loaded["metadata"]["name"] = "test"
    loaded["metadata"]["namespace"] = "namespace_test"
    loaded["spec"]["instanceRef"]["name"] = loaded["metadata"]["name"] + "-sqlinstance-" + loaded["metadata"]["namespace"]
    
    return (yaml.dump(loaded, default_flow_style=False))
