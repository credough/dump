def len_check(word):
    if len(word) > 4:
        return "Long"
    else:
        return "Short"
    
print(len_check("haha"))
print(len_check("Python"))