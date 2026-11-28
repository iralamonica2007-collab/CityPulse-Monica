# LIST
fruits = ["mango", "apple", "banana"]
fruits.append("orange")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits[0:2])


# SLICING (list)
nums = [10, 20, 30, 40, 50]
print(nums[0:3])
print(nums[2:])
print(nums[:2])
print(nums[-2:])
print(nums[::2])
print(nums[::-1])


# TUPLE
colors = ("red", "green", "blue")
print(colors)
print(colors[1])
print(colors[0:2])


# SLICING (string)
word = "Python"
print(word[0:3])
print(word[::-1])


# SET
numbers = {1, 2, 2, 3, 3}
print(numbers)

numbers.add(4)
print(numbers)


# DICTIONARY
student = {"name": "Monica", "age": 19}
print(student)
print(student["name"])

student["city"] = "Bengaluru"
print(student)


# DICTIONARY INSIDE DICTIONARY
students = {
    "s1": {"name": "Monica", "marks": 92},
    "s2": {"name": "Riya", "marks": 85}
}
print(students["s1"])
print(students["s1"]["name"])
print(students["s2"]["marks"])
