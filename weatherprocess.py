import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'weather-lamb-project1'