s3_buckets_lists = ["CloudTest_bucket", "CloudDev_bucket", "CloudProd_bucket"]

s3_buckets_lists.append("CloudZerotrust_bucket")

s3_buckets_lists.remove("CloudDev_bucket")

print(s3_buckets_lists)

