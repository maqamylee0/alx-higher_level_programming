#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list2 = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            if not isinstance(my_list_1[i], (int, float)) or
            not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            res = my_list_1[i] / my_list_2[i]
            mod = my_list_1[i] % my_list_2[i]
            if mod != 0:
                list2.append(0)
            else:
                list2.append(res)
        except IndexError as e:
            print(str(e))
            list2.append(0)
        except ZeroDivisionError as e:
            print(str(e))
            list2.append(0)
        except TypeError as e:
            print(str(e))
            list2.append(0)
        finally:
            pass
    return list2
