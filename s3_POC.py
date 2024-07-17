import boto3

def s3_upload(file_name, bucket_name=os.getenv('S3_BUCKET_NAME')):
    aws_access_key_id = os.getenv('S3_ACCESS_KEY')
    aws_secret_access_key = os.getenv('S3_SECRET_KEY')

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    try:
        print(file_name)
        s3.upload_file(file_name, bucket_name, f"folder_name/{file_name}")
        
    except Exception as e:
        print('error is ',e)
