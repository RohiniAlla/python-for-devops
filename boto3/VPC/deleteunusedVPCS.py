import boto3

def get_unused_vpcs():
    ec2 = boto3.resource('ec2')
    unused_vpcs = []
    used_vpcs = []
    for vpcs in ec2.vpcs.all():      
        # replace any non-breaking space characters with regular spaces in the vpc ID
        vpc_id = vpcs.id.replace('\u00A0', ' ')
        unused_vpcs.append(vpc_id)
    print('ec2 list not using VPCs %s' % unused_vpcs)
    

#def delete_volumes(volumes):
#    ec2 = boto3.resource('ec2')
#    for volume in volumes:
#        print(f"Deleting volume {volume}")
#        ec2.Volume(volume).delete()

#def main():
    #regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]
    #for region in regions:
    #    print(f"Checking for unused vpcs in region {region}")
    #    boto3.setup_default_session(region_name=region)
get_unused_vpcs()
        #if unused_volumes:
        #    delete_volumes(unused_volumes)
        #else:
        #    print(f"No unused volumes found in region {region}")

#if __name__ == "__main__":
 #   main()