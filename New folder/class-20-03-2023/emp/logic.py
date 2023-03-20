from model import employeeStatus
dict1 = {}
def add(emp_no,info):
    dict1[emp_no] = info
    return dict1
    
def view():
    return dict1
def spec(emp_no):
    return dict1[emp_no]
def dept(no):
    a = []
    for i in dict1.values():
        if i.dept_id == no:
            a.append(i.name)
            return a
def present(p):
    if dict1.get(p) is not None:
        return employeeStatus(1,"got result",dict1[p])
    else:
        return employeeStatus(0,"no result",None)












# from model import EmployeesStatus
# di={}
# def createDict(emp_No,info):
#     dect1[emp_No]=info
#     return di
# def viewDict():
#     return di
# def viewDetails(emp_No):
#     return di[emp_No]

# def deptId(n):
#     x=[]
#     for i in di.values():
#         if i.dept_Id==no:
#             x.append(i.name)
#         return x
# def dept(no):
#     a = []
#     for i in dict1.values():
#         if i.dept_id == no:
#             a.append(i.name)
#             return a
# def present(p):
#     if dict1.get(p) is not None:
#         return employeeStatus(1,"got result",dict1[p])
#     else:
#         return employeeStatus(0,"no result",None)




















# from model import Employee,EmployeesStatusModel
# emp1=Empl(1,'sanjay',11)
# emp2=Empl(2,'sanjay',12)
# emp3=Empl(3,'manoj',13)
# emp4=Empl(4,'akshay',14)
# emp5=Empl(5,'salman',15)
# # 2-models
# d={emp1.empno:emp1,emp2.empno:emp2,emp3.empno:emp3,emp4.empno:emp4,emp5.empno:emp5}


# def viewDetails(n):
#     # dict[empNo]=Info
#     # return dict
#     try:
#         return d[n]
#     except:
#         return "No such ID"
# def viewEplioyees(n):
#     l1=[]
#     for i in d.values():
#         if i.department_id==n:
#             l1.append(i.name)
#         return l1














# from plogic import EmployeeManagement

# def main():l
#     employee_management = EmployeeManagement()
#     employee_management.add_employee(1, "John Smith", 1)
#     employee_management.add_employee(2, "Jane Doe", 2)
#     employee_management.add_employee(3, "Bob Johnson", 1)
    
#     while True:
#         print("Enter 1 to get employee details by number")
#         print("Enter 2 to get employees by department")
#         print("Enter 3 to exit")
#         choice = input("Choice: ")
        
#         if choice == "1":
#             employee_number = int(input("Enter employee number: "))
#             employee = employee_management.get_employee_by_number(employee_number)
#             if employee:
#                 print(employee)
#             else:
#                 print("Employee not found.")
                
#         elif choice == "2":
#             department_id = int(input("Enter department ID: "))
#             employees = employee_management.get_employees_by_department(department_id)
#             if employees:
#                 for employee in employees:
#                     print(employee)
#             else:
#                 print("No employees found in department.")
                
#         elif choice == "3":
#             break
            
#         else:
#             print("Invalid choice. Try again.")
            
# if _name_ == "_main_":
#     main()












    
# dict = {'1':{'1.1':'emp1','1.2':'emp2'},
#         '2':{'2.1':'emp2.1','2.2':'emp2.2'},
#         '3':{'3.1':'emp3.1','3.2':'emp3.2'},
#         '4':{'4.1':'emp4.1','4.2':'emp4.2'},
#         '5':{'5.1':'emp5.1','5.2':'emp5.2'},}

# def viewdetails(key):
#     if key not in dict:
#         dict[key] = 1
#     else:
#         dict[key] += 1
#         return "key present"

# def viewAll():
#         return dict
    
# def viewwithOccurs():
#     return dict.items()