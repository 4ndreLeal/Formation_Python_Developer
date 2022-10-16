current_balance_bank_account = 0
current_amount = 0
limit_amount_withdrawn = 500
number_withdrawal = 0
bank_extract = ""
WITHDRAWAL_LIMIT = 3
control = True

def menu():
    return """
☆                          ☆
☆   [d] DEPOSIT            ☆
☆   [w] WITHDRAWAL         ☆
☆   [e] BANK EXTRACT       ☆
☆   [q] END BANK PROCESS   ☆
☆                          ☆
"""

def format_string(string_menu: str):
    return "\n" + string_menu.center(len(string_menu) + 56, "=") + "\n"

def define_transaction(show_menu: str):
    print(show_menu)
    option = input("Financial operation:\n=> ")
    return option

def execute_transaction_deposit():
    get_amount_deposit = float(input("Amount to be deposited: $ "))
    return get_amount_deposit
    
def execute_transaction_withdrawal():
    get_amount_withdrawal = float(input("Amount to be withdrawn: $ "))
    return get_amount_withdrawal

def update_bank_extract(insert_values_bank_extract: float, string_to_identify_which_transaction: str):
    if string_to_identify_which_transaction == "d":
        return f"Deposit: $ {insert_values_bank_extract:.2f}\n"
    else:
        return f"Withdrawal: $ {insert_values_bank_extract:.2f}\n"
        
while(control):
    choose_transaction = define_transaction(format_string(menu()))
    match choose_transaction:
        case "d":
            current_amount = execute_transaction_deposit()
            if current_amount > 0:
                current_balance_bank_account += current_amount
                bank_extract += update_bank_extract(current_amount, "d")
            else:
                print("_" * 26)
                print("|Invalid amount detected.|")
                print("-" * 26)
        case "w":
            current_amount = execute_transaction_withdrawal()
            balance_exceeded = current_amount > current_balance_bank_account
            limit_exceeded = current_amount > limit_amount_withdrawn
            withdrawal_exceeded = WITHDRAWAL_LIMIT <= number_withdrawal
            if balance_exceeded:
                print("_" * 77)
                print("|Transaction failed. You don't have enough balance to make this transaction.|")
                print("-" * 77)
            elif limit_exceeded:
                print("_" * 75)
                print("|Transaction failed. The amount requested to withdrawal exceeds the limit.|")
                print("-" * 75)
            elif withdrawal_exceeded:
                print("_" * 65)
                print("|Transaction failed. You exceeded the daily limit of withdrawal.|")
                print("-" * 65)
            elif current_amount > 0:
                current_balance_bank_account -= current_amount
                bank_extract += update_bank_extract(current_amount, "w")
                number_withdrawal += 1
            else:
                print("_" * 26)
                print("|Invalid amount detected.|")
                print("-" * 26)

        case "e":
            print("\n" + " EXTRACT ".center(40, "~"))
            print("You haven't made transactions." if not bank_extract else bank_extract)
            print(f"\nCurrent balance: $ {current_balance_bank_account:.2f}")
            print("=" * 40)
        case "q":
            print(f'You have closed your transactions with $ {current_balance_bank_account:.2f}.')
            control = not control
        case _:
            print(f"{choose_transaction} is an invalid operation. Try again.")
