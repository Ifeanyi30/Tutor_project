import re

with open("../../Downloads/Tweets.txt","r", encoding="utf-8") as tweets:
    myfile = tweets.readlines()
    for item in myfile:
        item = item.rstrip()
        mylist = re.findall("^RT (.*) ", item)
        if len(mylist) !=0:
            for line in mylist:
                if line.count("#") >=1:
                    ln = line.split("#")
                    dm = ln[1]
                    print(f"#{dm}")

def powersOf3ToN(n):
    try:
        num = int(round(n))
    except (ValueError, NameError, TypeError):
        print("Parameter of the function must be integer or float")
        quit()

    num_list = range(num)
    val_list = [pow(3,x) for x in num_list if pow(3,x) in num_list]
    print(val_list)

powersOf3ToN(30)