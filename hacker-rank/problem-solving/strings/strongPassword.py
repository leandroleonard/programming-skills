numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def strong_password(n, password):
    count = 0
    contain_number = contain_special_char = contain_lower = contain_upper = False
    
    for i in password:
        if i in lower_case and contain_lower is False:
            count += 1
            contain_lower = True
            continue
        if i in upper_case and contain_upper is False:
            count += 1
            contain_upper = True
            continue
        if i in numbers and contain_number is False:
            count += 1
            contain_number = True
            continue
        if i in special_characters and contain_special_char is False:
            count += 1
            contain_special_char = True
            continue

    if n < 6:
        r = 6 - n
        if r > 4 - count:
            return r
    
    return 4 - count
            

if __name__ == '__main__':
    n = int(input().strip())
    
    password = input()
    
    answer = strong_password(n, password)

    print(answer)