large = int(input("How large is the loan? (in a scale from 1-10)"))
credit = int(input("How good is your credit history?(in a scale from 1-10)"))
income = int(input("How high is your income?(in a scale from 1-10)"))
payment = int(input("How large is your down payment?(in a scale from 1-10)"))

loan_bool = None

if large >= 5:
    if credit >= 7 and income >= 7:
        print("yes.1")
        loan_bool = True
    elif credit >= 7 or income >= 7:    
        if payment >= 5:
            loan_bool = True
            print("yes.2")
        else:
            loan_bool = False
            print("no.1")
    else:
        loan_bool=False

elif large < 5 :
    if credit < 4:
        loan_bool = False
        print("no.2")
    elif income >= 7 or payment >= 7:
        loan_bool = True
        print("yes.3")
    elif income >= 4 and payment >= 4:
        loan_bool = True
        print("yes.4")
    else:
        loan_bool = False
        print("no.3")

if loan_bool == True:
    print("YES")
elif loan_bool==False:
    print("NO")
