class employee:
    def __init__(self,name,dept_id,address):
        self.name = name
        self.dept_id = dept_id
        self.address = address
    def __repr__(self):
        return f"name:{self.name},dept_id:{self.dept_id},address:{self.address}"
class employeeStatus():
    def __init__(self,statuscode,message,empobj):
        self.statuscode = statuscode
        self.message = message
        self.empobj = empobj
    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"

























        
# class Employee:
#     def __init__(self,EmpName,DeptId,addRess):
#         self.EmpName=EmpName
#         self.DeptId=DeptId
#         self.addRess=addRess
#     def __str__(self):
#         return f'EmpName:{self.EmpName},DeptId:{self.DeptId},addRess:{self.addRess}'

# class EmployeesStatus:
#     def __init__(self,statuscode,message,employeeObj):
#         self.statuscode=statuscode
#         self.message=message
#         self.employeeObj
#     def __str__(self):
#         return f'{self.statuscode},{self.message},{self.employeeObj}'







































# class Empl:
#     def __init__(self,EmpNo,EmpName,DeptId):
#         self.EmpNo=EmpNo
#         self.EmpnName=EmpName
#         self.DeptId=DeptId
#     def __str__(self):
#         return ({self.EmpNo},{self.EmpnName},{self.DeptId})
# class EmployeesStatusModel:
#     def __init__(self,statuscode,message,employeeObj):
#         self.__annotations__

# x=Empl(EmpNo, EmpName, DeptId)
# y=EmployeesStatusModel(0, 'message', x)