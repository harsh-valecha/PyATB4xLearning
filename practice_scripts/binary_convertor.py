# taking input
lst = list(map(int,input('Enter value:').strip().split()))
base= input().strip()
def decimal_convertor(binary:list,*args) -> str:
    binary_str = ''.join(str(i) for i in binary)
    decimal_val = int(binary_str,2)
    base = args[0]
    if base=='b':
        return binary_str
    if base=='d':
        str(decimal_val)
    if base=='x':
        return hex(decimal_val)[2:]
    if base=='o':
        return oct(decimal_val)[2:]

    else:
        return str(decimal_val)


print(decimal_convertor(lst,base))