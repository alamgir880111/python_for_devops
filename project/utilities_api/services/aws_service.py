import boto3
from datetime import datetime, timedelta, timezone

def get_bucket_info():
    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()
    
    new_buckets = []
    old_buckets = []
    current_time = datetime.now(timezone.utc).astimezone()
    for bucket in buckets["Buckets"]:
       
        creaion_date = bucket["CreationDate"]
    
        Day_01_ago = current_time - timedelta(days=1)
        
        if creaion_date < Day_01_ago:
            old_buckets.append(bucket["Name"])
        else:
            new_buckets.append(bucket["Name"])
        
    return {
         
        "New_Buckets" :new_buckets,
        "Old_Buckets" :old_buckets
        
    } 
    
        
    

    
        
   