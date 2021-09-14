import json



def lambda_handler(event,context):
    return json.dumps({
        "hello":"123",
        "body":f"you hav ehit the path {event['path']}"
    })
