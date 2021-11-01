from random import randint

l2 = [randint(0, 10) for a in range(10)]
print(l2)

x = int(input("Введіть число від 0 до 10: "))

y = l2.index(x)
print("Число" + " " + str(x) + " " + "знаходиться у списку під номером" + " " + str(y))




