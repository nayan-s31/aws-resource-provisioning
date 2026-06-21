import boto3

s3 = boto3.client('s3')

bucket_name = 'capstone-s3-project-040'  # Must be globally unique

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print(f"Bucket {bucket_name} created successfully")