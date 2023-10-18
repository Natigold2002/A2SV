def swap_case(s):
    string=""
    for st in s:
         
        if st.islower():
            
            string+= st.upper()
            
        else:  string+= st.lower()
            
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
