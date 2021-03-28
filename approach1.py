import sys

class Contact():
    def __init__(self, name, lastName, age, phone):
        self.name     = name
        self.lastName = lastName
        self.age      = age
        self.phone    = phone
        
    def editContact(self, name, lastName, age, phone):
        self.name     = name
        self.lastName = lastName
        self.age      = age
        self.phone    = phone

class MyContacts():
    
    def __init__(self):
        self.totalContacts= []
        
    def start(self):
        print("="*30)
        print("WELCOME TO YOUR CONTACTS")
        print("="*30)
        print("\t1.- View All Contacts")
        print("\t2.- View Single Contact")
        print("\t3.- Add Contact")
        print("\t4.- Edit Contact")
        print("\t5.- Delete Contact")
        print("\t6.- DELETE EVERYTHING (:S)")
        print("\t0.- Exit")
        opcion = int(input("Please pick an option: "))
        
        while (opcion>6 or opcion <0):
            opcion = int(input("Please pick a valid option: "))
        
        while(opcion != 0):
            if opcion == 1:
                self.viewAllContacts()            
            if opcion == 2:
                self.viewSingleContact()
            if opcion == 3:
                self.newContact()
            if opcion == 4:
                self.editContact()
            if opcion == 5:
                self.deleteContact()
            if opcion == 6:
                self.deleteEverything()
            opcion = int(input("Please pick a valid option: "))

        opcion = 0
        print("Goodbye!!")
        sys.exit()
                  
    def newContact(self):
        name        = input("Enter Contact Name: ")
        lastName    = input("Enter Contact Last Name: ")
        age         = input("Enter Contact Age: ")
        phone       = input("Enter Contact Phone: ")
        new_contact = Contact(name, lastName, age, phone)
        self.totalContacts.append(new_contact)
        print("\n\nContact Added Successfully")
        self.__goBackToMenu()
    
    def viewSingleContact(self):
        number = int(input("Please Enter Contact Number: "))
        i      = self.totalContacts[number-1]
        print("Name: {}\tLastName: {}\tAge: {}\tPhone: {}".format(i.name, i.lastName, i.age, i.phone))
        self.__goBackToMenu()
           
    def editContact(self):
        number   = int(input("Please Enter The Contact Number: "))        
        name     = input("Enter New Contact Name: ")
        lastName = input("Enter New Contact Last Name: ")
        age      = input("Enter New Contact Age: ")
        phone    = input("Enter New Contact Phone: ")
        if(name == ''):
            name = self.__getPreviousInfo(number).name
        if(lastName == ''):
            lastName = self.__getPreviousInfo(number).lastName
        if(age == 0 or age == ''):
            age = self.__getPreviousInfo(number).age
        if(phone == ''):
            phone = self.__getPreviousInfo(number).phone
        self.totalContacts[number-1].editContact(name, lastName, age, phone)
        print("\n\nContact Edited Successfully")
        self.__goBackToMenu()
        
    def viewAllContacts(self):
        j = 1
        for i in self.totalContacts:
            print("{}.- {}\t {}\t Age: {}\tPhone: {}".format(j, i.name, i.lastName, i.age, i.phone))
            j+=1
        self.__goBackToMenu()
        
    def deleteContact(self):
        number = int(input("Please Enter The Contact Number: "))
        self.totalContacts.remove(self.totalContacts[number-1])
        print("Contact Deleted Successfully")
        self.__goBackToMenu()
        
    def deleteEverything(self):
        self.totalContacts.clear()
        print("Contact List Deleted Sucessfully")
        self.__goBackToMenu()
    
    def __getPreviousInfo(self, number):
        previousInfo = self.totalContacts[number-1]
        return previousInfo
    
    def __goBackToMenu(self):
        input("\n\nPress Any Key To Go Back To the Menu....")
        self.start()
        

a = Contact('David', 'Acero', 26, '4481359562')
b = Contact('Alejandra', 'Lopez', 31, '12345681')
c = Contact('Godric', 'Griffindor', 28, '741 58523 9565')
usuario = MyContacts()
usuario.totalContacts.append(a)
usuario.totalContacts.append(b)
usuario.totalContacts.append(c)
usuario.start()
