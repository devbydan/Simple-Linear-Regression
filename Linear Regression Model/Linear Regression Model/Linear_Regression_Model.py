'''
 Author  -> Dan Murphy
 Project -> Simple Linear Regression
 Purpose -> Modeling the relationship between
		    a dependent variable and
			independent variable(s).
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 File    -> Linear_Regressoin_Model.py
'''


# Imported libraries ===================
# import mean functionality
from statistics import mean
# allow seeding functionality
from numpy.random import seed
# allow seeding of random integers
from numpy.random import randint
# ======================================

# Instantiate seeding process ------------------------
seed(1) # Force seed to generator random numbers
# Below this point, seeding is permitted -------------

# Store sequence of integers pre-randomized
sequence_of_integers = [i for i in range(20)]
# For debugging purposes, display the current sequence
# print(sequence_of_integers)

### Randomize the sequence of integers via shuffle func ###
x_values = ( shuffle(sequence_of_integers) )
y_values = ( shuffle(sequence_of_integers) )


'''
 Author  -> Dan Murphy
 Method  -> Simple Linear Regression
 Purpose -> Modeling the relationship between
		    a dependent variable and
			independent variable(s).
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 File    -> Linear_Regression_Model.py
'''

