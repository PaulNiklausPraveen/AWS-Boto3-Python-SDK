import glob
import boto3
import os
import sys
from multiprocessing.pool import ThreadPool

AWS_Access_Key_Id = '8d1fd22d-93ce-4766-bf93-c5ea18618edb'
AWS_Secret_Access_Key = '8d1fd22d-93ce-4766-bf93-c5ea18618edbdNVefl2/l3Tl5e'
AWS_Region = 'us-west-2'
S3_Bucket = 'pythons3-bucket-20241'
S3_Folder_Name = 'Folder1/'
Files_Location = 'c:/data/*.logs'

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
