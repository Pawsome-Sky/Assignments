print("Tuple Operations")
day_temperatures = (22.6, 19.1, 21.3)
print(len(day_temperatures))
print(" ")

print("Making a Shopping List")
shopping_list = ["milk", "eggs", "bread", "butter"]
print(shopping_list)
print(shopping_list[0])
bread_index = shopping_list.index("bread")
print(bread_index)
shopping_list[bread_index] = "banana"
shopping_list.insert(0,"apple")
print(shopping_list)
new_items = ("flour", "sugar")
shopping_list.extend(new_items)
print(shopping_list)
eggs_index = shopping_list.index("eggs")
print(eggs_index)
banana_index = shopping_list.index("banana")
print(banana_index)
print(shopping_list[2:4])
print(" ")

print("Half triangle")
number = int(input("Enter the triangle size: "))
for i in range(number):
    for j in range(i + 1):
        print(j + 1,end =" ")
    print()
print(" ")

print("Prime Numbers within a Range")
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
prime_numbers = []
for number in range(start, end +1):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            prime_numbers.append(number)
print(f"Prime numbers: {prime_numbers}")
print(" ")