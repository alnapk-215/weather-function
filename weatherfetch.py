import json
import urllib.request
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_table')

API_KEY = "a38d4c7b043154d30c9188d37d9cae32"

def lambda_handler(event, context):
    city = "Kochi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
 
response = urllib.request.urlopen(url)
data = json.loads(response.read())
table.put_item(
        Item={
            'city': city,
            'temperature': str(data['main']['temp']),
            'weather': data['weather'][0]['description'],
            'timestamp': datetime.now().isoformat()
        }
    )   
     return {
        'statusCode': 200,
        'body': json.dumps('Weather data inserted')
    }