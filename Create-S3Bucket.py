import boto3
AWS_REGION = "us-east-2"
resource = boto3.resource("s3", region_name=AWS_REGION)
bucket_name = "aws-s3-bucket"
location = {'LocationConstraint': AWS_REGION}
bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)
print("Amazon S3 bucket has been created")
