def mars_exploration(s):
    n = len(s) / 3
    count = i = 0
    while i <= len(s) - 3:
        j = s[i:i+3]
        if j[0] != "S": count += 1
        if j[1] != "O": count += 1
        if j[2] != "S": count += 1
        i+=3
    return count
        
    
if __name__ == '__main__':
    s = input()
    print(mars_exploration(s))