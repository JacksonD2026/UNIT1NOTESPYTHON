print("hello world")

lucky_num = 13 #int
my_name = "jackson" #str
cash = 5.50 #float
is_raining = True #boolean

greeting = "Hello, " + my_name
print(greeting)
# You can use single quotes instead
greeting = 'Python is cool, it\'s better than Java'
print(greeting)
long_greeting = """
                we were both young 
                when i first saw you
                i close my eyes
                """
print(long_greeting)

#f-strings are FORMATTED strings (like templates)
f_string = f"My name is {my_name} and my lucky number is {lucky_num}"
print(f_string)

# FUNCTIONS are reusable recipes/processes
# Use the keyword def to define a new function
def helloworld():
    # function BODY indente under the colon
    print("hello world I am a function")

#UN-indent to signal the end of the block
# CALL a void function
helloworld()

def multiply(x, y):
    result = x*y
    return result

five_times_three = multiply(5,3)
print(five_times_three)
print(multiply(67,41))

# *** LISTS ***
# ordered, mutable suquences
empty_list = list() # constructor 
another_empty_list = []


class_roster = ["Bryce","Finny","Jackson","Kevin","Maia","Natalie","Paige"]
print(class_roster)
print(len(class_roster))

# Indexes start at 0

first_item = class_roster[0]
print(first_item)

# Update an tem in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

# Storing lists
lottery_nums = [20, 8, 32, 24, 99, 78]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums) # sorted does not modify og list

# sort actual list
lottery_nums.sort()
print(lottery_nums)
lottery_nums.sort(reverse=True)
print(lottery_nums)

class_roster.append("Alex")
class_roster.insert(0, "Zoie")
class_roster.remove("Zoie")
class_roster.pop() # removes last item in list

print(13 in lottery_nums) 