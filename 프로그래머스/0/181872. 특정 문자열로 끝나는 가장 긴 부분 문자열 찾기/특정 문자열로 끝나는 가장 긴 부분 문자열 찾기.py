def solution(myString, pat):
    n = len(pat)
    last_idx = 0
    
    for i in range(len(myString) - n + 1):
        if myString[i:i+n] == pat:  
            last_idx = i + n        
    
    return myString[:last_idx]
