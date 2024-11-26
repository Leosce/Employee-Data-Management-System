# Employee-Data-Management-System
The Employee Data Management System is a Python-based application designed to manage employee data for a company or organization efficiently. The system allows users to perform essential operations like:
Adding a new employee.
Viewing all employees.
Updating an employee's details.
Deleting an employee.
Searching for an employee by their unique ID.
Saving and retrieving employee data using a CSV file.
This project showcases the use of core Python concepts, Object-Oriented Programming (OOP) principles, and file handling to build a functional and scalable application.

-------------------------------------------------

Employee class:
in the employee class, each employee enter their information. after entering they have 2 options: display the information they entered and update their email. any more updates can not be done by the employee,
has to be done by the employee manager.

employees can not enter string values in ID field, they also can not enter an ID that already exists.

employees can not enter int values in Name field.

employees can't enter string values, unless they end with 'k' for short to thousand. meaning they can input 49k instead of 49000. also works as error handling if the employee enters a value that is less than 1000
if the value is greater than 1000, the code registers it as int value salary. further error handling is done by the manager by updating employee's salary, in case salary is not correct. 

employees can not enter any value that is not in the position list, the list makes up for the positions that currently exist in the company.

employees can not enter invalid emails.

employees can display their information to check the info they entered, if changes are required it can be done by the manager. unless they want to update their email

employees can update their email, as it wouldn't negatively affect the system, but employee can not update their salary as it can result in unethical input, the employee can not update their ID as it might already exist or it might be reserved for specific positions, the employee can not update their position as it is controled by the manager, the employee can not update their name as they might impersonate other employees or managers, thus gaining access to manager class and ruin the system. same can happen if the employee can update their own ID. which is why the manager controls the updating process.

EmployeeManager class:
in the employee manager the manager controls employees' data. manager can add, delete, update, list and search for employees information. additionally, manager can save to and from csv file.

manager can add an employee by entering a new hire's info, that is then treated as an object of the Employee class and goes through the error handling that is in the Employee class.

manager can delete an employee by entering an existing employee ID. if the employee exists, the employee is deleted from the lists provided in the code and the csv file. if the employee doesn't exist, the program prompts the user to enter a different ID 

manager can update an employee's info by entering their ID, then typing out the fields that are required for update. if the prompt is empty or it doesn't include any of the program's fields, the program doesn't update, and it saves the employees' info.

manager can list all of the employees currently saved into the program's lists.

manager can search for a specific employee's info to be displayed in a more friendly way, showing each field with their respective value.

manager can choose to save to csv, even though every new change done to the program's list, the csv gets updated automatically.

manager can choose to load from csv, allowing the manager to use an already existing csv to work with or continuing from where the employee list left off. in case the manager wants to continue from where was once left off, the manager needs to load the dataset as the first step, otherwise the program will save the newly added information in the same csv and rewrite the old data. THIS IS AN INTENDED FEATURE.
