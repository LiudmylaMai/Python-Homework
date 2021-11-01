ticket = int(100)

print("Скільки коштів ви маєте")
a = int(input())
b = a-ticket
c = ticket-a

if a==ticket:
    print("Вам вистачає на один квиток :-)")
elif a>50 and a<ticket:
    print("Нажаль, вам не вистачає на квиток"), print(c)
else:
    print("Вітаємо, ви ще й отримаєте здачу!"), print(b)











