import json

print('Loading function')

def lambda_handler(event, context):
    servicename = event['servicename']
    manifest = "apiVersion: sql.cnrm.cloud.google.com/v1beta1 __servicename__"

    manifest = manifest.replace("__servicename__",servicename)
    return (manifest)
    #raise Exception('Something went wrong')ß