''' This program is about to find our expense calculations'''
import datetime
expense_details = {} # Expense details stored in dictionary
#salary = 0
total = 0            #Total expenditure amount
def salary_validation():
    '''This function is used for salary validatiion'''
    while True:
        while True:
            try:
                global Salary
                Salary = float(input("Enter your salary : "))
                if Salary < 1:
                    print("Enter a positive numbers")
                    break
                return Salary
            except:
                print("Enter valid salary : ")
                break

def expense_validation():
    '''This function is used for expendicture validations'''
    #validate = True
    while True:
        exp_name = (input("Enter your expenditure name : ").lower()).strip()
        if exp_name.isalpha():
            while True:
                try:
                    exp_amt = float(input(f"Enter your {exp_name} amount: "))
                    return [exp_name,exp_amt]
                except:
                    print("Enter valid amount : ")
        else:
            print("Enter valid expenditure name : ")

def expanse_calculator():
    '''This function used to calculates the expenditure'''

    Salary = salary_validation()
    global total
    global temp_sal
    temp_sal = Salary

    while temp_sal > 0:
        e_name = expense_validation()
        d_key = e_name[0]
        if d_key in expense_details.keys():
            e_price = e_name[1]
            if temp_sal >= e_price:
                expense_details[d_key] += e_price
                temp_sal -= e_price
            else:
                print("Insufficint funds")
                break
        else:
            e_price = e_name[1]
            if temp_sal >= e_price:
                expense_details[d_key] = e_price
                temp_sal -= e_price
            else:
                print("Insufficint funds")
                break
        total=sum(expense_details.values())
        while True:
            ch_ip = input("If you want to add any more expenditure [YES|NO]:")
            if ch_ip.lower() == 'no':
                return
            elif ch_ip.lower() == 'yes':
                break
            else:
                print("Invalid entry")

        if total>Salary:
            print("Insufficint funds")
            break
    else:
        print("Insufficint funds")
    return
expanse_calculator()
print(f"\n{' '*17}EXPENDITURE DETAILS\n{datetime.date.today()}")
print(f"Salary{' '*(20-len('Salary'))}:{' '*15}{Salary:.2f}/-\n{'-'*75}")
for exp_key,exp_value in expense_details.items():
    print(f"{exp_key}{' '*(20-len(exp_key))}:{' '*15}{exp_value:.2f}/-")
print(f"{'-'*75}")  
print(f"Total{' '*(20-len('total'))}:{' '*15}{total:.2f}/-")
print(f"Balance{' '*(20-len('Balance'))}:{' '*15}{temp_sal:.2f}/-")
