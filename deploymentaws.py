import boto
from boto.s3.core import CORSconfiguration

s3_conn = boto.connect_s3()

#Create bucket with_globally_unique_name.
bucket = s3_conn.create_bucket("fintechawsdeploy", location="ap-southwest-2")

cors = CORSconfiguration()
cors.add_rule(allow_method="GET", allowed_origin="*", allowed_header="*")
cors.add_rule(allow_method="POST", allowed_origin="*", allowed_header="*")
cors.add_rule(allow_method="PUT", allowed_origin="*", allowed_header="*")

#apply CORS cofig to our bucket.

bucket.set_cors(cors)
pyton deploymentaws.py