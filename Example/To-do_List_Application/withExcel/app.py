from TaskManager import TaskManager

# TaskManager 생성
taskManager = TaskManager()
menuNum = input("########## To-Do List App ########## \n 메뉴를 선택해주세요. \n 1. 조회 \n 2. 등록 \n 3. 변경 \n 4. 삭제 \n > ")

# Menu별 수행 내용
if menuNum is "1":
    print("김규범 님의 To-Do List")
    taskManager.viewTask()
elif menuNum is "2":
    taskName = input("Task의 이름을 입력 해 주세요: ")
    taskManager.createTask(taskName)
elif menuNum is "3":
    print("김규범 님의 To-Do List")
    index = input("변경할 Task의 번호를 입력 해 주세요: ")
    completed = input("이 일을 완료 표시 할까요? (y/n)")

    if completed is "y" or completed is "n":
        if completed is "y":
            result = taskManager.changeCompleted(index, True)
        elif completed is "n":
            result = taskManager.changeCompleted(index, False)

        if(result):
            print("변경 완료 되었습니다.")
        else:
            print("Task가 존재하지 않습니다.")
    else:
        print("y 또는 n을 입력 해 주세요")
elif menuNum is "4":
    print("김규범 님의 To-Do List")
    index = input("삭제할 Task의 번호를 입력 해 주세요: ")
    result = taskManager.deleteTask(index)
    if result:
        print("삭제 완료 되었습니다.")
    else:
        print("Task가 존재하지 않습니다.")
else:
    print("해당 메뉴는 존재하지 않습니다. 프로그램을 종료합니다.")
