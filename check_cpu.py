import psutil
 
def check_cpu_threshold():
     
    cpu_threshold = int(input("Enter the cpu threshold"))
     
    current_cpu = psutil.cpu_percent(interval=1)
    print ("current cpu is :", current_cpu)
    
    if current_cpu > cpu_threshold:
        print("cpu alert email sent!!!")
        
    else:
        print("everything is ok")
        
check_cpu_threshold()