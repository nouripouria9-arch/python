# import
import os
contacts={}
class Contact:
    def __init__(self,firstname,lastname,phone,adrress):
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.adrress=adrress
# def
def add_contact():
    os.system('cls')
    print("--------Add contact--------")
    phone=input("Enter phone number= ")
    if phone not in contacts:
        firstname=input("Enter first name= ")
        lastname=input("Enter last name= ")
        adrress=input("Enter adrress= ")
        contacts[phone]=Contact(firstname,lastname,phone,adrress)
        input("Contact added successfully")
    else:
        input("Contact already exists")



def remove_contact():
    os.system("cls")
    print("--------Remove contact--------")
    phone=input("Enter phone number= ")
    if phone in contacts:
        del contacts[phone]
        input("Contact removed successfully")
    else:
        input("Contact does not exist")




def update_contact():
    os.system("cls")
    print("--------Update contact--------")
    phone=input("Enter phone number= ")
    if phone in contacts:
        newfirstname=input("Enter newfirstname= "+contacts[phone].firstname+'=>')
        newlastname=input("Enter newlastname= "+contacts[phone].lastname+'=>')
        newadrress=input("Enter newadrress= "+contacts[phone].adrress+'=>')
        contacts[phone].firstname=newfirstname
        contacts[phone].lastname=newlastname
        contacts[phone].adrress=newadrress
        input("Contact updated successfully")
    else:
        input("Contact does not exist")



def find_contact():
    os.system("cls")
    print("--------Find contact--------")
    phone=input("Enter phone number= ")
    if phone in contacts:
        Contact=contacts[phone]
        print("{}-{}-{}-{}".format(Contact.firstname,Contact.lastname,Contact.phone,Contact.adrress))
        input("Press enter to continue")
    else:
        input("Contact does not exist so press enter to continue")



def list_contacts():
    os.system("cls")
    print("--------List contacts--------")
    for phone in contacts:
        Contact=contacts[phone]
        print("{}-{}-{}-{}".format(Contact.firstname,Contact.lastname,Contact.phone,Contact.adrress))
    input()



def display():
    print("--------welcome to this program--------")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Update contacts")
    print("4. Find contact")
    print("5. List contacts")
    print("6. Exit")



# main loop
while True:
    display()
    option = input("Enter your option between 1-6= ")
    if option == '1':
        add_contact()
    elif option == '2':
        remove_contact()
    elif option == '3':
        update_contact()
    elif option == '4':
        find_contact()
    elif option == '5':
        pass
    else:
        break