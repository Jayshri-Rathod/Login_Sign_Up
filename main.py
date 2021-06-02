import json
print("WELCOME TO SIGN UP/LOG IN PAGE")
num=input("DO YOU HAVE AN ACCOUNT:")
if num=="yes" or num=="y":
    f=open("userdetails.json","r")
    fn=f.read()
    user_name=input("enter your user ID:")                                              
    pass_word=input("enter your password :")
    if user_name in fn and pass_word in fn:
        print(user_name,"you have logged in succesfully")
    else:
        print("sorry! invalid username and password")
    f.close()
if num=="no" or num=="n":
    new=input("DO YOU WANT TO SIGN UP ACCOUNT?")
    if new=="yes":
        username1=input("enter your first name :")
        username2=input("enter your last name :")
        name=username1+username2
        print("USERNAME :",name)
        password1=input("enter your password:")
        if "$" or "@" in password1:
            if len(password1)>=6 and len(password1)<=16:
                if "2" or "8" in password1:
                    pass   
            else:
                print("You are using weak password")        
        else:
            print("at least password shoud contain one special charecter")
        password2=input("Confairm your password:")
        if password1!=password2:
            print("PASSWORD :",password1)
            print("both password are not same")
        else:
            print("congrats",name,"you have sign up succsefully!")
        a=[]
        a.append(name)
        a.append(password1)
        b=["username","password"]
        user={}
        for i in range(len(b)):
            user.update({b[i]:a[i]})
        with open("userdetails.json","w") as f:
            json.dump(user,f,indent=2)
        print("we want your information")
        print()
        description=input("enter whatever you like :")
        Dob=input("enter your Date of Birth :")
        Gender=input("enter your gender :")
        Hobbies=input("enter your hobbies :")
        print()
        print("Thank you for giving me your information")
        list1=["Discription","Dob","Gender","hobbies"]
        c=[]
        c.append(description)
        c.append(Dob)
        c.append(Gender)
        c.append(Hobbies)
        profile={}
        for i in range(len(list1)):
            profile.update({list1[i]:c[i]})
        k={"user":user,"profile":profile}
        with open("userdetails.json","w") as f:
            json.dump(k,f,indent=2)
        f.close()
