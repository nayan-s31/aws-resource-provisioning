import boto3

iam = boto3.client('iam')

response = iam.create_user(
    UserName='project-user-4'
)

print(response)