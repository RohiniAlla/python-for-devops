#! /bin/python3

import boto3, os
from botocore.exceptions import ClientError

vpc_id = "vpc-0b8c6da4dc0ee6542"
subnet_id = "subnet-0a1afc3cc131b5dba"
security_group_id = "sg-0259bb42f96f33786"
ami_id = "ami-0a15a308c19bc4970"
instance_type = "t2.small"
app_name = "flask"

create_key = True
key_name = "dev-key"
key_location = "/Users/sures/.ssh/na-bonda/"

ec2 = boto3.client('ec2')

def createKeyPair():

    try:
        key_pair = ec2.create_key_pair(KeyName=key_name)

        ssh_private_key = key_pair["KeyMaterial"]
        
        with os.fdopen(os.open(key_location + key_name + ".pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
            handle.write(ssh_private_key)
    except ClientError as e:
        print(e)
    
def createInstance():
    blockDeviceMappings = [
        {
            'DeviceName': "/dev/sda1",
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 20,
                'VolumeType': 'gp2'
            }
        },
    ]

    instances = ec2.run_instances(
        ImageId= ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        SubnetId=subnet_id,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        BlockDeviceMappings=blockDeviceMappings,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': app_name + "-server"
                    }
                ]
            },
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': app_name + "-root-disk"
                    }
                ]
            }
        ]
    )

    print(instances["Instances"][0]["InstanceId"])


if __name__ == "__main__":
    
   # createSecurityGroup()

    if create_key == True:
        createKeyPair();

    createInstance()


# References
# [1] https://codeflex.co/boto3-create-ec2-with-tags/
# [2] https://www.learnaws.org/2020/12/16/aws-ec2-boto3-ultimate-guide/
# [3] https://arjunmohnot.medium.com/aws-ec2-management-with-python-and-boto-3-59d849f1f58f

