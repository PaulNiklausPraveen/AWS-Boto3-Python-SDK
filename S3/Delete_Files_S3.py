
import boto3

#Update the IAM Access Keys
AWS_Access_Key_Id = '4a338104d79a418581c7c96af4d80f75'
AWS_Secret_Access_Key = 'gkx3uBYjCIx67b3a4632ef04443972e53ce761154ae'
AWS_Region = 'us-west-2'
S3_Bucket = 'aws-python-boto3-s3bucket-24'


session = boto3.client('s3', aws_access_key_id=AWS_Access_Key_Id, aws_secret_access_key=AWS_Secret_Access_Key,
                       region_name=AWS_Region)

objects = session.list_objects_v2(Bucket=S3_Bucket)

# Extract the keys (file names) from the objects
keys = [obj['Key'] for obj in objects.get('Contents', [])]

# Delete each file in the list of keys
for key in keys:
    session.delete_object(Bucket=S3_Bucket, Key=key)

print(f"Deleted {len(keys)} files from the bucket.")
