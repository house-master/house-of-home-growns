

from datastore.aws_s3_store import AwsS3Store


class LargeFileService:
    def __init__(self, bucket_datastore: AwsS3Store) -> None:
        self.bucket_datastore = bucket_datastore
        return
    
    def get_url(self, name: str):
        return self.bucket_datastore.get_base_url() + name

    def download(self, name: str):
        self.bucket_datastore.bucket.download_file(Key=name, Filename=name)
        return

    def delete_one(self, name: str):
        self.bucket_datastore.bucket.delete_key(name)
        return

    def upload_one(self, file_path: str):
        filekey = file_path.split("/")[len(file_path.split("/")) - 1]
        self.bucket_datastore.bucket.upload_file(
            Filename=file_path, Key=filekey)
        return

