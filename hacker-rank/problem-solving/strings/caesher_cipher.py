def caesher_cipher(n, s, rotation):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotation = rotation % 26
    lower_rotation = lower[rotation:] + lower[:rotation]
    upper_rotation = upper[rotation:] + upper[:rotation]

    answer = ""
    for i in s:
        if i in lower or i in upper:
            if i.isupper():
                answer += upper_rotation[upper.index(i)]
            else:
                answer += lower_rotation[lower.index(i)]
        else:
            answer += i
    
    return answer
            
if __name__ == "__main__":
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    
    print(caesher_cipher(n, s, k))
