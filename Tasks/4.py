# 1 Подсчитать сумму цифр в вещественном числе.

n = input("Введите вещественное число n: ")

n = n.replace(".", "")
n = n.replace(",", "")

result = 0

for i in n:
   
    result += int(i)

print(f'сумма цифр в указанном числе: {result}')