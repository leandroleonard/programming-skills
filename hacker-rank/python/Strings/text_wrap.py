import textwrap

def wrap(string, max_width):
    string = list(string)
    position = max_width
    while True:
        if position < len(string):
            string.insert(position, '\n');
        else:
            break
        position += max_width + 1

    return "".join(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)