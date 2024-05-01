import boto3
import json
from boto3.dynamodb.conditions import Key

TABLE_NAME = "basicSongsTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-1")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-1")
table = dynamodb.Table(TABLE_NAME)

response = dynamodb_client.query(
    TableName=TABLE_NAME,
    # AND ;BETWEEN OPERATORS
    KeyConditionExpression='artist = :artist AND song BETWEEN :songval1 AND :songval2',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':songval1': {'S': 'Bz'},
        ':songval2': {'S': 'D'}
    }
)  
print(response['Items'])
    #The less than operator (works BASED on ASCII CHARACTER)
response = dynamodb_client.query(
    TableName=TABLE_NAME,    
    KeyConditionExpression='artist = :artist AND song < :song',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':song': {'S': 'C'}}
)
print(response['Items'])
    # using HASH & SORT keytypes
response = table.query(
    TableName=TABLE_NAME,    
    KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').begins_with('C')    
)
print(response['Items'])