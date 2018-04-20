# Chandler Supple, 4/19/18
# Solution for CS Dojo's video 'Google Coding Interview Question and Answer #1'

def reader(input_):
    x = 0
    flag = 0
    input_ = input_.upper()
    individuals = list(input_)
    length = len(individuals)
    print(individuals)
    for j in range(0,length):
        for i in range(x+1,length):
            if(individuals[x] == individuals[i]):
                flag = 1
                print('The first repeating character listed was: %s' %(individuals[x]))
                break
            if(i >= length-1):
                x = x + 1
                if(x >= length-1):
                    break
            i = i + 1
        if(flag == 1):
            break

# Sample Input: reader('superfluous')
