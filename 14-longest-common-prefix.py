
# https://leetcode.cn/problems/longest-common-prefix/

def fun(str_list):

    first=str_list[0]

    for word in str_list[1:]:
        temp_index=-1
        length = len(first)
        for index,char in enumerate(word):
            if length < index+1:break
            if char == first[index]: temp_index=index
            else:break


        if temp_index==-1: return ""

        first=word[:temp_index+1]

    return first




if __name__ == '__main__':
    result= fun(["cir","car"])
    print(result)