import boto3
import logging
import boto3
from botocore.exceptions import ClientError

aws_access_key_id = '8d1fd22d-93ce-4766-bf93-c5ea18618edb'
aws_secret_access_key = '8d1fd22d-93ce-4766-bf93-c5ea18618edb/l3Tl5e'
AWS_Region = 'us-west-2'

S3_Bucket = 'pythons3-bucket-20241'
client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                      region_name=AWS_Region)

AWS_Response = client.create_bucket(
    Bucket=S3_Bucket,
    CreateBucketConfiguration={
        'LocationConstraint': AWS_Region
    }
)

print(AWS_Response)
