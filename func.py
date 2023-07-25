def handler(event, context):
    body = "Hello World Eduardo 51"
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {'Access-Control-Allow-Origin' : '*',"Content-Type": "application/json; charset=utf-8"},
        "body": body
        }

    return response
