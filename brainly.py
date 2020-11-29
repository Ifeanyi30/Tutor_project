def product_sum():

   accumulated_product = 0
   
   # infinite for loop with iter(callable, sentinel)
   for y in iter(list, 1):

       num1 = int(input("Enter a number: "))

       num2 = int(input("Enter a number: "))

       if num1 == 0 and num2 == 0:

           return  # or quit() or just return 0

       product = num1 * num2

       accumulated_product += product

       print("The product of {} and {} is {}. The accumulated product is {}".format(num1, num2, product, accumulated_product))



product_sum()


in1 = int(input("Enter value one: "))
in2 = int(input("Enter value two: "))



print(in1,type(in1), in2, type(in2))
if (in1 <=0 and in2 <=0) or (not in1 <=0 and not in2<=0):
    print( True)
else:
    print( False)