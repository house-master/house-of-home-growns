import boto3

class AwsS3Store:
    def __init__(self, bucket_name: str, access_key: str, access_secret: str, region: str = 'ap-south-1') -> None:
        self.bucket_name = bucket_name
        self.region = region

        s3 = boto3.resource(
            service_name='s3',
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=access_secret
        )

        self.bucket = s3.Bucket(bucket_name)

        return
    
    def get_base_url(self):
        return "https://" + self.bucket_name + ".s3." + self.region + ".amazonaws.com/"
