import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-07c687ff88f7820e6',
    InstanceType='t4g.micro',
    MinCount=1,
    MaxCount=1
)

print("Instance ID:", instances[0].id)