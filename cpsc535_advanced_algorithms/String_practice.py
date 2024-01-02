# message = 'Hello world'
# print(message)
# // WORKING ON STRINGS//
# print(len(message))#prints the length of the message
# print(message[0])# prints the 0th character in the message
# print(message[5])#Space, prints the 5th character in the message
# print(message[10])# prints the 10th character in the message
# #slicing of strings
# print(message[0:5])# prints the message from 0th character upto 5th character excluding 5th character
# print(message[0:])#prints the message from 0th character upto last character, becoz no end limit is provided
# print(message[6:11 ])
# # a method is just a function that belongs to an object
# print(message.lower())# converts the mesaage to lower case
# print(message.upper())# converts the mesaage to upper case

# print(message.count('Hello'))# tells the count/occurence of character in the message 

# print(message.count('l'))
# print(message.find('Hello'))# finds the index of the first character
# print(message.find('world'))# finds the index of the first character
# print(message.find('r'))# finds the index of the first character
# print(message.find('Hide'))# finds the index of the first character if its not inthe message returns -1
# #for replacing the string 
# new_message = message.replace('world', 'Universe')
# print(new_message)
# #concatenation of strings
# greetings = 'hello'
# name = "divya"
# message_1 = greetings + ', ' + name +'. Welcome!'
# #or curly brackets are place holders
# message_2 = '{}, {}. Welcome!'.format(greetings,name)
# #or
# message_3 = f'{greetings}, {name.upper()}. Welcome!'
# print(message_1)
# print(message_2)
# print(message_3)
# #dir function shows all the attributes and methods for that variable
# print(dir(name))
# #print(help(help))
# #print(help(str))

# //WORKING ON INTEGERS AND FLOATS//

# num = 3
# print(num)
# print(type(num))#Tells the type of the variable/num
# #arithmatic operators
# print(3+2)
# print(3-2)
# print(3*2)
# print(3/2)
# print(3//2)
# print(3**2)
# print(3%2)
# print(4 %2)
# print(3*2+1)
# print(3*(2+1))

# num = 1
# num = num+1
# #or
# #num += 1
# print(num)
# #print the absolute value
# print(abs(-3))
# #print the round off number and the second argument in bracket is upto how many digit you want to round of
# print(round(3.75))
# print(round(3.757,2))
# # comparison operators
# num1 = 3
# num2 = 2
# print(num1 == num2)
# print(num1 != num2)
# print(num1 > num2)
# print(num1 < num2)
# print(num1 >= num2)
# print(num1 <= num2)

# num_1 = '100'
# num_2 = '200'
# # so for adding two numbers we have cast the as
# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2)

# //working with lists(mutable), tuples(immutable) and sets//

# courses = ['History', 'Physics', 'Maths', 'CompSci']
# courses_1 = ['Drawing','Painting']
# print(courses)
# print(len(courses))#this will tell the length of the list
# print(courses[0])# this square tells the index of items inside list
# print(courses[3])
# print(courses[-1]) #this -1 give the last item inside the list helpful in large lengths
# print(courses[0:2])
# print(courses[:3])
# print(courses[2:])

#add an item to the end of list
#courses.append('Art')
#print(courses)
#TO INSERT art on a certain position inside list insert method is used and it takes two arguments first is the position of where the user wants to place the item and second is the value itself.
#courses.insert(0 , 'Art')
#or
#courses.insert(2,'Art')
#courses.insert(0, courses_1)
#print by adding the items of courses_1 to courses list
#courses.extend(courses_1)
#print(courses)
#remove method is used o remove an item from the list
#courses.remove('Maths')
#print(courses)

#pop method is ised to remove the last element of the list and its is used when the user want to use the list like a stack or a queue

#courses.pop()
#print(courses)

#if the user want to see popped value

#popped = courses.pop()
#print(popped)
#print(courses)

#reverse a list
#courses.reverse()
#print(courses)

#sort a list
#nums = [1,5,2,4,3]
# courses.sort(reverse = True)# this reverse argument will provide the list in descending order by default it prints in ascending order
# nums.sort(reverse = True)

# print(courses)
# print(nums)

# if we don't want to make changes in the original list and sort the list then store it in another function

#sorted_courses = sorted(courses)# now the original list is safe and unsorted
#print(sorted_courses)

#print min,max and sum of the list of items
# print(min(nums))
# print(max(nums))
# print(sum(nums))

#find the index of a certain item in list
#print(courses.index('CompSci'))

#to check the item in the list 
# print('Art' in courses)
# print('Maths' in courses)

# for item in courses:
#     print(item)# each time a new line by default

# for course in courses:
#     print(course)

#enumerate to know the index of item and it returns two things the index and value

# for index, course in enumerate(courses, start =1): #this start value will change the starting value of the list
#     print(index,course)

# for index, course in enumerate(courses, start =10):
#     print(index,course)

# # change the strings in the list to comma separted values
# course_str = ', '.join(courses)
# print(course_str)

# course_str = ' - '.join(courses)
# print(course_str)

# doing reverse of this and turn string back into a list, this can be done by splitting the string on a certai value like here in this case by hyphen

# course_str = ' - '.join(courses)
# new_list = course_str.split(' - ')
# print(course_str)
# print(new_list)


# //Working with tuples(immutable)//
#lists are mutable example
# list_1 = ['Sci', 'Maths','CompSci','Physics']
# list_2 = list_1
# print(list_1)
# print(list_2)

#changing the value of 0th item in the list
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)#the value changed in both the list becuse it is mutable

#Tuples are immutable example

# tuple_1 =('Sci', 'Maths','CompSci','Physics')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# BUT if the user want to do change the first index  value as above it is not allowed
#tuple_1[0] ='Art'# it is not allowed the assignment operator

# //working with sets//
#sets are values that are unordered and also have no duplicates

# cs_courses = {'Sci', 'Maths','CompSci','Physics'}
# art_courses = {'Sci', 'Maths','CompSci','datastructures','chemistry'}

#print(cs_courses)# order of printing the set
#changes on each execution the reason for this is because unlike lists and tuples sets really don't care about order because some 
#of them uses for a set is either to test whether a value is part of a set and also it's used a lot to remove duplicate values 
# because sets throw away duplicate values you can se it has two maths entry but print only once.
#Second point was it is used to test whether a value is part of a set now this is called a membership test
#so sets do this a lot more efficiently than lists and tuples
#print('Maths' in cs_courses)#this is a membership test 

#Intersection between two sets
#print(cs_courses.intersection(art_courses))

#differece between the sets
#print(cs_courses.difference(art_courses))# here the courses which are not in art_courses are displayed

#union of the both the sets
#print(cs_courses.union(art_courses))

#Empty lists
# empty_list = []
# empty_list = list()
#Empty tuples
# empty_tuple = ()
# empty_tuple = tuple()
#Empty dictionary
#empty_dict = {}
#Empty sets
#empty_set = set()

# //Working with dictionaries//
#dictionaries allow us to work with key value pairs(or hash maps and associative arrays)are two linked 
#values where the key is a unique identifier where we can find our data and value is that data. so it 
#almost like a real physical dictionary where the user lookup for definitions. each word the user looked
#up would be the key and the definition of that value would be the value.

# student = {'name':'john','age':25,'courses':['math','CompSci']}
# print(student) 
# print(student['name'])
# print(student['courses'])
# if the user wants to access akey that doesn't exist and wants to shows a message none then use get method
# print(student.get('name'))# in this case key is there so it displays the value
# print(student.get('phone'))# here the key is not in the dictionary so it displays none instead of showing a ke error
# or if a user wants to display a special message then pass the msg as a second argument
#print(student.get('phone', 'not found'))
# how to add a new key to the dictionary, the user have to do like as:
#student['phone'] = '555-5555'
#print(student.get('phone', 'not found'))
#update a key's value
#student['name'] = 'jane'
#print(student)# now it displays the dictionary with the updated values
#or it can be done by update method
#student.update({'name':'marcus','age':26,'phone':'555-5555'})
#print(student)

#to delete a key
# del student['age']
# print(student)
#another way to do it by pop method(will remove and also return the value)
# age = student.pop('age')
# print(student)
# print(age)

#length of the dictionary
#print(len(student))
#if user want to see the keys in dictionary
#print(student.keys())
#if user want to see the values in dictionary
#print(student.values())
#if user want to see the keys and values in dictionary
#print(student.items())
# if we loop through our list without using any method then it'll just loop through the keys 
#for key in student:
#    print(key)

#for looping through the keys and values use items
#for key, value in student.items():
 #   print(key, value)

# // working with conditional and booleans //
#in Python there is no switch case because the if and elif statements are pretty clear than switch case
# language = 'Python'

# if language == 'Python':
#     print('language is python')
# elif language  == 'java': 
#     print('language is java')
# elif language == 'javascript':
#     print('langauge is javascript')
# else:
#     print('No match')

# // working with boolean operators//
# user = 'Admin'
# logged_in = True

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('bad credentials')

# # //working with OR
# user = 'Admin'
# logged_in = False

# if user == 'Admin' or logged_in:
#     print('Admin Page')# it prints admin page because for it doesn't matter whether the second ststement is true or not

# else:
#     print('bad credentials')

# #Working with not
# if not logged_in:
#     print('Please Log in')# it prints admin page because for it doesn't matter whether the second ststement is true or not

# else:
#     print('Welcome')

# a = [1,2,3,4]
# b = [1,2,3,4]

# print(a == b)

# print(id(a))
# print(id(b))
# print(a is b)#it is false because these are two different objects in memory and we can print out these 
#locations with this built-in ID function, so this comparison really checking whether these IDs are same so

#if instead of creating a new list if i just say b = a

# a = [2,3,4]
# b=a

# print(a == b)

# print(id(a))
# print(id(b))
# print(a is b) # now for this case it is printing  they are same by checking their ID are also same.
#now because they are same objects in memory.

#false values:
# condition = False

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

# condition = None

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

#// for zero to any numeric type//working with numbers we have to keep in mind that you don't want to accidently pass
#zero that you think evaluates to true but it evaluates false
# condition = 0

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

# condition = 10

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

#// empty list, tuple, dictionary, string all returns false

# condition = []

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

# condition = ''

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')
# condition = 'Test'

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')


# condition = {}# this is empty mapping ie dictionry it also returns false

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')

# condition = ()

# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')


#// working with loops and iterations
#nums =[1,2,3,4,5,6]

# for num in nums:
#     print(num)# here we are looping thriugh each value of our list and each time through the loop this num
    #variable will be equal to the next item in the list so the first time through it will be equal to 1 and
    #the next time through ite will be 2 and so on. 

# break keyword will completely breakout of a loop and the 
# for num in nums:
#     if num == 3:
#         print('found!')
#         break
#     print(num)
#continue keyword move on to the next iteration of the loop
# for num in nums:
#     if num == 3:
#         print('found!')
#         continue
#     print(num)

# nested loops
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for i in range(10): #it will print the values starting from 0 to 9
#     #or we can do this like this if we want to define the starting value for i in range(1,11) because it will print upto 10 not 11
#     print(i)

#// while loop will just keeep goin into until a certain condition is met or until we hit a break
# x = 0
# # while x < 10:
# #     print(x)
# #     x += 1

#     #or 
# while x < 10:
#     if x==5:
#         break
#     print(x)
#     x += 1

#  #or 
# while True:
#     if x==5:
#         break
#     print(x)
#     x += 1

#  #or 
# while True:
#     print(x) # this is a infinite loop
#     x += 1


#// Working with Functions// 
# def hello_func():
#     pass
#here def means definition and we made simple function hello func, now we have parenthesis here because 
#where our parameters will go but we don't have any just yet so that it will be empty for now. now it is 
#possible to write a function and not have any code in it but we can't leave it completely blank but if 
#we want to fill this function later then the user can use this pass keyword. basically this pass keyword 
#is saying that we don't want to do anything now but it won't throw any errors for leaving it blank.
#if we want to rin our function and we can just say hello_func(). here we need to add those parenthesis in order to
# execute it if we don't have these parenthesis there then it'll be equal to the function itself.

#print(hello_func)# so when we print it shows that it is a function and its location in the memory. and it means that we are not executing the function.

#print(hello_func())# now we are executing the function it will return none because we don't have anything in it and didn't provided any rturn value yet

#so now if we provide any statement inside the function then we don't need the print statement to execute the function

# def helloyes_func():
#     print('Hello function!')

# helloyes_func()
# //major use of function is that they allow us to reuse code without repeating themselves//

# def hello_func():
#     return 'Hello function.'

# hello_func()# it don't give us any results because its just a string that we're not doing anything with

# print(hello_func())# now this prints outs our string Hello function.
# print(len('testing')) # this function gives us the length/number of the characters in string

# print(hello_func().upper()) # this executed function return all characters of the string in upper case

#// now we can see how to pass arguments in the string//

# def hello_func(greeting):
#     return '{} Function.'.format(greeting)
# print(hello_func('Hi'))# we can see tha when we ran that it says hello func is missing one required positional
#argument greeting(Hi) when we pass Hi it prints Hi function. we can see that when we pass this greeting argument high
#into our function that is set that greeting variable equal to the string high then returned the string high function
# now this greeting varible doesn't affect any variable outside the function its scope is only local to the
#function.

# now this grreting parameter is a required argument and that is because it doen't have a default value 
# now if we have a default value then it would just fall back to the default value whenever we didn't 
# pass that argument

# def hello_func(greeting, name = 'you'):
#     return '{}, {}'.format(greeting, name)
# #print(hello_func('Hi'))
# print(hello_func('Hi', name ='divya'))# if we want he value to the parameter

# the required positional arguments comes before the keyword arguments

# def student_info(*args, **kwargs):
#    print(args)
#    print(kwargs)

# student_info('Math','Art', name = 'john', age  = 22)# now from the output we can see that the argumnets 
# #are printed in tuple form amd the keyword arguments are printed in the format of dictionary

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math', 'Art']# changed the tuple into list
# info = {'name' : 'john', 'age'  : 22}

# #student_info(courses,info)# the output is not as expected instead of passing the values as individually and instead passed 
# #in the complete list and coomplete dictionary as positional arguments

# student_info(*courses,**info)# if we use single star in front of the list and double star in front of the 
#dictionary then it would unpack these values and pass them as individually basically equivalent to 
# the previous execution where we pass them as individually


#// code till this learning

# number of days per month. First value place hoder for indexing purposes.
# month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# def is_leap(year):
#     """Returns True for leap years, false for non-leap years."""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)

# def days_in_month(year, month):
#     """ Returns the number of days in that month in that year"""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print(is_leap(2017))
# print(is_leap(2020))

# print(days_in_month(2017, 2))#since 2017 is not a leap year it will just the number in days in that month here 2 means feb -28




#// OS module- use underlying Operating System Functionality: navigate the file system, get file 
# information, lookup and change the environment variables, move files around 
# import os
# from datetime import datetime
# this will show all the attributes and methods the user have access to within this module
##print(dir(os))

# this will show theb current directory that the user is in
#print(os.getcwd()) 
# to navigate to the new path so just copy the path as string inexample video:
#os.chdir('/Users/divyadhara/Documents/')
#print(os.getcwd()) 

# to print file and folders here are on desktop us listdir method for list directory:
#print(os.listdir())

# create a new folder in the directory:
#os.mkdir('Algo_535-1')this will create a new folder in the directory.
#print(os.listdir())
# os.makedirs('Algo_535-1/Sub-Dir-1')# in this if we want to create a directory that a few level deep then makedirs 
#will create the all the intermediate directories that the user need to make
#print(os.listdir())

#for removing the folders there are rmdir() and removedirs()


#os.removedirs('Algo_535-1/Sub-Dir-1')# this will remove the intermediate directories.
#os.rmdir('Algo_535-1')# this will not remove the intermediate directories
#print(os.listdir())

# rename a file or folder
#os.rename('Questions Set 1_GSU.pdf', 'Questions Set_1_GSU.pdf')
#print(os.listdir())

# to check the information about the file 'Questions Set 1_GSU.pdf'
#print(os.stat('Questions Set 1_GSU.pdf'))# it shows many attributes of the file like 
#size it's in bytes and modification time or st_mtime(its is form of time stamp but that is not in a human readable form)

#// to convert st_mtime in human  readable format import datetime 
# mod_time = os.stat('Questions Set 1_GSU.pdf').st_mtime
# print(datetime.fromtimestamp(mod_time))# mod_time is just a variable

#if the user want to see the entire directory tree and files within the desktop traverse 
# all the drectory tree and print all the directoryies and the files

# is a generator that yield s atuple of three values as is walking the directory
#tree for each directory that it sees it yields the directory path that directs within 
# the path and the files within that path.

# for dirpath, dirnames, filenames in os.walk('/Users/divyadhara/Documents/'):
#     print('Current Path:', dirpath)
#     print('Directories:',dirnames)
#     print('Files:',filenames )
#     print()


#access the home directory location by grabbing the home environment variable, for Home it shows None and HOME it provides the path
#print(os.environ.get('HOME'))

## to create a new file in home directory: the users first have to figure out what the path should be, for this os.path method is used
# file_path = os.environ.get('HOME') + 'test.txt'
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# to grab the file name of any path that we are working on and this doesn't have to be real path
#print(os.path.basename('/tmp/test.txt')) # this gives the base name of the entire path is test.txt

# now if the usr only want the directory name of the path instead of base name then just change the basename with dirname
#print(os.path.dirname('/tmp/test.txt'))# this gives the tmp directory that the user prvided

#now if the usr want the directory name of the path and base name both then os.path.split method is used
#print(os.path.split('/tmp/test.txt'))# this the o/p for this ('/tmp', 'test.txt')

# to check the existence of the path use os.path.exists
#print(os.path.exists('/tmp/test.txt')) #PROVIDES FALSE as it doesn't exists 

# if want to check the directory or a file then use os.path.isdir if it exists it returns true and same is for checking file os.path.isfile
# print(os.path.isdir('/tmp/test.txt'))
# print(os.path.isfile('/tmp/test.txt'))

# for splitting the root name and extension of a path and can be used for file manipulation
#print(os.path.splitext('/tmp/test.txt'))

#prints the methods that are available in the os path module
#print(dir(os.path))

#// file objects- Reading and writing to files//
# to open a file from the same directory:
# f = open('practice.py', 'r')# r specifies for reading and is default for writing('w')/ appending('a')reading and writing both then ('r+')
# print(f.name)
# #explicitly close the when done using it. it is necessary to close it because otherwise
# it cause leaks that cause you run over the maximum allowed file descriptors on your 
# systems and your application could throw an error. so it is always important to make 
# sure that you close the files that you open
# f.close()
# #check the mode of the file reading/writing/appending/ reading&writing
# print(f.mode)
#to open a file from the different directory pass the path o the open method:


# how to open file from the context manager it is done using 'with' keyword. this allow 
# us to work with files from within this block and after we exit that block of code it'll
# automatically close the file for us. so we don't have to worry about whether or not we
# add in these closes. this will also close the file if there are any exceptions that are
# thrown. here in this actually we have the access for this f variable
#with open('practice.py','r') as f:
#     pass
# print(f.close())# IT WILL RETURN TRUE and on read peration it will show error, for 
#working on a closed file. so if user want to do any operations on he has to do inside that block(context manager) only

#/ to read from a file create a f_contents variable to read the file
#with open('practice.py','r') as f:
    # f_contents = f.read()
    # print(f_contents) # it will show all the contents of the file   
    # f_contents = f.readlines()
    # print(f_contents)# it gives a list of all of thelines in the file

    # f_contents = f.readline()
    # print(f_contents)# it gives a line of the file and on each run it gives the next line of the file

    # f_contents = f.readline()
    # print(f_contents)
    #it will show a new line at the both lines, as we are printing it two it will provide
    #the first and second line as the result and if we add another argument as end = ''(empty string) then it will remove the extra space between the lines.

# to read large files without going out of memory run a for loop/iterate for each line in the file

# with open ('practice.py','r') as f:
#     for line in f:
#         print(line, end = '')# this will print all the contents in the file, this is 
        #eficient because is not reading in all of the contents from our file all at once
        #so it will not create the memory issue. it will go through and get one line at a time from the file 

# to get more control over the file and want to read the desired content
#with open ('practice.py','r') as f:
# since we don't know how long the file will be so we are going to use some kind of loop
# that just iterate over the small chunks at a time, so instead of hard coding in 100. i will create a variable size_to_read 
    
#     size_to_read = 10# this will grab the first 10 characters of our file
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#     # 10 is the first 10 characters if we print this one more time it will print the next 100 charcters
#         print(f_contents, end = '*')
# # now when we hit the end of the file then read will just return an empty string so we run a 
# while loop and say the length of F contents is greater than 0 then we will print out 
# the contents that we got out from the read. don't run at this step because it will be 
# an infinite loop 
        #f_contents = f.read(size_to_read)# this will kick us out to the while loop and 
        #it will check if we've hit the end of the file because f.read will return an empty string and it will not meet this conditional

 

 #//working with variable scope// LEGB: local, enclosing, global, built-in
# local: in which are variables defined within a function 
# enclosing: our variables in the local scope of enclosing functions
# global: are variables defined at the top level of a module or explicitly declared global using the global keyword
# built-in: are just names that are pre-assigned in python.

# x='global x'# x is global variable here because it is in the main boody of our file.

# def test():
#     y= 'local y'# y is a local variable
#     #print(y) #it returns local y because it checks for local variable first and it does sodirectly print that
#     print(x)# it will return global x because its is a global variable

# test()
# #print(y) # name 'y' is not defined
#  # but if we print y here it shows an error because y is a local variable and we want to print y out of its scope.
# print(x)
#if we print x here it prints x because x is a global variable and x is a global variable so it can be print anywhere in file.
 
# if we want to explicitly tell python that we want to change the value of global x variable.
# x= 'global x'
# def test():
#     global x # this tells python that vhange the value of global varible to local written in next line.
#     x = 'local x'
#     print(x)

# test()
# print(x)
# it is showing the value of x is local now both print statements and its is showing 
# the same output eventhough if comment the first line(x= 'global x') but if we comment 
# this(global x) then it will show error for the second print statement because at that 
# time x is out of scope

# now from here if the user want to pass the arguments in test  then local z wil when test function is called
# x = 'global x'

# def test(z):
#     x = 'local x'
#     print(z)

# test('local z')
# print(z)# this will show error because it is out of scope now that z is not defined

#/bulit-in function/
#if we would like to view the varibles that are within the built-in scope then we can simply say import builtins and then just print(dir(builtin)) on this builtin module 
# import builtins
# print(dir(builtins))# dir just gets a list of the attributes of a given 
# one more thing that we have to careful with as far as built-ins go is accidently 
# overriding them so this isn't something that python prevents us from doing now there's 
# reasons for this, but basically the're just trusting us with having the power to do 
# that so for example, if i was to create a min function here  
# def my_min():
#     pass # WE DIDN'T GET ANY ERRORS if we comment the below two lines for but  if we don't it gives us an error
# m= min([5,1,4,2,3])# passing an iterable as values, here min is the built-in function in python that provides min value in the interval
# print(m)
# # because python that min function in the global scope before it fell back to the builtin scope. but if change the function nme then its ok
# def test(z):
#     x  = 'local x'
#     print(z)

# // enclosing// so when we got a point within our inner function where we printed out 
# this x, it first checked if it had any x varibles local to that inner function and it
# doesn't because we commented it, so then it checks if it has an x variable and the 
# local scope of any enclosing functions so that's why it is called enclosing scope now 
# we looking in the local scope of any enclosing functions so our enclosure closing 
# function here is the outer function and we do have an x variable in the local scope of 
# that enclosing function so that's why it printed out outer x 

from re import S


x = 'global x'# now if i uncomment it and the last print statement i gives the o/p as :
#inner x
# outer x
# global x
#def outer():
#     x = 'outer x'
     
#     def inner():
#         #nonlocal x # to provide a value of the outer function explicitely to python now it will give the inner x both the print statements.
#         x = 'inner x'#if we comment this the will be outer x both times and this is what the enclosing scope is
#         print(x)
    
#     inner()
#     print(x)

# outer()
# print(x)
# # we run outer function outer() it then points to the def outer() here we set the value
# of our local x varible(which is local to the outer function) now come down and run the
# inner()  now it will point to the inner function now set the value of x which is local
# to the inner function so firstly it prints the inner x(according to the rule it checks
# it has a local variable and it does so it prints that) then it comes to print(x) and 
# it check does it have any local variable and it does that's outer one so print that 
# outer x in the second place.  


# // working with sorting lists, tuples and objects//
# li = [9,1,8,2,7,3,6,4,5]
# s_li = sorted(li)# this sorted function returns a new sorted list so that's we set it to a variable
# s_li = sorted(li, reverse = True)# this sorts the list in descending order
# print('Sorted Varible:\t', s_li)# this sorts in ascending order

# #li.sort()# but this sort method just sorts the list in place and then returns none
# li.sort(reverse=True)# this sorts the list in descending order
# print('original Varible:\t', li)

# why would i want to choose sorted function over the sort method?
# sort method on the list is fine if working with list and if you want to modify it in 
# place but sorted function gives us a little bit flexibility because we can pass in any
# iterable as opposed to the sort method which works specifically on list. 

#// working with tuples//
# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)# tuple doesn't have a sort method, so we have to use sort function to do sorting
# print('Tuple \t', s_tup)# prints a list of sorted integers from our tuple


# #// working with dictionary//
# di = {'name': 'Corey', 'job':'programming', 'age': None, 'os':'Mac'}
# s_di = sorted(di)
# print('Dict\t', s_di)# it returns with sorted the values based on keys
# the user can use either any method: like use sorted function or the sort method as long as difference is clear 


# li = [-6,-5,-4,3,2,1] 
# s_li = sorted(li, key = abs)# here this key parameter and it is equal to abs which will 
# #use the absolute value function now to runs each element through this absolute value function before it makes the comparision.
# #so key parameters is useful when you are sorting objects with named attributes 
# print(s_li )

# # here we ghave a class employee
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __repr__(self):# this tells python how we want this function represented when it's printed out on the screen
#         return '({},{},{})'.format(self.name,self.age,self.salary)
# from operator import attrgetter# afte importing this no needto write lambda e: e.name instead write key = attrgetter('age')
# #3 sample employees with random names ages and salary
# e1 = Employee('carl', 37, 70000)
# e2 = Employee('sarah', 29, 80000)
# e3 = Employee('john', 43, 90000)

# employees = [e1,e2,e3]# put all three into a list called employees
# now try to sort these based on specific attributes and we can't sort them without a key otherwise it shows an error
# writing a custom function to sort these, remember our key takes a function that takes each element of our list and returns what we want to sort

# def e_sort(emp):
#     return emp.age
#s_employees = sorted(employees, key = e_sort)
#or
# s_employees = sorted(employees, key = lambda e: e.name)# in this lambda function case no need to write def e_sort(emp): and  return emp.age
# # or 
# s_employees = sorted(employees, key = attrgetter('age') )
# print(s_employees)




#Python OOPs classes and instances
#method is a function that is associated with class 
#Difference between a class and an instance of a class.  so a class is basically a blue 
#print for creating instances and each unique employee that we create using our employee 
# class will be an instance of that class
# class Employee:
# #this is a initialize method/constructor(in other languages) below are the instances of 
# # our employee method
#     def __init__(self, first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
        
# #  so now we can directly pass the names and pay we can leave of self here
# emp_1 = Employee('Divya','tanwar', 50000)# so when we create this employee the init method 
# #will be run automatically so,emp_1 will be passed in a self and then it will set all of these
# #attributes. so it'll set emp_1.first is equla to first which we passed in as query.
# emp_2 = Employee('test','user', 70000)
# # each of these are going to be own unique instances of the employee class
# print(emp_1)
# print(emp_2)# so we can see both of them have different locations in the memory
# # difference between class variable and instance variable : instance variable contains 
# # data that is unique to each instance
# #//creating manually instance variable:
# # emp_1.first = 'Divya'
# # emp_2.last = 'tanwar'
# # emp_1.email = 'divya.tanwar@company.com' 
# # emp_1.pay = 50000

# # emp_2.first = 'test'
# # emp_2.last = 'user'
# # emp_2.email = 'test.user@company.com' 
# # emp_2.pay = 70000

# print(emp_1.email)#we can setup this automatically when we create the employee we're 
# #going to create init method. so now inside our employee class i'm going to create this 
# # special init method
# print(emp_2.email)

# print(emp_2.fullname())

# #running from a class name so for it we do have to pass an instance for this. an dif 
# #print this out we get the same o/p as the above line
# print(Employee.fullname(emp_1))


#Tutorial 2 class variables:
#class variables are the variables that are shared among all instances of a class. 
# so instance varibles can be unique for each instance the class varibales can be 
# class Employee:
#     raise_amount = 1.04
#     num_of_emps = 0
#     def __init__(self, first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email  = first +'.' + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#         #or self.pay = int(self.pay * Employee.raise_amount)
# print(Employee.num_of_emps)# o/p is zero , here we instantiated those employees then you can see that it was zero and we created two employees and then it printed out 2

# emp_1 = Employee('Divya','schafer', 50000)
# emp_2 = Employee('test','user', 70000)

# # print(Employee.__dict__)
# # #o/p {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x7f85d2a32b90>, 'fullname': <function Employee.fullname at 0x7f85d2a32d40>, 'apply_raise': <function Employee.apply_raise at 0x7f85d2a32dd0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

# # print(emp_1.__dict__)
# # #o/p {'first': 'Divya', 'last': 'schafer', 'pay': 50000, 'email': 'Divya.schafer@company.com'}
# # Employee.raise_amount = 1.06
# #o/p this will change the raise amount for the class and all the instances:1.06
# # 1.06
# # 1.06
# # but on the other hand if we change it to  instance(emp_1) instead of class(Employee)
# # emp_1.raise_amount =1.05 #: it will just change the raise amount for the  emp_1(1.05) only rest have the same value as 1.04 
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)

# print(Employee.num_of_emps)# o/p 2 employees

#// class methods and static methods
# regular methods in class automatically take the instance as the first argument and by
# convention we were calling this self. so if a regular method automatically takes in 
# the instance as the first argument then how can we change this so that it istead 
# automatically takes the class as the first argument. so for this we use class methods
# and to turn a regular method into class method add a decorator at the top called class method

# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@gmail.com'

#         Employee.num_of_emps += 1
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     # so from now we receive the class as our first argument instead of instance
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

#     @classmethod
#     def from_string(cls,emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)


# emp_1 = Employee('divya', 'tanwar', 50000)
# emp_2 = Employee('test','Employee', 70000)

# Employee.set_raise_amt(1.05)# after this statement all the three print statements below 
# # return 1.05 becuse we ran this set amt method which is class method which means that 
# # now we are working with the class instead of instance, 
# #emp_1.set_raise_amt(1.05) we can also change the class method from instance like this
# print(Employee.raise_amt)# class.raise amount
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)# instance.raise amount
# # we get the o/p for these three same becuse of the declared class varible 4 percent

# # class methods as alternative constructors that means you can use these class methods 
# # in order to provide multiple ways of creating our objects so lets say that: for example
# # someone is using our employee class and they said i have these specific use cases 
# # where i'm getting employee information in the form of a string that is separated by 
# # hyphens and i'm constantly needing to parse the string before i create new employees 
# # so is there a way to just pass in a string and create a employee from that.

# emp_str_1 = 'john-doe-70000'
# emp_str_2 = 'steve-smith-30000'
# emp_str_3 = 'jane-doe-90000'




# #new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

#video 5 special(magic/dunder) method

class Employee:
    raise_amt =1.04
    def __init__(self,first,last,pay):# this special dunder(means double underscore)init
# method is mplicitly called when we create our employee objects here and it comes in
# and sets all of our attributes for us.
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# two special methods to implement are __repr__ and __str__ and these are what 
# implicitly called anytime when we run our __repr__ on one of our objects or __str__ 
# on one our objects and this can be used to fix printing out this vague employee object
# when we printed out our employee instance here. __repr__ is used to be an ambiguous 
# representation of the object and used for logging and debugging and things like that,
# __str__ is meant to be more of a readable representation of an object and is meant to
# be used as a display to the end-user 

    def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return'{}- {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('divya','tanwar',70000)
emp_2 = Employee('test','user',90000)

print(len(emp_1))



# print(emp_1 + emp_2)

#print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('1','2'))
# print(str.__add__('a','b'))


# class 6 Property Decorators - Getters, Setters, and Deleters
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname