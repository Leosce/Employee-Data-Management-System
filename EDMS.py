import re
import csv
class Employee:

    #list for every field in the database.
    emp_list=[]
    ID_list=[]
    pos_list=['CEO','CFO','COO','MM','HR','SWE','DS','ML']
    sal_list=[]
    mail_list=[]
    emp_pos_list=[]
    fields=['ID','Name','Position','Salary','Email']

    
    def __init__(self,ID,Name,Position,Salary,Email):
             
        ID=Employee.ID_handle(self,ID)   #make sure the ID entered is numeric and isn't already taken. if not, a different ID replaces the original.
        self.__ID=ID
    
        Name=Employee.name_handle(self,Name) #make sure the Name entered is valid. if not, a different Name replaces the original.
        self.Name=Name
            
        Position=Employee.position_handle(self,Position) #make sure the Position entered is in the position list. if not, a different Position replaces the original.
        self.Position=Position
        
        Salary=Employee.salary_handle(self,Salary) #make sure the Salary entered is a numeric value. if not, a different Salary replaces the original.
        self.__Salary=Salary

        Email=Employee.email_handle(self,Email) #make sure the Email entered is valid and not already registered on the system. if not, a different Email replaces the original.
        self.__Email=Email

        #append the lists with user input for later access.
        Employee.ID_list.append(self.__ID)
        Employee.emp_list.append(self.Name)
        Employee.emp_pos_list.append(self.Position)
        Employee.sal_list.append(self.__Salary)
        Employee.mail_list.append(self.__Email)
        EmployeeManager.save_to_csv()
        Employee.menu(self)

# Exception Handling:
    def ID_handle(self,id):
        while True:
            try:
                id=int(id)
                if id in Employee.ID_list:
                    print('ID already exists.')
                    id=input('Please enter a valid ID: ')
                else:
                    return id
            except ValueError:
                print('ID is invalid. ')
                id=input('Please enter a valid ID: ')
    
    
    def name_handle(self,name):
        while True:
                try:
                    # name=input("Please enter a valid name: ")
                    int(name)
                    name=input("Please enter a valid name: ")
                except(ValueError):
                    return name

    def position_handle(self,position):
        while True:
            try:
                position=position.upper()
                if(position not in Employee.pos_list):
                    print("This position doesn't exist.")
                    position=input("Please enter a valid position: ")
                else:
                    return position
            except AttributeError:
                print('Please enter string format input.')
                position=input("Please enter a valid position: ")

    def email_handle(self,email):
        while True:
            try:
                pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if re.match(pattern, email) is not None and email not in Employee.mail_list:
                    return email
                else:
                    if email in Employee.mail_list:
                        print('Email already exists.')
                        email= input('Please enter a valid email: ')
                        continue
                    print('Email is not valid, try again.')
                    email= input('Please enter a valid email: ')
            except TypeError:
                print('Please enter string format input.')
                email= input('Please enter a valid email: ')

    def salary_handle(self,salary):
        while True:
                try:
                    if(type(salary)==str and salary[-1].upper()=='K'):
                        return salary
                    salary=int(salary)
                    if salary<1000:
                        salary=f'{salary}K'
                    return salary
                except(ValueError):
                    print("Please enter standard numeric values or numeric values ending with 'k' only.")
                    salary=input('Please enter a valid salary: ')


#class methods:
    
    def get_ID(self):
        return self.__ID
        
    def get_Salary(self):
        return self.__Salary
    
    def get_Email(self):
        return self.__Email

    def update_email(self):
        i=Employee.ID_list.index(self.__ID)
        new_email=input('Enter a valid email: ')
        Employee.mail_list[i]=(Employee.email_handle(self,new_email))
        print('Email has been updated.')
        EmployeeManager.save_to_csv()
        
    #def display_public_info(self):
    #display by list not self.
    #    return self.Name,self.Position
    
    def display_all_info(self):
        i=Employee.ID_list.index(self.__ID)
        print( f"ID: {Employee.ID_list[i]} \nName: {Employee.emp_list[i]} \nEmail: {Employee.mail_list[i]}\nPosition: {Employee.emp_pos_list[i]} \nSalary: {Employee.sal_list[i]} \n")
    

    def menu(self):
        while True:
            try:
                print('\nWhat would you like to do?')
                print('1-Display my information.\n2-Update my email.\n3-Exit. \n')
                choice=int(input('Please enter a number corresponding to your choice: \n'))
            except ValueError:
                print('Please enter a valid number.')
    
            if choice==1:
                Employee.display_all_info(self)
                
            if choice==2:
                Employee.update_email(self)
    
            if choice==3:
                break


class EmployeeManager(Employee):
    @classmethod
    def __init__(self):
        EmployeeManager.menu(self) #call the menu method
        
#class methods:
    @classmethod
    def ID_checker(self,ID): #ID checker, checks if ID is valid or if it already exists and prompts the user for input if it needed.
        while True:
            try:
                ID=int(ID)
                if(ID in Employee.ID_list):
                    self.ID=self.get_ID
                    self.ID=ID
                    self.i=Employee.ID_list.index(self.ID) 
                    break
                else:
                    ID=int(input("this employee ID doesn't exist, Please enter an existing employee ID: "))
                    
            except(ValueError):
                
                print('This ID is invalid, Please try agian.')
                ID=input('Please enter a valid ID:  ')
    
    @classmethod
    def add_emp(self,id,name,pos,sal,mail):   # add an employee.
        Employee(id,name,pos,sal,mail)
        print('Employee added successfully, saving...') #user confirmation.
        EmployeeManager.save_to_csv() #save changes to csv.
        
    @classmethod
    def del_emp(self,ID):   # delete an employee, by giving the employee's ID
            #remove employee from the lists.
            EmployeeManager.ID_checker(ID) 
            Employee.emp_list.pop(self.i)
            Employee.ID_list.pop(self.i)
            Employee.mail_list.pop(self.i)
            Employee.sal_list.pop(self.i)
            Employee.emp_pos_list.pop(self.i)
            print('Employee deleted successfully, saving...') #user confirmation.
            EmployeeManager.save_to_csv() #save changes to csv.
 
            
    @classmethod 
    def list_all_emps(self):   # list all employees.
        print(Employee.emp_list)
        print(Employee.ID_list)
        print(Employee.sal_list)
        print(Employee.mail_list)
        print(Employee.emp_pos_list)
        
    @classmethod
    def search_emp(self,ID):   # search for information relation to an employee, given their ID.
        EmployeeManager.ID_checker(ID)
        print(f'Name: {Employee.emp_list[self.i]}') 
        print(f'ID: {Employee.ID_list[self.i]}')
        print(f'Salary: {Employee.sal_list[self.i]}')
        print(f'Email: {Employee.mail_list[self.i]}')
        print(f'Position: {Employee.emp_pos_list[self.i]}')
    
    @classmethod
    def update_emp(self,ID):   # update employees infromation.
        EmployeeManager.ID_checker(ID)
        upd=input("Please enter type the required fields to update. seperated by a comma or a space.")
        
        if 'ID' in upd.upper():
            while True:
               try:
                   new_id=int(input("Please enter the new ID: "))
                   if new_id in Employee.ID_list and new_id!=Employee.ID_list[self.i]:
                       print("ID already exists, try again.")
                   else:
                       Employee.ID_list[self.i]=new_id
                       print('ID updated successfully.')
                       break
               except(ValueError):
                   print('Invalid input, try again.')
                   
        if 'SALARY' in upd.upper():
            new_salary=input('Enter a valid salary: ')
            new_salary=Employee.salary_handle(self,new_salary)
            Employee.sal_list[self.i]=new_salary
            print('Salary updated successfully.')

        if 'NAME' in upd.upper():
            new_name=input('Enter a valid name: ')
            new_name=Employee.name_handle(self,new_name)
            Employee.emp_list[self.i]=new_name
            print('Name updated successfully.')
                    

        if 'POSITION' in upd.upper():
            new_position=input('Enter a valid position: ')
            new_position=Employee.position_handle(self,new_position)
            Employee.emp_pos_list[self.i]=new_position
            print("Position updated successfully.")
            

        if 'EMAIL' in upd.upper():
            new_email=input('Enter a valid email: ')
            new_email=Employee.email_handle(self,new_email)
            Employee.mail_list[self.i]=new_email
            print("Email updated successfully.")
        
        EmployeeManager.save_to_csv()

    @classmethod
    def save_to_csv(self):   # save changes to csv.
        with open('employee_data.csv','w',newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(Employee.fields)
            
        for i in range(len(Employee.ID_list)):
            employee_list=[Employee.ID_list[i],Employee.emp_list[i],Employee.emp_pos_list[i],Employee.sal_list[i],Employee.mail_list[i]]
            with open('employee_data.csv','a',newline='') as csvfile:
                csvwriter=csv.writer(csvfile)
                csvwriter.writerow(employee_list)
        print('csv saved successfully.')

    @classmethod
    def load_from_csv(self):   # retrieve data from csv
        Employee.ID_list=[]
        Employee.emp_list=[]
        Employee.emp_pos_list=[]
        Employee.sal_list=[]
        Employee.mail_list=[]
        try:
            with open('employee_data.csv',newline='') as csvfile:
                csvreader=csv.reader(csvfile)
                next(csvreader)
                for row in csvreader:
                    Employee.ID_list.append(int(row[0]))
                    Employee.emp_list.append(row[1])
                    Employee.emp_pos_list.append(row[2])
                    Employee.sal_list.append(row[3])
                    Employee.mail_list.append(row[4])
                if len(Employee.ID_list) !=0:
                    print('Data loaded successfully.')
                else:
                    print('csv file is empty.')
                    
        except FileNotFoundError:
            print('csv file move or not found.')
    
    def menu(self):   # menu for user interface.
        while True:
            try:
                print('\nWhat would you like to do?\n1-Add an employee.\n2-Delete an employee.\n3-List all employees.\n4-Search for an employee.\n5-Update an employee.\n6-Save data to csv file.\n7-Load from csv file.\n8-Exist.\n')
                choice=int(input('Please enter a number corresponding to your choice: \n'))
            except ValueError:
                print('Please enter a valid number.')
                
            if choice==1:
                print('Please enter ID, Name, Position, Salary and Email for the employee.')
                while True:
                    try:
                        ID=int(input('ID: '))
                        break
                    except ValueError:
                        print('ID is invalid, please enter a valid ID. ')
                Name=input('Name: ')
                Position=input('Position: ')
                Salary=input('Salary: ')
                Email=input('Email: ')
                EmployeeManager.add_emp(ID,Name,Position,Salary,Email)
                
            if choice==2:
                ID=input('Please enter the ID of the employee you would like to delete: ')
                EmployeeManager.del_emp(ID)
                
            if choice==3:
               EmployeeManager.list_all_emps()

            if choice==4:
                ID=input('Please enter the ID of the employee you would like to search for: ')
                EmployeeManager.search_emp(ID)

            if choice==5:
                ID=input('In order to update employees information, please enter an existing ID: ')
                EmployeeManager.update_emp(ID)

            if choice==6:
                print('Saving...\n')
                EmployeeManager.save_to_csv()
                
            if choice==7:
                print('Loading...\n')
                EmployeeManager.load_from_csv()

            if choice==8:
                break