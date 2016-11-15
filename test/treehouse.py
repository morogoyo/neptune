def loopy(items):
	for item in items:
		print(item)
		if item == "STOP":
			break


def loopy(items):
	for item in items:
		if item == "STOP":
		   break
		else:
			print(item)



def loopy(items):
    for item in items:
        if item[0] == "a":
            continue
        else:
            print(item)



def main():    
    show_help()

    # make a list to hold onto our items
    shopping_list = []

    while True:
     # ask for new items
        new_item = input("> ")
    
        # be able to quit the app
        if new_item == 'DONE':
             break
        elif new_item == 'HELP':
             show_help()
             continue
        elif new_item == 'SHOW':
            show_list(shopping_list)
            continue
    add_to_list(shopping_list, new_item)

    show_list(shopping_list)


test="Rene"
print("this is the number without the comma after {}".format(test))
		


def just_right(x):
    if x.len() < 5:
        return "Your string is too short" 
    elif x.len()>5:
        return "Your string is too long"
    else:
        return True


def just_right(x):
    if x.len() < 5:
    	print("Your string is too short" )
    elif x.len()>5:
        print("Your string is too long")
    else:
        return True



def squared (x):
    try:
       x = int(x)
       return x ** 2
    except ValueError:
        print( x,"is not an integer")



print(squared("time"))


import random 
def random_item(x):
     return x[random.randint(0,len(x)-1)]




import sys

test = input('234242343232Would you like to start the movie ')
print('test')

if test == "":
    print("Enjoy the show!")
else:
    sys.exit()


print("test")





def first_4(var):
    #var[1:4]
    print(var)


first_4("hello")
print("var")




