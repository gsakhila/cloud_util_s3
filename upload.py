import boto3
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='mybucketakhila')
s3.create_bucket(Bucket='mybucketakhila', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-1'})
data = open('test.txt', 'rb')
s3.Bucket('mybucketakhila').put_object(Key='test.txt', Body=data)
