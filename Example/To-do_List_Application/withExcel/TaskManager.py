import openpyxl

# TaskList의 요소 Class
class Task:
    # Task Class 생성자
    def __init__(self, taskName, isCompleted):
        self.taskName = taskName # task 이름
        self.isCompleted = isCompleted # task 완료 유무

    # Task 완료 유무를 변경하는 Method
    def setCompleted(self, isCompleted):
        self.isCompleted = isCompleted 

# Task를 관리하기 위한 Class
class TaskManager:
    # TaskManager Class 생성자
    def __init__(self):
        self.taskList = [] # Task의 목록을 내부적으로 저장
        self.workbook = openpyxl.load_workbook('./data.xlsx') # excel파일 load
        self.sheet = self.workbook['Sheet1'] # Sheet1 load

        if self.sheet.max_column is not 1: # 빈 파일 검사
            for row in self.sheet:
                self.taskList.append(Task(row[0].value, row[1].value))

        self.workbook.close() # 파일 리소스 정리

    # Task 생성 Method
    def createTask(self, taskName):
        newTask = Task(taskName, False)
        self.taskList.append(newTask) # 내부 목록에 Task 추가

        # Excel에 행 추가
        self.sheet["A" + str(len(self.taskList))] = taskName
        self.sheet["B" + str(len(self.taskList))] = False

        # 저장 후 파일 리소스 정리
        self.workbook.save("./data.xlsx")
        self.workbook.close()

    # Task 조회 Method
    def viewTask(self):
        index = 1
        for task in self.taskList:
            print("%d  %s  %s" % (index, "V" if task.isCompleted else " ", task.taskName))
            index += 1
    
    # Task 변경 Method
    def changeCompleted(self, index, completed):
        taskIndex = int(index)

        # 존재하지 않는 Task를 선택하지 못하도록 조건 검사
        if len(self.taskList) > 0 and len(self.taskList) >= taskIndex and 0 < taskIndex :
            # 내부 목록의 Task 상태 변경
            self.taskList[taskIndex-1].setCompleted = completed

            # Excel의 값 변경
            self.sheet["B" + index].value = completed
            self.workbook.save("./data.xlsx")
            self.workbook.close()
            return True
            
        return False

    # Task 삭제 Method
    def deleteTask(self, index):
        taskIndex = int(index)

        # 존재하지 않는 Task를 선택하지 못하도록 조건 검사
        if len(self.taskList) > 0 and len(self.taskList) >= taskIndex and 0 < taskIndex :
            # 내부 목록의 Task 삭제
            del self.taskList[taskIndex-1]

            # Excel의 행 삭제
            self.sheet.delete_rows(taskIndex)
            self.workbook.save("./data.xlsx")
            self.workbook.close()
            return True
            
        return False