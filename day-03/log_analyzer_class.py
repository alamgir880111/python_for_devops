import json

class LogAnalyzer:
    
    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file
        
        
    def read_log(self):
        with open(self.file_name, "r") as file:
            result = file.readlines()
            return result
        
    def log_analyzer(self):
        log_count = {
            "INFO" : 0,
            "WARNING" : 0,
            "ERROR" : 0
        } 
        
        lines = self.read_log()   
        
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

    def write_json(self):
        log_count = self.log_analyzer()
        with open(self.output_file, "w+") as json_file:
            json.dump(log_count, json_file)
            
            
log_1 = LogAnalyzer("app2.log", "output1.json")

log_1.write_json()

        
    # lines = read_log()
    # count = log_analyzer(lines)
    # write_json(count)
    # print(count)