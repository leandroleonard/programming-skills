upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def CamelCase(s):
    if len(s) == 0: return 0
    words = 1
    for i in s: 
        if i in upper_case: words += 1
    return words
        
if __name__ == '__main__':
    s = input()
    
    answer = CamelCase(s)
    print(answer)

