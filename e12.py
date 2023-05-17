student_one = float(input("请输入第一个同学的体重："))
student_two = float(input("请输入第二个同学的体重："))
student_therr = float(input("请输入第三个同学的体重："))
student_four = float(input("请输入第四个同学的体重："))
zuida = student_one
if zuida <student_two:
    zuida=student_two
if zuida<student_therr:
    zuida=student_therr
if zuida<student_four:
    zuida=student_four

print("最大体重为:"+str(zuida))