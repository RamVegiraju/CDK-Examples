import json
import boto3

def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Lambda was invoked successfully.'
    }