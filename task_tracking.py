

class TaskTracking:
    def __init__(self,task_management):
        self.task_management=task_management
 
    def get_task_status(self,task_id):
        task=self.get_task_by_id(task_id)
        if task:
            print (f"{task.status}")

    def get_task_deadline(self,task_id):
        task=self.get_task_by_id(task_id)
        if task:
            print(f"{task.deadline}")
    def get_task_color(self,task_id):
        task=self.get_task_by_id(task_id)
        if task:
            print(f"{task.color}")
        
    def get_task_by_id(self,task_id):
        for task in self.task_management.task_list:
            
            
            if task.task_id==task_id:
                return task
        
        print ("ID is not found")
        return False