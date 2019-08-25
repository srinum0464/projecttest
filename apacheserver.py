import boto3
import time

ec2 = boto3.resource('ec2')
tags = [{'Key': 'Name','Value': 'Apache'}]
instance = ec2.create_instances(ImageId='ami-03d3bc5ddecc060ce',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='AWSKey',
     SecurityGroupIds= ["sg-d4ae5288"],
     SubnetId= "subnet-16406571",
     TagSpecifications = [{'ResourceType': 'instance', 'Tags': tags}])
print('Checking State...')
instance[0].wait_until_running()
print('Checking Status...')
ec2_client = boto3.client('ec2')
while True:
    status_check = ec2_client.describe_instance_status(InstanceIds=[instance[0].id])
    
    if status_check['InstanceStatuses'] != None:
        if status_check['InstanceStatuses'][0]['InstanceStatus']['Status'] == 'ok' and status_check['InstanceStatuses'][0]['SystemStatus']['Status'] == 'ok':
            print('Status Check Completed...and Up')
            exit(0)
    time.sleep(30)