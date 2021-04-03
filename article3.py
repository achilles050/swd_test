mylist = [1,2,1,3,5,6,4]

def findmaxindex(mylist):
    max_index = 0
    for index in range(len(mylist)):
        try:
            if index == 0:
                max_index = index
            if mylist[index] >= mylist[max_index]:
                max_index = index
        except Exception as e:
            print('error before finish ',e)
            return max_index
    return max_index

maxindex = findmaxindex(mylist)
print(f'max index = {maxindex}\nmax value = {mylist[maxindex]}')