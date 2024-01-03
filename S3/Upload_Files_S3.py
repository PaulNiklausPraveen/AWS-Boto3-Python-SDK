import glob
import boto3
import os
import sys
from multiprocessing.pool import ThreadPool

#Update the IAM Access Keys
AWS_Access_Key_Id = '4a338104d79a418581c7c96af4d80f75'
AWS_Secret_Access_Key = 'gkx3uBYjCIx67b3a4632ef04443972e53ce761154ae'
AWS_Region = 'us-west-2'
S3_Bucket = 'aws-python-boto3-s3bucket-24'
S3_Folder_Name = 'Images/'
Files_Location = 'c:/data/*.jpg'

session = boto3.client('s3', aws_access_key_id=AWS_Access_Key_Id, aws_secret_access_key=AWS_Secret_Access_Key,
                       region_name=AWS_Region)

# The list of files we're uploading to S3
filenames = glob.glob(Files_Location)


def upload(file):
    s3_file = f"{S3_Folder_Name}/{os.path.basename(file)}"
    session.upload_file(file, S3_Bucket, s3_file)


# process files in parallel
pool = ThreadPool(processes=len(filenames) * 3)
pool.map(upload, filenames)
