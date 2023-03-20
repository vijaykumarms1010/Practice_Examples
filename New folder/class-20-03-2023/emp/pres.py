from logic import add, view, spec, dept, present
from model import employee
def init():
    exit = False
    e1 = employee("sanjay",10,"banglore")
    add(1,e1)
    e2 = employee("suresh",11,"delhi")
    add(2,e2)
    e3 = employee("gagan",12,"mumbai")
    add(3,e3)
    while(exit == False):
        print("1.View all\n2.View specific\n3.By department\n4.status check\n0.Exit")
        ch = int(input("Enter choice:"))
        if ch == 1:
            message = view()
            print(message)
        elif ch == 2:
            no = int(input("Enter emp_no:"))
            message = spec(no)
            print(message)
        elif ch == 3:
            no = int(input("Enter dept_id:"))
            message = dept(no) 
            print(message)
        elif ch == 4:
            no = int(input("Enter employee no:"))
            p = present(no)
            print(p)
        elif ch == 0:
            exit = True




















# from logic import viewDetails,viewEplioyees
# from view import Employee
# def init():
#     exit=False
#     while exit==False:
#         print("1.Employee Details\n2.Get Employee on dept Id\n0.Exit")
#         ch=int(input("Enter your choice:"))
#         if ch==1:
#             EmpNo=int(input("Enter Employee Num:"))
#             if EmpNo in d:
#                 print('The emp detaiks:',d[n])
#             print(res)
#             # res=viewDetails(n)
#             # result(res)
        
#         elif ch==2:
#             deptId=int(input("Enter dept Id:"))
#             res=deptId
#             res=l1
#             # res=viewEplioyees()
#             # print(res)
#         elif ch == 0:
#             print("--- GoodBye! ---")
#             break




















# class Employee:
#     def _init_(self, employee_number, name, department_id):
#         self.employee_number = employee_number
#         self.name = name
#         self.department_id = department_id
        
#     def _str_(self):
#         return f"{self.employee_number}: {self.name}, Department {self.department_id}"

# class EmployeeManagement:
#     def _init_(self):
#         self.employee_database = []
        
#     def add_employee(self, employee_number, name, department_id):
#         self.employee_database.append(Employee(employee_number, name, department_id))
        
#     def get_employee_by_number(self, employee_number):
#         for employee in self.employee_database:
#             if employee.employee_number == employee_number:
#                 return employee
#         return None
        
#     def get_employees_by_department(self, department_id):
#         employees = []
#         for employee in self.employee_database:
#             if employee.department_id == department_id:
#                 employees.append(employee)
#         return employees











# from logic import addWord,viewAll,viewwithOccurs
# def init():
#     exit = False
#     while exit == False:
#         print("*** MENU ***")
#         print("1. view emp details based on empno.")
#         print("2. show emp details based on deptid.")
#         print("0. Exit")
#         ch = int(input("Enter your choice:"))
#         if ch == 1:

            

#         elif ch == 2:
            
#         elif ch==0:
#             break
#         # elif ch == 3:
#         #     i = int(input("Enter the occured num : "))
#         #     message = viewwithOccurs(i)
#         #     if not message:
#         #         print("No such word")
#         #     else:
#         #         print(i, "has occured", message)
        