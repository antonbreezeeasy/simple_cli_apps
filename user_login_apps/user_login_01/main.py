#Main Menu
user_list = [{'id':'1', 'username':'antoshka', 'role':'admin'}, 
             {'id':'2', 'username':'andrew', 'role':'user'},
             {'id':'3', 'username':'natasha', 'role':'admin'}]

def display_main_menu():  
    while True:
        print('User Login Main Menu')
        print("1: View Users")
        print("2: Add Users")
        print("3: Change Password")
        print("4: Exit")
        result = int(input('Select an option'))

        if result == 1:
            view_users()
        elif result == 2:
            add_users()
        elif result == 3:
            change_password()
        elif result == 4:
            exit

def view_users():
    print('View Users')
    for user in user_list:
        print(user)
    x = input('select user id to login or type "exit" to go back to main page ')
    if x == id:
        input('Password')
    elif x == 'exit':
        display_main_menu()  

def add_users():
    pass

def change_password():
    pass

# def exit():
#     pass

# view_users()

display_main_menu()



