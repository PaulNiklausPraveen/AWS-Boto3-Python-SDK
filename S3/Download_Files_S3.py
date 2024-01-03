import boto3
import os
from botocore.exceptions import NoCredentialsError

#Update the IAM Access Keys
AWS_Access_Key_Id = '4a338104d79a418581c7c96af4d80f75'
AWS_Secret_Access_Key = 'gkx3uBYjCIx67b3a4632ef04443972e53ce761154ae'
#Update the region and bucket name
AWS_Region = 'us-west-2'
S3_Bucket = 'aws-python-boto3-s3bucket-24'
Local_directory = 'C:/s3_download'

def download_all_files_from_s3(S3_Bucket_name, local_directory):


    try:
        #Creates an S3 client session
        session = boto3.client('s3', aws_access_key_id=AWS_Access_Key_Id, aws_secret_access_key=AWS_Secret_Access_Key)
        response = session.list_objects_v2(Bucket=S3_Bucket)
        #Download each object
        for obj in response.get('Contents', []):
            object_key = obj['Key']
            local_file_path = os.path.join(local_directory, object_key)
            # Create the local directory if it doesn't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            # Download the files
            session.download_file(S3_Bucket, object_key, local_file_path)
            print(f"File downloaded successfully: {local_file_path}")

    except NoCredentialsError:
        print("Credentials not available or incorrect")
        

if __name__ == "__main__":
    download_all_files_from_s3(S3_Bucket, Local_directory)
