#自訂的tools module
import random,csv
def getStudents(student_nums:int=1, scores_nums:int=2) -> list[list]:
    '''
    參數: student_nums -> 學生人數\n
    參數: scores_nums -> 科目數\n
    '''
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:str = file.read()#傳回包含size行的清單, size 未指定則傳回全部行。

    nameList:list[str] = names.split('\n')#https://docs.python.org/zh-tw/3/library/stdtypes.html#str
    students:list[list] = []

    names:list[str] = random.choices(nameList,k=student_nums)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)    
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)

    return students

def saveToCSV(fileName:str,data:list[list],subject_nums:int) -> bool:
    fileName += ".csv"
    subjects = [f'科目{i+1}' for i in range(subject_nums)]
    fields = ['姓名']
    fields.extend(subjects)
    with open(fileName,mode='w',encoding='utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(data)
        except:
            return False
        else:
            return True