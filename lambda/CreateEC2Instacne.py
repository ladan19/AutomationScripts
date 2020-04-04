import os  
import boto3

AMI= os.environ['AMI']
TYPE= os.environ['TYPE']
KEY= os.environ['KEY']
VOLUMETYPE= os.environ['VOLUMETYPE']
#VOLUMESIZE= os.environ['VOLUMESIZE']
SUBNET= os.environ['SUBNET']

ec2=boto3.resource('ec2')

def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=TYPE,
        KeyName=KEY,
        BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'VolumeSize': 13,
                'VolumeType': 'gp2',
                'Encrypted': True
            }
        },
    ],
        SubnetId=SUBNET,
        MaxCount=1,
        MinCount=1
    )
    print("New instance created:", instance[0].id)