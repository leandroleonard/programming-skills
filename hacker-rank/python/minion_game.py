def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        result = ""
        s = set()
        
        for c in part:
            if c not in s:
                result += c
                s.add(c)
        
        print(result)
        

if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)