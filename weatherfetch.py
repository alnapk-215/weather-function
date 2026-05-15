import json
import urllib.request
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_table')

API_KEY = "a38d4c7b043154d30c9188d37d9cae32"

def lambda_handler(event, context):