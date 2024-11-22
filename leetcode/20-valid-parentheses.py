from idlelib.pyparse import trans


def fun(str):
    left_list = ["(", "{", "["]
    right_list = [")", "}", "]"]

    left_find = []
    right_find = []

    for i in str:
        if i in left_list:
            left_find.append(i)
        elif i in right_list:
            right_find.insert(0, i)

    if len(left_find) != len(right_find):
        return False

    for left in left_find:
        left_index = left_list.index(left)
        right = right_list[left_index]
        right_index = right_find.index(right)
        if left_index != right_index:
            return False
    return True


def fun_v2(str):
    stack = list()
    for i in str:
        if i == "(":
            stack.append(")")
        elif i == "[":
            stack.append("]")
        elif i == "{":
            stack.append("}")
        else:
            if len(stack) == 0: return False
            ch = stack.pop()
            if ch != i: return False

    return True


print(fun_v2("()[]{}"))
