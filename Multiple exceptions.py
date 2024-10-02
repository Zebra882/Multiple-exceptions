try:
    num1,num2=eval(input("enter two numbers separated by comma: "))
    result=num1/num2
    print("result is : ",result)
    
#use multiple except block for diffrent types of error
except ZeroDivisionError:
    print("division by zero is an error")
    
except SyntaxError:
    print("comma is missing.Enter the numbers separated by comma like 1,2")

except:
    print("Wrong input")
    
else:
    print("No exception")
    
finally:
    print("This will excicute no matter what.")
    