import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'weath-erbucket'
def lambda_handler(event, context):

    print(event)