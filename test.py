import boto3

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if {'Key': 'Name', 'Value': 'Apache'} in instance.tags:
        print(instance.tags)