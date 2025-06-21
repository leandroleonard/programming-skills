def timeConversion(s: str):
    arr = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00', '12']
    
    isAM = True
    if len(s) > 2:
        isAM = s[len(s) - 2:] == "AM"
    
    if isAM:
        s = s.replace("AM", "")
        if s[0:2] == "12":
            s = s.replace(s[0:2], "00")
            
    else:
        s = s.replace("PM", "")
        if int(s[0:2]) == "00" or int(s[0:2]) == "0":
            index = len(arr) - 1
        elif s[0:2] == "12":
            index = len(arr) - 1
        else:
            index = int(s[0:2]) - 1 
            
        s = s.replace(s[0:2], arr[index])
    
    return s

if __name__ == '__main__':
    s = input()
    
    print(timeConversion(s))