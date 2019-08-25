import boto3

ec2_client = boto3.client('ec2')
while True:
    status_check = ec2_client.describe_instance_status(InstanceIds=['i-005b48d4bfabb7832'])
    print(status_check)
    if status_check['InstanceStatuses'] != None:
        if status_check['InstanceStatuses'][0]['InstanceStatus']['Status'] == 'ok' and status_check['InstanceStatuses'][0]['SystemStatus']['Status'] == 'ok':
            exit(0)