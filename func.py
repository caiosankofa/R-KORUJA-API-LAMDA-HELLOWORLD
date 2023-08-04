import json

def handler(event, context):
    body = "Hello World Eduardo New"
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "Holla Caio Monteiro!"})
    }

    return response
