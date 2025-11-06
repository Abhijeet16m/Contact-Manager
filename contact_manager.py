import os
import json
from datetime import datetime
import re

def add_contact():
    print()
    with open("contacts.json", "r") as c:
        data = json.load(c)
    user = get_inputs
    while(True):
        name = user.get_name()
        if not name.title() in data:
            break
        else:
            print("This name already exist in your contact list")
    email = user.get_email_address()
    mobile = user.get_mobile_number()
    contact = {"name": name.title(), "email": email, "mobile": mobile}
    data[name.title()] = contact
    data = {key: data[key] for key in sorted(data.keys())}
    with open("contacts.json", "w") as c:
        json.dump(data, c, indent=4)

    print("Contact saved successfully!!")
    input("\nEnter to Continue")

def get_contact_list():
    print()
    with open("contacts.json", "r") as c:
        data = json.load(c)
    print(f"There are {len(data)} contacts\n")
    for names in data:
        print(f"Name: {data[names]["name"]}\nMobile number: +91 {data[names]["mobile"]}\nEmail: {data[names]["email"]}\n")
    input("Enter to Continue")

def search_contact():
    print()
    user = get_inputs
    search = user.get_name()
    with open("contacts.json", "r") as c:
        data = json.load(c)
    results = [i for i in data if search.lower() in i.lower()]
    print(f"{len(results)} results found\n")
    for names in results:
        print(f"Name: {data[names]["name"]}\nMobile number: +91 {data[names]["mobile"]}\nEmail: {data[names]["email"]}\n")
    input("Enter to Continue")


def delete_contact():
    print()
    with open("contacts.json", "r") as c:
        data = json.load(c)
    user = get_inputs
    to_delete = user.get_name()
    results = [i for i in data if to_delete.lower() in i.lower()]
    if len(results):
        print(f"{len(results)} results found\n")
        for i in range(len(results)):
            print(f"{i+1}. Name: {data[results[i]]["name"]}\nMobile Number: {data[results[i]]["mobile"]}\n")
        action = user.get_operation("Which one do You want to delete: ", len(results))
        data.pop(results[action-1])
        with open("contacts.json", "w") as c:
            json.dump(data, c, indent=4)
        print("Contact deleted Successfully!!\n")
        input("Enter to Continue")
    else:
        print("No Result Found!!")
        input("Enter to Continue")

def your_details():
    print()
    with open("login_details.json", "r") as ld:
        data = json.load(ld)
    print("Your Details: ")
    for i in data:
        print(f"{i.title()}: {data[i]}")
    input("\nEnter to Continue")

class get_inputs:
    @staticmethod
    def get_name():
        while(True):
            name = input("Enter Name: ")
            if name.strip():
                return name
            else:
                print("Invalid Name!")

    @staticmethod
    def get_email_address():
        while True:
            email = input("Enter Email Address (optional): ")
            match = re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", email)
            if match or email == "":
                return email
            else:
                print("Invalid Email!")

    @staticmethod 
    def get_mobile_number():    
        while(True):
            mobile = input("Enter Mobile Number: ")
            match = re.match("^[6-9][0-9]{9}$", mobile)
            if match:
                return mobile
            else:
                print("Invalid Mobile Number!")
    
    @staticmethod
    def get_operation(s, n):
        while(True):
            try:
                user = int(input(s))
                if 0<user<=n:
                    return user
                else:
                    print("Invalid Command!")
            except:
                print("Invalid Command!")

def login():
    input("You don't have a account press enter to make your account")
    user = get_inputs
    name = user.get_name()
    email = user.get_email_address()
    mobile = user.get_mobile_number()

    details = {"name": name.title(), "email": email, "mobile": mobile}
    with open("login_details.json", "w") as ld:
        json.dump(details, ld, indent=4)
    print("Login Complete.\n\n")

def greet():
    current_time = datetime.now().hour
    with open("login_details.json") as j:
        login = json.load(j)
        name = login["name"]
    if 5<=current_time<12:
        print(f"Good Morning, {name}")
    elif 12 <= current_time < 17:
        print(f"Good Afternoon, {name}")
    elif 17 <= current_time < 21:
        print(f"Good Evening {name}")
    else:
        print(f"Hey, {name}")

def check_user_login_status():
    if os.path.exists("login_details.json"):
        return True
    else:   
        return False

def main():
    user_login = check_user_login_status()
    if not user_login:
        login()
    if not os.path.exists("contacts.json"):
        with open("contacts.json", "w") as c:
            json.dump({}, c)

    greet()
    while(True):
        print()
        print("1. Add Contact\n2. Get Contact List\n3. Search Contact\n4. Delete Contact\n5. See Your details\n6. Exit\n")
        choice = get_inputs
        user = choice.get_operation("What You want to do?: ", 6)
        if user == 1:
            add_contact()
        elif user == 2:
            get_contact_list()
        elif user == 3:
            search_contact()
        elif user == 4:
            delete_contact()
        elif user == 5:
            your_details()
        elif user == 6:
            print()
            print("Ending the program! have a nice day")
            return
        else:
            print()
            print("I am really sorry, I think something went wrong!")


if __name__ == "__main__":
    main()