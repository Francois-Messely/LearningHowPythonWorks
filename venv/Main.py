#name = input("what is your name?: ")
#age = int(input("what is your age?: "))
#height = float(input("How tall are you?: "))

#age = age + 1
#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("you are " +str(height)+" cm")

#import math

#pi = 3.14

#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.ceil(math.sqrt(pi)))
#print(max (x,y,z))
#print(min(x,y,z))


#



#name = "Bro bob"

#first_name = name[:3]

#last_name = name[4:]
#funky_name = name [::4]
#reversed_name = name[::-1]
#print(reversed_name)
#print(funky_name)
#print(first_name)
#print(last_name)

#website ="https://google.com"
#website2 ="https://you.com"

#slice = slice(8,-4,1)

#print(website[slice])
#print(website2[slice])

#age = int(input("How old are you?: "))

#if age >=18:
#    print("You are an adult!")
#elif age < 0:
#    print("WHAT?!")
#else:
 #   int(input("Try Again"))
#return

#temp = int(input("WWhat is the temperature outside?"))

#if not(temp >= 0 and temp <=30):
#    print("okok")
#elif not(temp < 0 or temp >30):
#    print("the temperature is nice")


#name = None

#while not name:
    #name = input("enter your name: ")

#print("hello" + name)


#for i in range(10):
 #   print(i+1)

#for i in range(50,100+1,2):
#     print(i)

#for i in "bro code":
#    print(i)

###looooooooooop

#import time


#for i in range(10,0,-0.2)):
   # print(i)
   # time.sleep(1)
#print("fuck you!")

##inner loop = loop inside a loop


#rows = int(input("how many rows?; "))
#columns = int(input("how many columns?: "))
#symbol = input("enter a symbol to use:" )

#for i in range (rows):
#    for j in range(columns):
 #       print(symbol, end="")
#    print()

#while True:
 #   name = input("Enter your name: ")
 #   if name != "":
   #     break

#phone_number = "123-123-1235"
#for i in phone_number:
 #   if i == "-":
  #      continue
 #   print(i, end="")


#for i in range(1,21):

   # if i ==13:
   #     pass
  #  else:
  #      print(i, end="")

#food = ["pizza","hamburger","hotdog",""]
#food.append("ice cream")
#food.remove("pizza")
#food.pop()
#food.insert(0,"cake")
#print(food[0])
#food.sort()
#food.clear()



#for x in food:
 #   print(x)

#drinks = ["Coffee","soda","tea"]
#dinner = ["pizza", "hamburger", "sushi"]
#dessert = ["cake","icecream"]
#food = [drinks,dinner,dessert]

#print(food)
#print(food[4][3])

#student = ("Bro",21,"male")
#print(student.count("Bro"))
#print(student.index("Bro"))

#for x in student:
   #  print(x)

#if "Bro" in student:
  #  print("testtest#  ")

#utensils = ["knife","fork",]

#for utensils in utensils:
#    print("%s" % utensils)

#add = input("please enter a utensils")
#if add not in utensils:
#    utensils.append(add)
#else: print("already in list!")

#for x in utensils:
#    print(x)

#capitals = {"USA":"Washington DC",
            #"India:":"New Dehli",
            # "china":"beijing",
           # "russia":"Moscow"}
#print(capitals["russia"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#capitals.update({"germany":"berlin"})
#capitals.update({"USA":"Bob"})
#capitals.pop("china")
#capitals.clear()

#for key,value in capitals.items():
 #   print(key,value)

#name = "bro bro"

#if(name[0].islower()):
   #name = name.capitalize()

#first_name = name[:3].upper()
#last_name =name[4:].capitalize()
#print(first_name)
#print(last_name)

#add = input("What is your name?: ")
   # name.append(add)

#def hello(name):
   # print("Hello "+name)
  #  print("You are cute")

#hello("bro")#
## testing

## just learned how to push to github :D


#9-03-2022 - Having fun again

#food=["pizza","cookie","sushi","hamburger","oreo","your mom"]

#food.append("ice cream")
#food.remove("hamburger")
#food.sort()
#food.pop()
#food.insert(0,"cake")
#food.reverse()
#for x in food:
#    print(x)
#first_name = "Francois"
#last_name = "Messely"
#full_name = first_name +" "+last_name
#age = 28

#def hello(full_name,age):
 #   print("Hello "+full_name)
 #   print("Ton Prénom est: "+first_name)
 #   print("Ton nom de famille est: "+last_name)
 #   print("Tu as: "+str(age)+" ans")

#hello(full_name,age)

#

#return statement

#def multiply(number1,number2):
#        return number1 * number2

#x = multiply (6,8)

#print(x)


# #####Keywords arguments########

#first = "Francois"
#middle = "messely"
#last = "le grand"

#def hello(first,middle,last):
  #  print("Hello "+first+" "+middle+" "+last)

#hello(last=last,middle=middle,first=first)

# positional arguments
#def hello(first,midle,last):
   # print("Hello "+first+" "+midle+" "+last)

#hello("Francois","messely","le grand")

