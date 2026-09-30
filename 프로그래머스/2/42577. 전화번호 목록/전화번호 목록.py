def solution(phone_book):
    hash_map  = set(phone_book)
    
    for pn in phone_book:
        prefix = ""
        for c in pn[:-1]:
            prefix += c
            
            if prefix in hash_map:
                return False
    return True