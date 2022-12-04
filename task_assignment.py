def task_assignment(k, tasks):
    # Write your code here.
	sorted_tasks = sorted(tasks)
	final_tasks = []
	for i in range(len(tasks)//2):
		task_pair = [tasks.index(sorted_tasks[i]), tasks.index(sorted_tasks[len(tasks) - i -1])]
		finalTasks.append(task_pair)
    return final_tasks

def get_index(dict_index: dict[int, list], value:int):
    dict_index.
