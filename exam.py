Y =input("Do you have any medial cause ?")
X =int(input("What is your attendance score ?"))

if (Y=="Yes") :
    print("You are unfortunately allowed .")
else :
    if (X>75) :
        print("You are unfortunately allowed")
    else :
        print("You are fortunately not allowed")
     