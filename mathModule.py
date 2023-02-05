import math

#Ex1
degree = 360
    #Rad for 360 deg

rad = degree * math.pi /180
print(math.radians(degree))

degree = 45
print(math.radians(degree))

#Ex2
small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

PI = math.pi

print(small_pizza_price/(PI * small_pizza_r**2))
print(big_pizza_price/(PI * big_pizza_r**2))
print(family_pizza_price/(PI * family_pizza_r**2))

math_ls = dir(math)
print(math_ls)