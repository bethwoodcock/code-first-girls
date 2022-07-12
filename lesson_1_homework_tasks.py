###Question 1
#I am building some very high quality chairs and need exactly four nails for each chair. I've written a
#program to calculate how many nails I need to buy to build these chairs.
chairs = '15'
nails = 4
total_nails = chairs * nails
nailsmessage = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(nailsmessage))

#When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
#my program calculating the total number of nails correctly? What is the problem? How do I fix it?

##ANSWER
# chairs does not have to be in quotations.
chairs = 15
nails = 4
total_nails = chairs * nails
newnailsmessage = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(newnailsmessage))

###Question 2
#I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix
#the program?
my_name = Penelope
my_age = 29
agemessage = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(agemessage)

##ANSWER
#Change my_name = Penelope into my_name = "Penelope".

my_name = "Penelope"
my_age = 29
namemessage = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(namemessage)

###Question 3
#I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
#make. Write a program to calculate this.
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
#able to easily change these values if I want. The output should say something like "You can make 9
#omelettes with 6 boxes of eggs".

eggs = 30
eggs_in_box = eggs / 6
omelette = eggs / 4
message = 'You can make {} omelettes with {} boxes of eggs'.format(omelette, eggs_in_box)
print(message)