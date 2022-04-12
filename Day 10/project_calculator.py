from art import logo


def add(num1: float, num2: float) -> float:
    val = num1 + num2
    return val


def subtract(num1: float, num2: float) -> float:
    val = num1 - num2
    return val


def multiply(num1: float, num2: float) -> float:
    val = num1 * num2
    return val


def divide(num1: float, num2: float) -> float:
    val = num1 / num2
    return val


def main():
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    continue_calculation = True
    use_prev_result = False

    while continue_calculation:
        if not use_prev_result:
            n1 = float(input("What's the first number? : "))
        else:
            n1 = result
        for operation in operations:
            print(operation)
        perform_operation = input("Pick an operation: ")
        if perform_operation not in operations:
            print(f"Wrong Operation! Please choose one of the operations displayed. Please start again.\n")
            continue
        n2 = float(input("What's the next number? : "))

        result = operations[perform_operation](n1, n2)
        print(f"{n1} {perform_operation} {n2} = {result}")

        continue_current_operation = input(
            f"Type yes to continue calculating with {result},  type no to start a new calculator, or bye to stop: "
        )
        if continue_current_operation == "yes":
            use_prev_result = True
        elif continue_current_operation == "bye":
            break
        else:
            print("Starting new calculator!!!")
            print(logo)
            use_prev_result = False


if __name__ == "__main__":
    main()
