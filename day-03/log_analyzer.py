import json
def read_log():
    with open("app.log", "r") as file:
        result = file.readlines()
        return result
    
def log_analyzer(lines):
    log_count = {
        "INFO" : 0,
        "WARNING" : 0,
        "ERROR" : 0
    }    
    
    for line in lines:
        if "INFO" in line:
            log_count ["INFO"] += 1
            
        elif "WARNING" in line:
                    log_count ["WARNING"] += 1
                    
        elif "ERROR" in line:
                    log_count ["ERROR"] += 1
                    
        else:
            pass
        
    return log_count

def write_json(count):
    with open("output.json", "w+") as json_file:
        json.dump(count, json_file)
    
lines = read_log()
count = log_analyzer(lines)
write_json(count)
print(count)