# Программа считает сколько в кассе денег
# Проверяет верно ли количество
# Учитывает возвраты, оплату мобильным банком и расходы

print("CashCount - Программа для подсчета наличных денег в кассе")

count_5000 = int(input("How much 5000 RUB? "))
count_2000 = int(input("How much 2000 RUB? "))
count_1000 = int(input("How much 1000 RUB? "))
count_500 = int(input("How much 500 RUB? "))
count_200 = int(input("How much 200 RUB? "))
count_100 = int(input("How much 100 RUB? "))
count_50 = int(input("How much 50 RUB? "))
count_10 = int(input("How much 10 RUB? "))
count_5 = int(input("How much 5 RUB? "))
count_2 = int(input("How much 2 RUB? "))
count_1 = int(input("How much 1 RUB? "))

rubles_in_5000 = count_5000 * 5000
rubles_in_2000 = count_2000 * 2000
rubles_in_1000 = count_1000 * 1000
rubles_in_500 = count_500 * 500
rubles_in_200 = count_200 * 200
rubles_in_100 = count_100 * 100
rubles_in_50 = count_50 * 50
rubles_in_10 = count_10 * 10
rubles_in_5 = count_5 * 5
rubles_in_2 = count_2 * 2
rubles_in_1 = count_1 * 1

total_cash = rubles_in_5000 + rubles_in_2000 + rubles_in_1000 + rubles_in_500 + rubles_in_200 + rubles_in_100 + rubles_in_50 + rubles_in_10 + rubles_in_5 + rubles_in_2 + rubles_in_1

print(f"Total cash is {total_cash} RUB")
