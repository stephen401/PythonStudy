import math

d = []
n = 0
while len(d) != 3:  #输入3个数字
    n += 1
    prompt = f"\n请输入第{n}个参数： "
    m = input(prompt)
    d.append(m)
    #print(d, len(d), type(m))
    while True:  #如果输入非数字，则重新输入
        if d[0] == '0':
            print("\n第一个参数不能为0，请重新输入！")
            d.clear()
            n = 0
            break
        elif m.isalpha() == True:
            print("\n参数不能为字符，请重新输入！")
            d.clear()
            n = 0
            break
        break

a = float(d[0])
b = float(d[1])
c = float(d[2])
i = round((b**2 - 4 * a * c), 2)
if i < 0:
    print(f"i={i}, 小于0, 无实数解!")
else:
    x1 = (-b + math.sqrt(i)) / (2 * a)
    x2 = (-b - math.sqrt(i)) / (2 * a)
    print(
        f"\n一元二次方程 {a}x^2+{b}x+{c}=0 的解: i={i}, x1={round(x1,2)}, x2={round(x2,2)}."
    )

#疑问: 标点符号如何判断?
