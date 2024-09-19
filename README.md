# vail-coding-assignment-dbelasich

This is Dan Belasich's submission for the following coding exercise:

The problem we would like you to solve deals with an array of integers. We want to rotate these integers to a specified number of positions to the left.
If for example you have an array of integers [1,2,3,4,5,6,7] and we would like to rotate 2 positions to the left, the solution expected would be [3,4,5,6,7,1,2].
Note: the solution should be able to handle a position value greater than the number of integers in the array. If, for example, we would like to rotate [1,2,3,4,5,6,7] 8 positions to left, it would produce the result [2,3,4,5,6,7,1]. Negative values for the positions to rotate will throw an error which the code example should handle gracefully.

# Notes:
This solution was written in Python, and is located in the module shift_position.py

The test cases for this solution are in the "tests" package in the module "test_shift_position.py"
If you wish to run these test cases, please do the following:

1. Create a virtual environment and activate it
2. Run the following command: "pip install -r requirements.txt" to install pytest and its dependencies
3. From the project root directory, run the test module with the command: "pytest tests/test_shift_position.py"
