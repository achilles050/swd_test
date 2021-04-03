number = 25

def fac(n):
    try:
        n = int(n)
    except Exception as e:
        print('int only', e)
        return None

    tmp = 1
    if n == 0:
        return tmp
    elif n > 0:
        for value in range(n):
            tmp *= value+1
        return tmp
    else:
        print('possitive int only')
        return None


def findzero(n):
    try:
        n = int(n)
    except Exception as e:
        return None

    i = 0
    tmp = 0
    count = 0
    while(True):
        i += 1
        if n % (10**i) == 0:
            count += 1
        else:
            break
    return count

print('your number: ',number)
print('factorial of number: ',fac(number))
print('number of contiguous zero: ',findzero(fac(number)))