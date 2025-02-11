car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)  # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

oldest, *others, youngest = car_ages_descending
print(oldest, others, youngest)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)  # 0 1 [20, 19, 15, 9, 8, 7, 6, 4]
