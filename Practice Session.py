

class Employee:

    def __init__(self):
        self.Empname = "Employee Name"
        self.EmpID = "Employee ID"

    def empDisplay(self):
        print("Name of Employee: "+self.Empname)
        print("Employee ID: "+self.EmpID)

    def empInputs(self):
        self.Empname = input("Enter the name of Employee: ")
        self.EmpID = input("Enter Employee ID: ")

        return self.Empname, self.EmpID


Emp = Employee()
(Name,ID)= Emp.empInputs()
file1 = open("C:\\Users\ss023020\Documents\Pycharm\MyProjects\InputOutputFiles\PracticeWritingReadingFile.txt","a+")
file1.truncate(0)
file1.writelines(["Name: ", Name, "\nID: ", ID])
file1.seek(0)
print(file1.read())
file1.close()
print(dir(float))


#Emp.empInputs()
#Emp.empDisplay()