class Calculation:
    def __init__(self, number=0, operator=None):
        self._number = number
        self._operator = operator
        self._value = None

    def set_operator(self, new_operator):
        self._operator = new_operator
    
    def get_operator(self):
        return self._operator

    operator = property(get_operator, set_operator)

    def set_number(self, new_number):
        self._number = new_number

    def get_number(self):
        return self._number

    number = property(get_number, set_number)

    def set_value(self, new_value):
        self._value = new_value

    def get_value(self):
        return self._value

    value = property(get_value, set_value)

    def calculate(self):
        if self._operator == "+":
            self._number += self._value
        elif self._operator == "-":
            self._number -= self._value
        elif self._operator == "*":
            self._number *= self._value
        elif self._operator == "/":
            self._number /= self._value
        elif self._operator == None: 
            self._number = self._value
            print("Value reset to {}".format(self._value))
            
def main():

    print("""
    Welcome to continuous calculator
    --------------------------------
    Please enter an operator.

    + for addition
    - for substraction
    * for multiplication
    / for division
    """)

    valid_op = ['+','-','*','/']
    special_nums = ['e','pi']
    end = False
    calc = Calculation()

    print("Enter operator or number ('end' to stop, 'r' to reset): ")

    while end == False: 
        
        in_str = input("\nOperator: [{}] Value: [{}]: ".format(calc.operator, calc.number))
        
        if in_str.lower() == "end":
            end = True
        elif in_str in valid_op: 
            calc.operator = in_str
        # Incase of special numbers
        elif in_str in special_nums:
            if in_str == 'pi':
                calc.value = 3.14159
            elif in_str == 'e':
                calc.value = 2.718281828
            calc.calculate()
        # Reset case
        elif in_str == 'r':
            calc.number = 0
            calc.value = 0
            calc.operator = None
        else:
            try:
                calc.value = float(in_str)
                calc.calculate()
            except:
                print("ERROR: Value is not a float, int or a valid operator. Please try again.")
        
if __name__=="__main__":
    main()