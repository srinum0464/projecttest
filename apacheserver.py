import boto3
from jedi.evaluate.context import instance
from Tools.scripts.ptags import tags

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

instance[0].wait_until_running()
