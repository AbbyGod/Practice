
users = []
tasks = {}
current_user = None

def menu():
    while True:
        print(f"\nTo do list App - Logged in as {current_user}")
        print("Menu")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Delete Tasks")
        print("4. Log Out")

        choice = input("What do you want to do now? ")
        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()  
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid input, Try another selection")



def register():
    global current_user
    name = input("Enter User's name: ")
    password = input("Create your password: ")
    for user in users:
        if user["name"] == name:
            print("⚠️ Username already exists. Try another.")
            return
    user = {"name": name, "password": password}
    users.append(user)
    tasks[name] = []  
    current_user = name
    print(f"Welcome {name} to our system")
    menu()
    

def login():
    global current_user
    log_name = input("Enter User's name: ")
    log_password = input("Enter your password: ")
    for user in users:
        if user["name"] == log_name:
            current_user = log_name
            if user["password"] == log_password:
                print(f"Welcome back {log_name} ")
                menu()
                return
            else:
                print("Wrong password, Try again")
                return 
        
    print("\nthis user does not exist")  
                


def view_task():
    user_tasks = tasks[current_user]
    if not user_tasks:
        print("No task has been added yet")
    else:
        print("\nMy Tasks ")
    for i, task in enumerate(user_tasks, start=1):
        print(f"{i}- {task}" )
def add_task():
    task = input("Enter new task: ")
    tasks[current_user].append(task)
    print(f"Your task {task} has been added")

def delete_task():
    user_tasks = tasks[current_user]
    if not user_tasks:
        print("This task does not exist yet")
        return
    task = input("What task do you want to delete? ")
    
    if task in user_tasks:
        user_tasks.remove(task)
        print(f"The task {task} has been removed") 
    else:
        print("This task does not exist")

while True:
    print("\nWelcome to the login system")
    print("\nMenu")
    print("1. Register")
    print("2. Log in")
    print("3. Exit")
    choice = input("\nWhat do you want to do: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Bye, see you next time")
        break
    else: 
        print("Wrong input, Please chose another one")







