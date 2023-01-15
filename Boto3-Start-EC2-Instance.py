#This python script get Instance ID as input and start the EC2 instance and display the current status of the instance as output
#Reference URL : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html

import boto3
import time
import json
aws_access_key_id = 'ABCDEFGHIJKLMNOP12345'
aws_secret_access_key = 'fae2ff7bb6d46bbb0bda2153aaaf09e25575d6d8'
region_name = 'us-east-2'
session = boto3.session.Session(aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=region_name)
ec2resource = session.resource('ec2')
Instance_ID= input("Enter the Instance ID of the EC2 Instance?\n")
ec2resource.Instance(Instance_ID).start()
print("\nScript pause for 30 seconds,waiting for Instance to come online\n")
time.sleep(30)
response = ec2resource.meta.client.describe_instance_status(InstanceIds=[Instance_ID],IncludeAllInstances=True)
output=(response['InstanceStatuses'][0])
print (json.dumps(output, indent=1, default=str))


