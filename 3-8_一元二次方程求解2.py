import math

while True:
    prompt = "\n请输入参数a, b, c，以空格间隔： "
    a, b, c = input(prompt).split()
    #print(a, b, c, type(a))
    if a == '0':
        print("\n参数a不可为0，请重新输入!")
    elif a.isalpha() == True or b.isalpha() == True or c.isalpha() == True:
        print("\n参数不可为非数值类型，请重新输入!")
    else:
        break

a = float(a)
b = float(b)
c = float(c)
i = (b**2 - 4 * a * c)
if i < 0:
    print(f"\ni={i}, 小于0, 无实数解!")
else:
    x1 = (-b + math.sqrt(i)) / (2 * a)
    x2 = (-b - math.sqrt(i)) / (2 * a)
    print(
        f"\n一元二次方程 {a}x^2+{b}x+{c}=0 的解: i={round(i,2)}, x1={round(x1,2)}, x2={round(x2,2)}."
    )
    
 #疑问: 标点符号怎么判断?
