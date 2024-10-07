import boto3

def create_instance(name, ami_id, instance_type, key_pair):
    ec2_resource = boto3.resource('ec2')
    
    user_data_script = """#!/bin/bash
    echo "Hello, World!" > /home/ec2-user/hello.txt
    chown ec2-user:ec2-user /home/ec2-user/hello.txt"""
    
    instance = ec2_resource.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_pair,
        UserData=user_data_script,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name
                    }
                ]
            }
        ]
    )
    print(f"Created instance {name} with ID: {instance[0].id}")

def main():
    create_instance("My Linux Instance 1", 'YOUR-EC2-AMI', 't2.micro', 'YOUR-KEY-PAIR')
    create_instance("My Linux Instance 2", 'YOUR-EC2-AMI', 't2.micro', 'YOUR-KEY-PAIR')

if __name__ == '__main__':
    main()