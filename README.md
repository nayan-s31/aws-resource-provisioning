# AWS Resource Provisioning Automation using Python & Boto3

## Project Overview
This project automates the provisioning of AWS resources using Python and Boto3. Instead of manually creating resources through the AWS Management Console, the entire infrastructure can be provisioned using scripts.

The project demonstrates Infrastructure as Code (IaC) concepts by automating the creation of:

Amazon S3 Buckets
AWS IAM Users
Amazon EC2 Instances

A combined automation script (provision_resources.py) provisions all resources in a single execution.

AWS Services Used
Amazon S3
Create and manage S3 buckets
Store files and objects
AWS IAM
Create IAM users
Manage permissions and access control
Amazon EC2
Launch virtual servers
Automate infrastructure deployment

Launch virtual servers
Automate infrastructure deployment
Technologies Used
Python 3
Boto3
AWS CLI
AWS IAM
Amazon S3
Amazon EC2

Features
Automated S3 Bucket Creation
Automated IAM User Creation
Automated EC2 Instance Launch
Error Handling using try-except blocks
Logging Support
Single Script Resource Provisioning

Challenges Faced

During development, the following AWS issues were encountered and resolved:

IllegalLocationConstraintException
Invalid AMI ID Error
UEFI Boot Mode Compatibility Issue
ARM64 vs x86_64 Architecture Mismatch
EC2 UnauthorizedOperation Error
IAM Permission Configuration

These challenges provided hands-on experience in AWS troubleshooting and cloud resource management.

Learning Outcomes

Through this project, I learned:

AWS Infrastructure Automation
Boto3 SDK Usage
IAM User Management
EC2 Provisioning
S3 Bucket Management
Error Handling in Cloud Automation
Infrastructure as Code Concepts





