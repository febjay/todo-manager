import json
# task = {"id": 1, "text": "Купить хлеб", "done": False}

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def show_tasks(tasks):
    if not tasks:  # если список пустой
            print("Список задач пуст")
            return     
    for task in tasks:
        id = task["id"]
        text = task["text"]
        if task["done"]:
            status= "[x]"
        else:
            status= "[ ]"
        print(f"{id}. {status} {text}")

def add_task(tasks):
    text = input("Введите задачу: ")
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
    "id": new_id,
    "text": text,
    "done": False
    }
    tasks.append(new_task)
    print(f"Задача '{text}' добавлена под номером {new_id}")

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return 
    try:
        task_id = int(input("Введите номер задачи, которую нужно отметить выполненной: "))
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                print("Задача выполнена!")
                return
           
        print("Задача не найдена")
        
    except ValueError:
        print("Введите число!")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return   
    try:
        task_id = int(input("Введите номер задачи для удаления: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Задача удалена")
                return
        print("Задача не найдена")   # ← внутри try, после цикла
    except ValueError:
        print("Введите число!")

def main():
    tasks = load_tasks()  # загружаем при старте
    
    while True:
        print("\n=== TODO Менеджер ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить выполненной")
        print("4. Удалить задачу")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)      # сохраняем после изменения
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()