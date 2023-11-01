student={}
student["sid"] = input("請輸入您的學號：")
student["sname"] = input("請輸入您的姓名：")
student["fchina"] = float(input("請輸入您的國文成績："))
student["fmath"] = float(input("請輸入您的數學成績："))
student["finfo"] = float(input("請輸入您的電腦成績："))
total = student["fchina"]+student["fmath"]+student["finfo"]
round(total,2)
avg = round(total / 3,2)
print("-"*30)
print("{}({})同學您好：\n以下是您各科成績與分數評定\n\n國文：{:<5}/ 數學：{:<5}/ 電腦：{:<5}\n總分：{:<6}/ 平均：{:<6}".format(student["sname"],student["sid"],student["fchina"],student["fmath"],student["finfo"],total,avg))
print("-"*30)
if avg>60 :
    grade = "合格"
elif avg<60 :
    grade = "不及格"
print("成績判定：{}\n".format(grade))