import random

print("Random float (0.0 to 1.0):", random.random())
print("Random integer (1 to 10):", random.randint(1, 10))

my_list = [i for i in range(1, 50)]
lucky_six = random.sample(my_list, 6)

print("Lucky numbers for today:", sorted(lucky_six))

random.seed(42)
print("Seeded random value (always 0.639...):", random.random())