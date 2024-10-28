from math import ceil
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
n = 0
while (money_capital + salary - ceil((spend * (increase + 1) ** n) + 0.5)) >= 0:
    money_capital += salary - ceil((spend * (increase + 1) ** n) + 0.5)
    n += 1

print("Количество месяцев, которое можно протянуть без долгов:", n)