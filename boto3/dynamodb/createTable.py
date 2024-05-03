import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.create_table(
  TableName="basicSongsTable",
  AttributeDefinitions=[
    {
      "AttributeName": "artist",
      "AttributeType": "S"
    },
    {
      "AttributeName": "song",
      "AttributeType": "S"
    }
  ],
  KeySchema=[
    {
      "AttributeName": "artist",
      "KeyType": "HASH" 
      #HASH KEYtype represents single primary key or partition key 
    },
    {
      "AttributeName": "song",
      "KeyType": "RANGE"
      #RANGE or sort key represents composed with HASH KEY Type ,combination of hash key and sort key must be unique.
    }
  ],
  ProvisionedThroughput={
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }
)

print(response)