import boto3
import logging
import boto3
from botocore.exceptions import ClientError
import json

#Update the IAM Access Keys
AWS_Access_Key_Id = '4a338104d79a418581c7c96af4d80f75'
AWS_Secret_Access_Key = 'gkx3uBYjCIx67b3a4632ef04443972e53ce761154ae'
AWS_Region = 'us-west-2'
s3_bucket_name = 'aws-python-boto3-s3bucket-24'

client = boto3.client('s3', aws_access_key_id=AWS_Access_Key_Id, aws_secret_access_key=AWS_Secret_Access_Key,
                      region_name=AWS_Region)


def create_s3_bucket(s3_bucket):
    aws_response = client.create_bucket(
        Bucket=s3_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': AWS_Region
        }
    )
    # print(aws_response)
    json_output = json.dumps(aws_response, indent=3)
    # Print the JSON-formatted string
    print(json_output)


if __name__ == "__main__":
    create_s3_bucket(s3_bucket_name)
