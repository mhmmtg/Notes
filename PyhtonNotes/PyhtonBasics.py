x = 5  # int
y = "Hello"  # str
z = float(3)  # float
p = int(4.2)
t = "world!"
print(y + t)
print(x, y, z, t, p)

# false booleans
b1 = bool(False)
b2 = bool(None)
b3 = bool(0)
b4 = bool("")
b5 = bool(())
b6 = bool([])
b7 = bool({})

a = b = c = "7"
print(a, b, c)

a, b, c = 3, 5, 7
print(a, b, c)

# This is a comment
"""
This is a multiline comment!
"""

# string
my_string = "{} beautiful {}"
my_string2 = "{} \"beautiful\" {}"
print(my_string.format(y, t))
print(my_string2.format(y, t))

my_str = "Mohammad"
print(my_str[0])
print("m" in my_str)
print("n" not in my_str)
print(len(my_str))
print(my_str[2:6])
print(my_str[3:])
my_str.upper()
my_str.lower()
my_str.split("m")
my_str.strip()

for s in my_str:
    print(s)

for i in range(5):
    print(i)

i = 0
while i < len(my_str):
    print(my_str[i], sep="-")
    i += 1

# functions
m = 5


def sum_of_two():
    global m
    print(m)


sum_of_two()


# global - scope
def outer_fun():
    global a
    a = 20

    def inner_fun():
        global a
        a = 30
        print('a =', a)

    inner_fun()
    print('a =', a)


a = 10
outer_fun()
print('a =', a)


def my_fun():
    print(my_var)


my_var = 34
my_fun()


def print_name(name="John"):
    print(name)


print_name()
print_name("Jane")

# lists
my_list2 = list(("apple", "banana", "peach"))
print(my_list2[-3:-1])

my_list = ["apple", "orange"]
my_list[0] = "plum"
my_list.insert(1, "apricot")

my_list.extend(my_list2)

# if
a = 5
b = 3
if a > b:
    print("bigger")
elif a < b:
    print("smaller")
else:
    print("equal")
