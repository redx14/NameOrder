#Andrey Ilkiv 9/30/2020 section 01 print functions

#program start()
name1 = input("Please enter name 1 : ")
#User asked to enter name and is stored in name1 variable
name2 = input("Please enter name 2 : ")
#User asked to enter name and is stored in name2 variable
name3 = input("Please enter name 3 : ")
#User asked to enter name and is stored in name3 variable

print('\n')
#prints empty line and goes to the next line of code
print('Here are your names in every possible order:' , '--------------------------------------------' , '' , sep='\n')
#prints out heading and at the end of the print function prints an empty line
print('1. ' , name1 , ', ' , name2 , ', ' , name3 , '\n' , sep='')
#prints out the string "1. " + name1 + "," + name2 + "," + name3 seperated by a 'empty space' in place of commas in code
#prints out an empty line at the end of the print function
#code can also be written as print('1. ' + name1 + ', ' + name2 + ', ' + name3 , '\n')
print('2. ' , name1 , ', ' , name3 , ', ' , name2 , '\n' , sep='')
#prints out the string "2. " + name1 + "," + name3 + "," + name2 seperated by a 'empty space' in place of commas in code
#prints out an empty line at the end of the print function
print('3. ' , name2 , ', ' , name1 , ', ' , name3 , '\n' , sep='')
#prints out the string "3. " + name2 + "," + name1 + "," + name3 seperated by a 'empty space' in place of commas in code
#prints out an empty line at the end of the print function
print('4. ' + name2 , name3 , name1 , '' , sep='\n')
#prints out the string "4. " + name2
#moves down one line and prints name3
#moves down one line and prints name1
#prints out empty line at the end of the print function
print('5. ' + name3 , name2 , name1 , '' , sep='\n')
#prints out the string "5. " + name3
#moves down one line and prints name2
#moves down one line and prints name1
#prints out empty line at the end of the print function
print('6. ' + name3 , name1 , name2 , sep='\n')
#prints out the string "6. " + name3
#moves down one line and prints name1
#moves down one line and prints name2
#in this function we do not need a filler " '' " to print next line so we dont include it in the code.

