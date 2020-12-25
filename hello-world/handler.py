import json

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your Hello-World function executed successfully!",
        "input": event
    }

    print(body['message'])

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
