def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count
    
print(count_vowels("Si Aaron ay pogi"))