"""
In the second script:
 1 - import a variable from the first one and print it type and id;
 2 - create a variable containing your age and print its type and id. In the next line change this variable
  and print type and id again
"""

# import variables from the first file
import first

# print variables type and id from the first file
print("Type for name is", type(first.my_name), "and id for name is", id(first.my_name))
print("Type for surname is", type(first.my_surname), "and id for surname is", id(first.my_surname))

# create a variable containing your age by input it from console
my_age = input('Please, enter your age:')
# print its type and id
print("Your current age type is", type(my_age), "and your current age id is", id(my_age))

# change my_age variable and print type and id again
new_age = int(my_age) + 10
print('Your future age is', new_age, ", type is", type(new_age), "and your future age id is", id(new_age))
