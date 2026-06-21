import boto3
import logging
from botocore.exceptions import ClientError

# =========================
# Logging Configuration
# =========================

logging.basicConfig(
    filename="provision.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# AWS Clients
# =========================

s3 = boto3.client("s3")
iam = boto3.client("iam")
ec2 = boto3.resource("ec2")

# =========================
# Resource Names
# =========================

BUCKET_NAME = "nayan-capstone-project-0004"  # Must be globally unique
IAM_USER = "project-user-5"                     # Change if already exists

# Your working AMI ID
AMI_ID = "ami-07c687ff88f7820e6"

INSTANCE_TYPE = "t4g.micro"

print("=" * 50)
print("AWS Resource Provisioning Started")
print("=" * 50)

# =========================
# Create S3 Bucket
# =========================

try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        }
    )

    print(f"✅ S3 Bucket Created: {BUCKET_NAME}")
    logging.info(f"S3 Bucket Created: {BUCKET_NAME}")

except ClientError as e:
    print(f"❌ S3 Error: {e.response['Error']['Message']}")
    logging.error(f"S3 Error: {e.response['Error']['Message']}")

# =========================
# Create IAM User
# =========================

try:
    response = iam.create_user(
        UserName=IAM_USER
    )

    print(f"✅ IAM User Created: {IAM_USER}")
    logging.info(f"IAM User Created: {IAM_USER}")

except ClientError as e:
    print(f"❌ IAM Error: {e.response['Error']['Message']}")
    logging.error(f"IAM Error: {e.response['Error']['Message']}")

# =========================
# Launch EC2 Instance
# =========================

try:
    instances = ec2.create_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "Automation-EC2"
                    }
                ]
            }
        ]
    )

    instance = instances[0]

    print(f"✅ EC2 Instance Created")
    print(f"Instance ID: {instance.id}")

    logging.info(f"EC2 Instance Created: {instance.id}")

except ClientError as e:
    print(f"❌ EC2 Error: {e.response['Error']['Message']}")
    logging.error(f"EC2 Error: {e.response['Error']['Message']}")

print("=" * 50)
print("Provisioning Completed")
print("=" * 50)