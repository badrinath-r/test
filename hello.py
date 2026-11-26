def add_numbers(first: float, second: float) -> float:
    return first + second


def main() -> None:
    print("Two-Number Addition")

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print(f"The sum is: {add_numbers(first, second)}")


if __name__ == "__main__":
    main()