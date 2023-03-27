from emp_model import emp
from emp_db import insertVaribleIntoTable,getDeptInfo,getEmployeeInfo


e1=emp(6,"harry",6,"mT",16)
e2=emp(7,"sam",7,"dv",17)
e3=emp(8,"messi",8,"ts",18)
e4=emp(9,"ronaldo",9,"ms",19)
e5=emp(10,"neymer",10,"governance",20)
i1=insertVaribleIntoTable(e1)
i2=insertVaribleIntoTable(e2)
i3=insertVaribleIntoTable(e3)
i4=insertVaribleIntoTable(e4)
i5=insertVaribleIntoTable(e5)
d={e1.empno:e1,e2.empno:e2,e3.empno:e3,e4.empno:e4,e5.empno:e5}
def empDetails(n):
    try:
        return d[n]
    except:
        return "No such ID"
    
def deptEmployees(n):
    l=[]
    for i in d.values():
        if i.empdeptno==n:
            l.append(i.empname)
    return l

def ispresent(n):
    if d.get(n) is not None:
        return EmployeeStatusCode(1,"got result",d[n])
    else:
        return EmployeeStatusCode(0,"no result",None)