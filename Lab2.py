#Charlie Hammond | A00080108

num_a = 5
num_b = 6
num_c = 7

NUM_OF_INPUTS = 3

num_average = (num_a + num_b + num_c) / NUM_OF_INPUTS

print("The average of",num_a,",",num_b,"and",num_c,"is:",num_average)
print("The average of "+str(num_a)+", "+str(num_b)+" and "+str(num_c)+" is: "+str(num_average))
print("The average of {0}, {1} and {2} is: {3}".format(num_a,num_b,num_c,num_average))

#------------------------------------------------------------------------------------------------------------------------------

weight_p = 123

CALORIES_PER_POUND = 19

calories_needed = weight_p * CALORIES_PER_POUND

print("Your weight is:",weight_p,"pounds, and your calories needed per day are:",calories_needed)
print("Your weight is: "+str(weight_p)+" pounds, and your calories needed per day are: "+str(calories_needed))
print("Your weight is: {0} pounds, and your calories needed per day are: {1}".format(weight_p,calories_needed))

#------------------------------------------------------------------------------------------------------------------------------

earth_age = 18
mercury_days = 88
venus_days = 225
jupiter_days = 4380
saturn_days = 10767

EARTH_YEAR = 365
print("Your age on Earth is: {0}".format(earth_age))

mercury_age = (18 * EARTH_YEAR) // mercury_days
print("Your age on Mercury is: {0}".format(mercury_age))

venus_age = (18 * EARTH_YEAR) // venus_days
print("Your age on Venus is: {0}".format(venus_age))

jupiter_age = (18 * EARTH_YEAR) // jupiter_days
print("Your age on Jupiter is: {0}".format(jupiter_age))

saturn_age = (18 * EARTH_YEAR) // saturn_days
print("Your age on Saturn is: {0}".format(saturn_age))
