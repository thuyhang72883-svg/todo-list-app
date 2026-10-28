# Danh sách để lưu các công việc (mỗi công việc là một dictionary)
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành (task_index tính từ 1)."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index - 1]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách (task_index tính từ 1)."""
    if 1 <= task_index <= len(tasks):
        removed = tasks.pop(task_index - 1)
        print(f"Đã xóa công việc: '{removed['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Liệt kê tất cả các công việc hiện có kèm theo số thứ tự và trạng thái."""
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")
        
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Công việc thử xóa")

    # Đánh dấu công việc số 1 là hoàn thành
    complete_task(1)

    # Xóa công việc số 3
    delete_task(3)

    # Thử chỉ số không hợp lệ
    delete_task(10)

    # Gọi hàm hiển thị danh sách công việc
    list_tasks()