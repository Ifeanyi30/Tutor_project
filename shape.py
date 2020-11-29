try:
    size = int(input("Enter a number: "))
except ValueError:
    print("must be a number")

if size==0:
    print("number must be greater than zero.")

elif size%2==0:
    print("number must be odd.")
    
else:
    obj = '*'
    mid_size = round(size/2)
    s = size - mid_size
    count = 2
    counts = 1
    for i in range(size+1):
        if i<=mid_size:
            print(" " *(size - i) + (obj+" ") * i)
        elif i>mid_size:
            print(" " * (s + counts) + (obj + " ") * (i - count))
            count += 2
            counts += 1