import boto3

# Replace the following variables with your own values according to environment
aws_access_key_id = 'type access key id'
aws_secret_access_key = 'type secret access key'
region_name = 'us-east-1'

# Create a Boto3 session with your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def create_instance():
    ec2_client = session.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId='ami-0889a44b331db0194',
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2instance-keypair",
        SubnetId="subnet-0fa86e9d04c3cc79b"
    )
    print(instances["Instances"][0]["InstanceId"])

create_instance()
