import json
import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    # Error 1: Unused variable
    unused_var = "This variable is not used"

    # Error 2: Hardcoded AWS credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
        aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
    )

    try:
        # Error 3: Use of print statement instead of logging
        print("Trying to list buckets...")

        response = s3.list_buckets()

        # Error 4: No validation on the response
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]

        # Error 5: Insecure handling of sensitive data
        secret_data = event['secret_data']
        print(f"Received secret data: {secret_data}")

        return {
            'statusCode': 200,
            'body': json.dumps(bucket_names)
        }

    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps("Credentials not available")
        }
