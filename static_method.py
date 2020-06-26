class MethodTypes:
  @staticmethod
  def factorial(number):
        if number == 0:
            return 1
        else:
            return number * MethodTypes.factorial(number - 1)
       
factorial = MethodTypes.factorial(5)
print(factorial)
