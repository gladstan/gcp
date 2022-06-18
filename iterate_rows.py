from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table = client.get_table('t-sunlight-352712.test_dataset.test_123')

row_iterator = client.list_rows(table)
print(row_iterator.to_dataframe())


# project = "bigquery-public-data"
# dataset_id = "samples"
# table_id = "shakespeare"

# destination_uri = "gs://{}/{}".format(bucket_name, "shakespeare.csv")
# dataset_ref = bigquery.DatasetReference(project, dataset_id)
# table_ref = dataset_ref.table(table_id)

# extract_job = client.extract_table(
#     table_ref,
#     destination_uri,
#     # Location must match that of the source table.
#     location="US",
# )  # API request
# extract_job.result()  # Waits for job to complete.

# print(
#     "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri)
# )

#print(row_iterator.items())

#for data in row_iterator:
    #print(type(data))
 #   print(data.items())
# # fix: next(iter(row_iterator))
# next(row_iterator)