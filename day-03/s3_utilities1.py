import boto3

def get_connection(service):
    s3 = boto3.client(service)
    return s3

def show_buckets(s3):
    response = s3.list_buckets()["Buckets"]

    for bucket in response:
        print(f"Name: {bucket["Name"]}")
        
        
def create_buckets(s3, bucket_name, region):
    try:
        response1 = s3.create_bucket(
            Bucket = bucket_name,  CreateBucketConfiguration = {
            "LocationConstraint": region
                    }
        )
    
        print(f"Bucket : {bucket_name} created successfully")
        
    except:
        print("error occured")
        
def upload_file(s3, file_name, bucket_name, object_name):
    try:
        response2 = s3.upload_file(file_name, bucket_name, object_name)
        print("file uploaded successfully")
        
    except:
        print("Not possible to upload the file")
    
    
 

s3 = get_connection("s3")
show_buckets(s3)
create_buckets(s3, "rahman-ki-ldkg", "eu-north-1")
upload_file(s3, "app.log", "rahman-ki-ldk", "new_file" )
        
        
        
