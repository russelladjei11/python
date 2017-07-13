# A fuction to define a persons name and age
def get_age():
    age = (int)(raw_input("what is your age?"))
    return age

def get_name():
    name = (raw_input("what is your name"))
    return name

age = get_age()
name = get_name()
print "Hey, " + name + " , you are " + str(age) + "years old, dude!"

