# main.py
def main():
    while True:
        print("\n--- DevOps Dashboard ---")
        print("[1] System Info")
        print("[2] Log Checker")
        print("[3] Task List")
        print("[0] Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("System Info selected") # Placeholder for now
        elif choice == '2':
            print("Log Checker selected") # Placeholder for now
        elif choice == '3':
            print("Task List selected")    # Placeholder for now
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
