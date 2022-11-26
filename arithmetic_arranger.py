def arithmetic_arranger(input_value, printresult=False):
    """
    Create a function that receives a list of strings that are arithmetic problems
    and returns the problems arranged vertically and side-by-side.
    The function should optionally take a second argument.
    When the second argument is set to True, the answers should be displayed.
    """

    length_input_value = len(input_value)
    if length_input_value < 6:
        pass
    else:
        print("Error: Too many problems.")
        return

    seperate_value = []
    first_num = []
    second_num = []
    operator = []
    res = []

    for i in range(length_input_value):
        seperate_value = input_value[i].split(" ")
        first_num.append(seperate_value[0])
        operator.append(seperate_value[1])
        second_num.append(seperate_value[2])

    for j in range(length_input_value):
        sign = operator[j]
        if sign in ("+", "-"):
            signs = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
            if first_num[j].isdigit() and second_num[j].isdigit():
                result = signs[sign](int(first_num[j]),int(second_num[j]))
                res.append(result)
            else:
                print("Error: nums must only contain digits.")
                return
        else:
            print("Error: operator must be '+' or '-'.")
            return

    max_length_input = 0
    for j in range(length_input_value):
        length_input = max(len(first_num[j]), len(second_num[j]))
        max_length_input = max(max_length_input,length_input)

    for j in range(length_input_value):
        length_input = max(len(first_num[j]), len(second_num[j]))
        if max_length_input < 5:
            print(" "*(length_input+2-len(first_num[j])) + first_num[j], end="    ")
        else:
            print("Error: nums cannot be more than four digits.")
            return
    print()

    for j in range(length_input_value):
        length_input = max(len(first_num[j]), len(second_num[j]))
        print(operator[j] + " "*(length_input+1-len(second_num[j])) + second_num[j], end="    ")
    print()

    for j in range(length_input_value):
        length_input = max(len(first_num[j]), len(second_num[j]))
        print("-"*(length_input+2), end="    ")
    print()



    if printresult is True:
        for j in range(length_input_value):
            length_input = max(len(first_num[j]), len(second_num[j]))
            print(" "*(length_input+1-len(str(res[j]))), str(res[j]), end="    ")
    else:
        return
