d1={}

def present(id):
    if id in d1.keys():
        print()
        return "Present, value = ",d1[id]
    else:
        return "Not present\n"
def addTask(x):
    if x.id in d1:
        return "This id already present", 1
    else:
        d1[x.id]={x.taskname,x.description,x.priority}
        return d1

def updateTask(x):
    if x.id not in d1: 
        return "This id is not present",1
    else:
        d1[x.id]={x.taskname,x.description,x.priority}
        return d1
def viewTask(id):
    return d1[id]

def removeTask(id):
    return "Removed",d1.pop(id)























# from classe import Task

# tasks_dict = {}

# def update_task(taskid):
#     if taskid in tasks_dict:
#         task = tasks_dict[taskid]
#         task.taskname = input("Enter task name: ")
#         task.description = input("Enter task description: ")
#         task.priority = input("Enter task priority: ")
#     else:
#         print("Task ID not found.")

# def view_task(taskid):
#     if taskid in tasks_dict:
#         task = tasks_dict[taskid]
#         print("Task ID: ", task.taskid)
#         print("Task Name: ", task.taskname)
#         print("Task Description: ", task.description)
#         print("Task Priority: ", task.priority)
#     else:
#         print("Task ID not found.")

# def remove_task(taskid):
#     if taskid in tasks_dict:
#         del tasks_dict[taskid]
#     else:
#         print("Task ID not found.")

# def add_task(taskid, taskname, description, priority):
#     if taskid not in tasks_dict:
#         task = Task(taskid, taskname, description, priority)
#         tasks_dict[taskid] = task
#     else:
#         print("Task ID already exists.")





















































# from classe import Task
# task_dict={}

# def update_task(taskid):
#     if taskid in task_dict:
#         x=task_dict[taskid]
#         x.taskname=input("Enter Task Name:")
#         x.description=input('Enter task description:')
#         x.priority=input("Enter task priority:")
#     else:
#         print("TaskId Not Found")
# def 



# employees = {}
# def addWord(name): 
#     if name in employees.keys():
#         employees[name] = employees[name]+1
#         return"Name already present, Count added"
#     else:
#         employees[name] = 1 
#         return "Name Added"
# def viewWord(): 
#     return employees.keys()
# def allWord():
#     return employees
# def occurWord(inte):
#     d1=[]
#     for emp in employees:
#         if employees[emp]>=inte:
#            d1.append(emp)
#            return d1