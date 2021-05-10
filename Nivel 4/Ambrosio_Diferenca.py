def XOR(arr_bit):
    result = 0
    for bin in arr_bit.split():
        bin = format(int(bin),'b')
        result ^= int(bin,2)
    return format(result,'b')
T = int(input())
n = 0
while(True and n <= T):
    try:
        a = input()
        if(n < T):
            total = XOR(a)
            total = list(total)
            difference = total.count('1')
            n += 1
        else:
            break
        print(difference)
    except EOFError:
        break
