import boto3

class AWSUtils:
    
    def __init__(self):
        self.s3 = self.get_connection("s3")
        
        
    def get_connection(self,service):
        s3 = boto3.client(service)
        return s3

    def show_buckets(self):
        response = self.s3.list_buckets()["Buckets"]

        for bucket in response:
            print(f"Name: {bucket["Name"]}")
            
            
    def create_buckets(self, bucket_name, region):
        try:
            response1 = self.s3.create_bucket(
                Bucket = bucket_name,  CreateBucketConfiguration = {
                "LocationConstraint": region
                        }
            )
        
            print(f"Bucket : {bucket_name} created successfully")
            
        except:
            print("error occured")
            
    def upload_file(self, file_name, bucket_name, object_name):
        try:
            response2 = self.s3.upload_file(file_name, bucket_name, object_name)
            print("file uploaded successfully")
            
        except:
            print("Not possible to upload the file")
    
    
if __name__ == "__main__": # ye file ka jo execution hoga woh if condition ka andar hoga
      
    aws = AWSUtils()
    aws.show_buckets()
    aws.create_buckets("new-lullu-pullu1", "eu-north-1")
    aws.upload_file("app2.log", "rahman-ki-ldk", "lala")

 

# s3 = get_connection("s3")
# show_buckets(s3)
# create_buckets(s3, "rahman-ki-ldkg", "eu-north-1")
# upload_file(s3, "app.log", "rahman-ki-ldk", "new_file" )
        