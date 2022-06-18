
from google.cloud import storage

bucket_name = "new_storage123"
storage_client = storage.Client()

bucket = storage_client.bucket(bucket_name)
bucket.storage_class = "COLDLINE"
new_bucket = storage_client.create_bucket(bucket, location="EU")

print(
    "Created bucket {} in {} with storage class {}".format(
        new_bucket.name, new_bucket.location, new_bucket.storage_class
    )
)