
def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()

def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    combined_name = format_name(first_name, last_name)
    print(f"Hello {combined_name}!")

if __name__ == "__main__":
    main()