import boto3
from _pyio import open
import os
if os.path.exists('/home/ansible/hosts'):
    with open('/home/ansible/hosts','r') as hosts_file:
        ip = hosts_file.read()
else:
    ip = []
ans_ip = []
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if {'Key': 'Name', 'Value': 'Apache'} in instance.tags:
        if instance.private_ip_address not in ans_ip:
            ans_ip.append(instance.private_ip_address)
            

with open('/home/ansible/hosts','a') as file:
    for i in ans_ip:
        if i not in ip:
            file.write(i)
            file.write('\r\n')
            print('written ip:',i)
            with open('/etc/ssh/ssh_config','a') as ssh1:
                ssh1.write("\rHost"+"\r "+i)
                ssh1.write('\r\n')
                ssh1.write('\r    StrictHostKeyChecking no')
                ssh1.write('\r\n')
                ssh1.write('\r    UserKnownHostsFile=/dev/null')
                ssh1.write('\r\n')
                print('written ssh file')