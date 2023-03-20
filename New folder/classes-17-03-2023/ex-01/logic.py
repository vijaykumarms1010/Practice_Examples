from start import Task
d={}
def update_task(taskId,taskName,Desc,priority):
    if taskId in d:
        task= d[taskId]
        task.taskName=taskName
        task.Desc=Desc
        task.priority=priority
    else:
        print("Task Id Not Found.")

def view_task(taskId):
    if taskId in d:
        task=d[taskId]
        return (task.taskId,task.taskName,task.Desc,task.priority)
    else:
        return "Task ID Not Found"
def remove_task(taskId):
    if taskId in d:
        del d[taskId]
    else:
        print("Task Id Not Found. ")
def add_task(taskId,taskName,Desc,priority):
    if taskId not in d:
        task =Task(taskId,taskName,Desc,priority)
        d[taskId]=task
    else:
        print("Task id already exist")