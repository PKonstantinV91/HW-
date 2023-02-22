from stack import*


def balance(list_):
    flag = True
    for el in list_:
        if el in '[{(':
            s.push(el)
        elif el in ']})':
            if s.is_empty():
                flag = False
                break
            a = s.pop()
            if a == '(' and el == ')':
                continue
            elif a == '[' and el == ']':
                continue
            elif a == '{' and el == '}':
                continue
            else:
                flag = False
                break
    return flag




if __name__ == '__main__':

    s = Stack()
    list_  = input("Введите последовательность: ")
    if balance(list_) == True and s.is_empty():
        print("Сбалонсированно")
    else:
        print("Несбалансированно")