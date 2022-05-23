while(True):
    u=int(input("Enter year of birth or your present age: "))
    if u>0 and u<=99:
        age=u
    elif u<0    or u>2022:
        print("You are not yet born\n")
        break
    elif u>1900 and u<=2022:
        yob=u
    elif u<1900 or u>99:
        print("You are seem to be the oldest person alive\n")
        break
    else:
        print("Enter a valid input!!")
    print("1.To Know when you are 100 years old\n2.To know your age in particular year")
    ch=int(input())
    age=2022-yob
    yob=2022-age
    yh=(2022-age)+100
    sh=yob+100
    if ch==1:
        print(f"You will be 100 years old in year {yh}\n")
    elif ch==2:
        year=int(input("Enter the year in which you want to know your age:"))
        page=(year-2022)+age
        print(f"Your age in {year} is {page}.")
    else:
        print("Enter a valid choice!!!!")