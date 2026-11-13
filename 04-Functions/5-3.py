###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import my_keyboard # your own defined module

# Reads employee's data from keyboard
first_name = my_keyboard.input_string('Enter name: ')
last_name = my_keyboard.input_string('Enter last name: ')
age = my_keyboard.input_integer('Enter age: ')
salary = my_keyboard.input_real('Enter salary: ')
is_salary_hidden = my_keyboard.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last Name:', last_name)
print('Age:', age)
if is_salary_hidden == True:
    print('Salary:', salary)
