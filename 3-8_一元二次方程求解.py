import math

d = ()
while len(d) != 3:
    prompt = "\n请输入参数a, b, c，以空格间隔： "
    d = input(prompt).split()
    #print(d, type(d))
    for s in d:
        if d[0] == '0' or s.isalpha() == True:
            print("\n参数须为数值，a不可为0，请重新输入!")
            d.clear()

a = float(d[0])
b = float(d[1])
c = float(d[2])
i = (b**2 - 4 * a * c)
if i < 0:
    print(f"\ni={i}, 小于0, 无实数解!")
else:
    x1 = (-b + math.sqrt(i)) / (2 * a)
    x2 = (-b - math.sqrt(i)) / (2 * a)
    print(
        f"\n一元二次方程 {a}x^2+{b}x+{c}=0 的解: i={round(i,2)}, x1={round(x1,2)}, x2={round(x2,2)}."
    )