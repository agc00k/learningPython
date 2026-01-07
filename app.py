"""Module providing first python code block"""
print("Hello World!")
print("*" * 10)
students_count = 1000
print(students_count)
print("*" * 10)
first = "Andres"
last = "Cook"
full = f"{first} {last}"
print(full)
print("*" * 10)
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
print("*" * 10)


def greet(name):
    print(f"Hi {name}")


greet("Andres")
# End-of-file (EOF)
