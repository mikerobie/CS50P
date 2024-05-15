
def main():
    
    list = ["3801-2", "3+3", "4*4"]
    a, b, c = list

    arithmetic = str(a)
    
    #print(a)

    numbers = []
    operands = []

    for item in arithmetic:
        if item.isdigit():
            numbers.append(int(item))
        elif item in ['+', '-', '*', '/']:
            operands.append(item)

    concatenated_string = ''.join(str(num) for num in numbers)
    
    print(concatenated_string)
    
    
    #print(str(numbers))
    #print(operands)



    #if "-" in a:
     #   operand = "-"
      #  print("Minus is found!!!!")
    
    #print(b)
    #print(c)
    #if is_even(x)
    #    print("Even")
   # else:
     #   print("Odd")

#def is_even(n):
 #   return True if n % 2 == 0 else False

main()





#arithmetic_arranger(["3801 - 2", "123 + 49"]) should return   3801      123\n-    2    +  49\n------    -----.