# AWS Resource Provisioning Automation using Python & Boto3

## Project Overview

This project automates the provisioning of AWS resources using Python and Boto3. Instead of manually creating resources through the AWS Management Console, the entire infrastructure can be provisioned using scripts.

The project demonstrates Infrastructure as Code (IaC) concepts by automating the creation of:
- Amazon S3 Buckets
- AWS IAM Users
- Amazon EC2 Instances

A combined automation script (provision_resources.py) provisions all resources in a single execution.

## AWS Services Used

### Amazon S3
- Create and manage S3 buckets
- Store files and objects

### AWS IAM
- Create IAM users
- Manage permissions and access control

### Amazon EC2
- Launch virtual servers
- Automate infrastructure deployment

## Challenges Faced

During development, the following AWS issues were encountered and resolved:

1. IllegalLocationConstraintException
2. Invalid AMI ID Error
3. UEFI Boot Mode Compatibility Issue
4. ARM64 vs x86_64 Architecture Mismatch
5. EC2 UnauthorizedOperation Error
6. IAM Permission Configuration

These challenges provided hands-on experience in AWS troubleshooting and cloud resource management.

## Learning Outcomes

Through this project, I learned:

- AWS Infrastructure Automation
- Boto3 SDK Usage
- IAM User Management
- EC2 Provisioning
- S3 Bucket Management
- Error Handling in Cloud Automation
- Infrastructure as Code Concepts





