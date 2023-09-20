#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if my_list_1 is out of range
            if i >= len(my_list_1):
                raise IndexError("out of range")

            # Check if my_list_2 is out of range
            if i >= len(my_list_2):
                raise IndexError("out of range")

            # Divide the elements
            result.append(my_list_1[i] / my_list_2[i])

        except ZeroDivisionError:
            result.append(0)
            print("division by 0")

        except TypeError:
            result.append(0)
            print("wrong type")

        except IndexError as e:
            result.append(0)
            print(e)

    return result
