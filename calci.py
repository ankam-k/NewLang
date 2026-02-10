def inputer():
    num1 = int(input("Enter the number: "))
    return num1

def switch_case(opertor_select, num1, num2):
    match opertor_select:
        case 1:
            result = num1 + num2
            return result
        case 2:
            result = num1 - num2
            return result
        case 3:
            result = num1 * num2
            return result
        case 4:
            result = num1 / num2
            return result
        case 5:
            result = num1 % num2
            return result
        case 6:
            return "false"

if __name__ == "__main__":
    result = "true"

    while result != "false":
        num1 = inputer()
        num2 = inputer()
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exit")
        opertor_select = int(input("Enter the number to perform operation: "))
        result = switch_case(opertor_select, num1, num2)
        print(result)

        while result != "false":
            print("\n1. To continue\n2. To exit")
            pp = int(input("Choose an option: "))
            match pp:
                case 1:
                    num3 = int(input("Enter the number: "))
                    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exit")
                    opertor_select = int(input("Enter the number to perform operation: "))

                    match opertor_select:
                        case 1:
                            result += num3
                        case 2:
                            result -= num3
                        case 3:
                            result *= num3
                        case 4:
                            result /= num3
                        case 5:
                            result %= num3
                        case 6:
                            result = "false"

                    print(result)
                case 2:
                    result = "false"