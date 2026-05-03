def count_substring(string, sub_string):
    l , r = 0, len(sub_string)
    count = 0

    while r <= len(string):
        if sub_string == string[l:r]:
            count += 1
        
        l += 1   
        r += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)