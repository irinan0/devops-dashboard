def check_log():
    filename = input("Enter the log filename to check: ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
