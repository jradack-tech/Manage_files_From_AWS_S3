import boto3

s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
  print(bucket.name)

# Create an S3 access object
s3 = boto3.client("s3")

s3.upload_file(
  Filename="data/downloaded_from_s3.txt", 
  Bucket="bucket_name", 
  Key="test.txt", 
)