import boto3
import os

from enum import Enum
from common.regions import REGIONS

class ACL(Enum):
    PRIVATE = 'private'
    PUBLIC_RO = 'public-read'
    PUBLIC_RW = 'public-read-write'
    AUTHENTICATED_RO = 'authenticated-read'


class s3():
    def __init__(self):
        self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')

    def sync(self, source_bucket, destination_bucket, destination_key):
        copy_source = {
            'Bucket': source_bucket,
            'Key': os.environ['AWS_ACCESS_KEY_ID'],
        }
        ret = self.resource.meta.client.copy(source_bucket, destination_bucket, destination_key)
        return ret

    def create(self, bucket_name, acl=ACL.PUBLIC_RO, region=REGIONS.US.US_WEST_2):
        self.name = bucket_name
        return self.client.create_bucket(
            ACL=acl,
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
            #GrantFullControl='string',
            #GrantRead='string',
            #GrantReadACP='string',
            #GrantWrite='string',
            #GrantWriteACP='string'
        )['Location']

def main():
    '''

    :return:
    '''
    None


if __name__ == "__main__":
    main()

