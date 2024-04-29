class FormulaError(Exception): #Class to make a customized error
    def __init__ (self, message): #Function to assign the correct string as the message
        self.message = message
        super().__init__(self.message)
process = "yes"
while process == "yes":
    try:
        equation = input("Please input an equation comprises only of 3 terms separated by a space (+, -, /, *): ")
        splitted = equation.split()
        if len(splitted) != 3: #If the user did not input a simple equation
                raise FormulaError("Please input only an equation of 3 terms.")
        try:
            if splitted[1] == "+":
                print(float(splitted[0]) + float(splitted[2]))
            elif splitted[1] == "-":
                print(float(splitted[0]) - float(splitted[2]))
            elif splitted[1] == "/":
                print(float(splitted[0]) / float(splitted[2]))
            elif splitted[1] == "*":
                print(float(splitted[0]) * float(splitted[2]))
            else:
                raise FormulaError("Please input a valid operator.") #If the user did not used the given operators
        except ValueError: #If there is a ValueError, raise a FormulaError instead
            raise FormulaError("Please input valid numbers.")
    except FormulaError as error: #To call and print all FormulaError raised
        print(error.message)
    process = input("Do you want to continue (yes/no): ")
    if process != "yes" and process != "no":
        print("Please respond only with yes or no.")