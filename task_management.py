class TaskManagement:
    def __init__(self):
        self.task_list=[]
    
    def add_task(self, task):
        self.task_list.append(task)
    
    def list_tasks(self):
        if not self.task_list:
            print('Henuz Listenecek Gorev Yok!')
            return
        for task in self.task_list:
            print(f"[{task.task_id}] {task.task_name}  -  {task.task_status}  -  {task.task_priority}   -  {task.task_deadline}  -   {task.task_color}")
    
    def find_task_by_id(self, task_id):
        for task in self.task_list:
            if task.task_id==task_id:
                return task
        print('Gorev bulunamadi...')
        return None
        