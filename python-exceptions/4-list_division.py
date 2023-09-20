#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
                continue
            if my_list_2[i] == 0:
                print("division by 0")
                result.append(0)
            elif not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                result.append(0)
            else:
                result.append(my_list_1[i] / my_list_2[i])
    except:
        pass
    finally:
        return result
