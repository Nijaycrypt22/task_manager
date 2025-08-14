import add
import show
import update
import delete

add_task_response= add.add_task("sleep")
print(add_task_response)

show_task_response= show.show_task()
print(show_task_response)

update_task_response= update.update_task("sleep", "wake up")
print(update_task_response)
delete_task_response = delete.delete_task("wake up")
print(delete_task_response)