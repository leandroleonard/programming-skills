def time_delta(t1, t2):
    from datetime import datetime
    
    format = "%a %d %b %Y %H:%M:%S %z"
    
    d1 = datetime.strptime(t1, format)
    d2 = datetime.strptime(t2, format)
    
    diff = abs(int((d1 - d2).total_seconds()))
    
    return diff
    
           

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)