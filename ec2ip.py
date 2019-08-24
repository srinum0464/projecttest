import boto3

if os.path.exists('/home/ansible/hosts'):
    with open('/home/ansible/hosts','r') as hosts_file:
        ip = hosts_file.read()
else:
    ip = []

ans_ip = []
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if instance.tags == [{'Key': 'Server', 'Value': 'Apache'}]:
        if instance.private_ip_address not in ans_ip:
            ans_ip.append(instance.private_ip_address)

with open('/home/ansible/hosts','a') as file:
    for i in ans_ip:
        if i not in ip:
            file.write(i)
            file.write('\n')