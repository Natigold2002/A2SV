import textwrap

def wrap(string, max_width):
    mod=len(string)%max_width
    ans=[]
    for i in range(0,len(string)-mod,max_width):
        ans.append(string[i:i+max_width])
    ans.append(string[len(string)-mod:])
    return '\n'.join(ans)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
