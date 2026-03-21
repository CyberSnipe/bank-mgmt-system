# Secure Banking Menu
def secure_banking_menu():
    
    while True:
        print("\n=== Welcome To SecureBank ===\n")
        print("  SecureBank Main Menu")
        print("\t1. Create Account")
        print("\t2. Deposit")
        print("\t3. Withdrawl")
        print("\t4. Check Balance")
        print("\t5. Save Bank Data")
        print("\t6. Load Bank Data")
        print("\t0. Exit\n")
        
        choice = input("Enter a number...: ").strip()
                
        if choice == '1':
            #create_account()
            print("Coming soon...create_account")
            input("Press Enter to continue...")
        elif choice == '2':
            #deposit()
            print("Coming soon...deposit")
            input("Press Enter to continue...")
        elif choice == '3':
            #withdrawl()
            print("Coming soon...withdrawl")
            input("Press Enter to continue...")
        elif choice == '4':
            #check_balance()
            print("Coming soon...check_balance")
            input("Press Enter to continue...")
        elif choice == '5':
            #save_bank_data()
            print("Coming soon...save_bank_data")
            input("Press Enter to continue...")
        elif choice == '6':
            #load_bank_data
            print("Coming soon...load_bank_data")
            input("Press Enter to continue...")
        elif choice == '0':
            print("Thank you for visiting SecureBank....\n")
            break
        else:
            print("Invalid entry. Enter a valid number...0-6\n")
            input("Press Enter to contiue...")

if __name__ == "__main__":
    secure_banking_menu()