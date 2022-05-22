# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    record.reverse()
    DB = {}
    result = []
    
    for i in range(len(record)):
        temp_record = record[i].split()
        if temp_record[0] == "Change" and temp_record[1] not in DB:
                DB[temp_record[1]] = temp_record[2]
                
        elif temp_record[0] == "Enter" and temp_record[1] not in DB:
                DB[temp_record[1]] = temp_record[2]
    
    record.reverse()
    
    for i in range(len(record)):
        temp_record = record[i].split()        
        if temp_record[0] == "Enter":
            result.append(DB[temp_record[1]]+ "님이 들어왔습니다.") 
        elif temp_record[0] == "Leave":
            result.append(DB[temp_record[1]]+ "님이 나갔습니다.")
            
    return result

