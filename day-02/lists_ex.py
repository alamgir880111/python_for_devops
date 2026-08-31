cloud = list()

cloud.append("AWS")
cloud.append("AZURE")
cloud.append("GCP")
cloud.append("STC")
cloud.append("ALIBABA")
cloud.append("TATA")
cloud.append("UTHO")

print(cloud)



for clouds in cloud:
    if clouds == "AWS":
        print("This is the market leader")
        
    elif clouds == "UTHO":
        print("This service is very cheap")
        
    else:
        print("everything is bad")
        
        

for clouds in cloud:
    if clouds == "AWS":
        print(f"{clouds} This is the market leader")
        
    elif clouds == "UTHO":
        print(f"{clouds} This service is very cheap")
        
    else:
        print(f"{clouds} everything is bad")



