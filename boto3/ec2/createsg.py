def createSecurityGroup():
    global security_group_id
    try:
        response = ec2.create_security_group(GroupName=app_name + "-sg",
                                            Description=app_name + " Security Group",
                                            VpcId=vpc_id,
                                            TagSpecifications=[
                                                    {
                                                        'ResourceType': 'security-group',
                                                        'Tags': [
                                                            {
                                                                'Key': 'Name',
                                                                'Value': app_name + "-sg"
                                                            }
                                                        ]
                                                    },
                                                ],
                                            )
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        ingress = ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {
                                    'IpProtocol': 'tcp',
                                    'FromPort': 80,
                                    'ToPort': 80,
                                    'IpRanges': [
                                        {
                                            'CidrIp': '0.0.0.0/0'
                                        }
                                    ]
                                },
                                {
                                    'IpProtocol': 'tcp',
                                    'FromPort': 22,
                                    'ToPort': 22,
                                    'IpRanges': [
                                        {
                                            'CidrIp': '0.0.0.0/0'
                                        }
                                    ]
                                }
                            ])
        print('Ingress Successfully Set %s' % ingress)
    except ClientError as e:
        print(e)