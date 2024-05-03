import boto3

def get_all_vpcs():
    ec2 = boto3.resource('ec2')
    used_vpcs = []
    for vpcs in ec2.vpcs.all():      
        # replace any non-breaking space characters with regular spaces in the vpc ID
        vpc_id = vpcs.id.replace('\u00A0', ' ')
        used_vpcs.append(vpc_id)
    print('ec2 list using VPCs in a current region configs %s' % used_vpcs)
    
get_all_vpcs()