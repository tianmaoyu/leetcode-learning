
def roman_to_int(x):
    d_str_list = ["IV","IX", "XL", "XC", "CD", "CM"]
    d_num_list = [4, 9, 40, 90, 400, 900]

    roman_list=["I","V","X","L","C","D","M","IV","IX", "XL", "XC", "CD", "CM"]
    num_list=[1,5,10,50,100,500,1000,4, 9, 40, 90, 400, 900]

    new_str_list=[]
    length=len(x)
    i=0
    while i<= length-1:
        next = ""
        current = x[i]

        if i < length - 1:
            next = x[i+1]
        item = current + next
        if item in d_str_list:
            new_str_list.append(item)
            i+=2
        else:
            new_str_list.append(current)
            i+=1
    print(new_str_list)

    sum=0
    for index,roman in enumerate(new_str_list):
        index=roman_list.index(roman)
        sum+=num_list[index]
    return sum

if __name__ == '__main__':
     roman_to_int("IIV")