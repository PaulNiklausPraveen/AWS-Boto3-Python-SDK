import boto3
from botocore.exceptions import NoCredentialsError

#Update the Access Key
AWS_Access_Key_Id = '4a338104d79a418581c7c96af4d80f75'
AWS_Secret_Access_Key = 'gkx3uBYjCIx67b3a4632ef04443972e53ce761154ae'
AWS_Region = 'us-west-2'
bucket_name = 'aws-python-boto3-s3bucket-24'

client = boto3.client('s3', aws_access_key_id=AWS_Access_Key_Id, aws_secret_access_key=AWS_Secret_Access_Key,
                      region_name=AWS_Region)


def delete_all_objects_in_bucket(delete_files_in_bucket):
    try:
        # List all objects in the bucket
        response = client.list_objects_v2(Bucket=bucket_name)

        # Delete each object
        for obj in response.get('Contents', []):
            object_key = obj['Key']
            client.delete_object(Bucket=bucket_name, Key=object_key)
            print(f"Object deleted: {object_key}")

        print("All objects deleted")

    except NoCredentialsError:
        print("Credentials not available or incorrect.")


def delete_s3_bucket(delete_bucket):
    response = client.delete_bucket(Bucket=delete_bucket)
    print(response)


if __name__ == "__main__":
    # Delete all objects in the S3 bucket
    delete_all_objects_in_bucket(bucket_name)

    # Delete the S3 bucket
    delete_s3_bucket(bucket_name)
