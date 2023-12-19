import random
import pyinputplus as pyip


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

def saveToCSV(fileName:str,data:list[list]) -> None:
    fileName += ".csv"
    print("檔案名稱",fileName)
    print(f"資料:{data}")


if __name__ == '__main__':#判斷是不是正在執行主要檔
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    o_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = getStudents(student_nums=s_nums,scores_nums=o_nums)
#append說明書https://www.runoob.com/python/att-list-append.html
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱):")
    saveToCSV(fileName=fileName,data=students)