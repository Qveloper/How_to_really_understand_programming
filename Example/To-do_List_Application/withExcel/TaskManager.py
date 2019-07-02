import openpyxl
from Task import Task

class TaskManager:
    def __init__(self):
        self.taskList = []
        wb = openpyxl.load_workbook('./data.xlsx')
        sheet = wb['Sheet1']

        if sheet.max_column is not 1:
            for row in sheet:
                self.taskList.append(Task(row[0].value, row[1].value))
        wb.close()
        print(self.taskList)

    def createTask(self, taskName):
        newTask = Task(taskName, False)
        self.taskList.append(newTask)

        wb = openpyxl.load_workbook('./data.xlsx')
        sheet = wb['Sheet1']

        sheet["A" + str(len(self.taskList))] = taskName
        sheet["B" + str(len(self.taskList))] = False

        wb.save("./data.xlsx")
        wb.close()

    def viewTask(self):
        index = 0
        for task in self.taskList:
            index += 1
            print("%d  %s  %s" % (index, "V" if task.isCompleted else " ", task.taskName))
    
    def changeCompleted(self, index, completed):
        taskIndex = int(index)
        if len(self.taskList) > 0 and len(self.taskList) >= taskIndex and 0 < taskIndex :
            self.taskList[taskIndex-1].isCompleted = completed

            wb = openpyxl.load_workbook('./data.xlsx')
            sheet = wb['Sheet1']
            sheet["B" + index].value = completed
            wb.save("./data.xlsx")
            wb.close()
            print("변경 완료 되었습니다.")

    def deleteTask(self, index):
        taskIndex = int(index)
        if len(self.taskList) > 0 and len(self.taskList) >= taskIndex and 0 < taskIndex :
            del self.taskList[taskIndex-1]

            wb = openpyxl.load_workbook('./data.xlsx')
            sheet = wb['Sheet1']
            sheet.delete_rows(taskIndex)
            wb.save("./data.xlsx")
            wb.close()
            print("삭제 완료 되었습니다.")
        else:
            print("목록이 없거나, 번호가 존재하지 않습니다.")