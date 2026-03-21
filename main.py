# Main BANKING entry menu
from src.menus.secure_banking_menu import secure_banking_menu
def main_menu():
    
    while True:
        
        print("Welcome to SecureBank")
        input("Press Enter to continue...")
        secure_banking_menu()
        
        

if __name__ == "__main__":
    main_menu()
    