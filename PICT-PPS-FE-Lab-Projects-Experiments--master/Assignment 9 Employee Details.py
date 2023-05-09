'''
Write a program in Python that Create class EMPLOYEE for storing
details (Name, Designation, gender, Date of Joining and Salary).
Define function members to compute
a) total number of employees in an organization
b) count of male and female employee
c) Employee with salary more than 10,000
d) Employee with designation “Asst Manager”
'''
class EMPLOYEE:
    total=0
    m=0
    f=0
    def __init__(self,name,designation,gender,doj,salary):
        self.name=name
        self.designation=designation
        self.gender=gender
        self.doj=doj
        self.salary=salary
        EMPLOYEE.total+=1
        if gender=="m":
            EMPLOYEE.m+=1
        elif gender=="f":
            EMPLOYEE.f+=1
    def sal(self):
        if int(self.salary)>10000:
            return self.salary
    def desig(self):
        if self.designation=="Asst Manager":
            return self.name
def create():
    name=input("Enter Name:")
    designation=input("Enter Designation:")
    gender=input("Enter gender:")
    doj=input("Enter date of joining:")
    salary=int(input("Enter Salary:"))
    object_employee=EMPLOYEE(name,designation,gender,doj,salary)
    return object_employee
def main():
    list=[]
    while(1):
        c =int(input("Choose your choice:\n1.Create Employee\n2.TotalEmployees\n3.Number of male and female employees respectively\n4.Employees with salary>10000\n5.Employees whose designation is Asst Manager"))
        if c==1:
            list.append(create())
        elif c==2:
            print(EMPLOYEE.total)
        elif c==3:
            print("Males:",EMPLOYEE.m,"Females:",EMPLOYEE.f)
        elif c==4:
            for i in list:
                if i.sal():
                    print(i.name)
        elif c==5:
            for j in list:
                if j.desig():
                    print(j.name)
        else:
            print("Invalid Chioce")
            break
if __name__ == '__main__':
    main()