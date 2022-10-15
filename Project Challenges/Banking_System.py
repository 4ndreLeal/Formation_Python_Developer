current_amount_into_bank_account = float(input("How much money do you have into your Bank account? $ "))
current_amount_deposited = 0
current_amount_withdrawn = 0
bank_extract_dictionary = {
    "Amount deposited": 0,
    "Amount withdrawn": 0,
}
WITHDRAWAL_LIMIT = 3
current_number_withdrawals = 0
control = True

menu = """
*                             *
*   [d] Deposit               *
*   [w] Withdrawal            *
*   [e] Bank extract          *
*   [l] End banking process   *
*                             *
"""

menu_exception = """
*                             *
*   [d] Deposit               *
*   [e] Bank extract          *
*   [l] End banking process   *
*                             *
"""

def format_string(string_menu: str):
    return "\n" + string_menu.center(len(string_menu) + 62, "*") + "\n"

def define_transaction(show_menu: str):
    print(show_menu)
    option = input("Financial operation: ")
    return option

def execute_transaction_deposit():
    get_amount_deposit = -1
    while get_amount_deposit <= 0:
        get_amount_deposit = float(input("Amount to be deposited: $ "))
    return get_amount_deposit
    
def execute_transaction_withdrawal(amount_to_check_available_of_transaction: float):
    get_amount_withdrawal = -1
    counter = 0
    while get_amount_withdrawal <= 0 or get_amount_withdrawal > 500 or get_amount_withdrawal > amount_to_check_available_of_transaction:
        counter += 1
        if counter > 1:
            print("Choose an available option!")
        get_amount_withdrawal = float(input("Amount to be withdrawn: $ "))
    return get_amount_withdrawal

def update_bank_extract(update_values_into_bank_extract_dictionary: dict, values_to_insert_into_bank_extract_dictionary: float, string_to_identify_which_transaction: str):
    if string_to_identify_which_transaction == "d":
        update_values_into_bank_extract_dictionary["Amount deposited"] = values_to_insert_into_bank_extract_dictionary
        return update_values_into_bank_extract_dictionary
    else:
        update_values_into_bank_extract_dictionary["Amount withdrawn"] = values_to_insert_into_bank_extract_dictionary
        return update_values_into_bank_extract_dictionary

def print_bank_extract(dictionary_of_transactions: dict, ends_with_that_money: float):
    for key, value in dictionary_of_transactions.items():
        print(f"{key} = R$ {value:.2f}")
    if ends_with_that_money > 0:
        print(f"You still have $ {ends_with_that_money:.2f}")
    else:
        print(f"You have no money at this point.")
        
while(control):
    choose_transaction = define_transaction(format_string(menu))
    match choose_transaction:
        case "d":
            get_return_of_transaction_deposit = execute_transaction_deposit()
            current_amount_deposited += get_return_of_transaction_deposit
            current_amount_into_bank_account += get_return_of_transaction_deposit
            bank_extract_dictionary = update_bank_extract(bank_extract_dictionary, current_amount_deposited, "d")
        case "w":
            if WITHDRAWAL_LIMIT == current_number_withdrawals:
                print("You can't do another withdrawal transaction!")
                continue
            else:
                get_return_of_transaction_withdrawal = execute_transaction_withdrawal(current_amount_into_bank_account)
                current_amount_withdrawn += get_return_of_transaction_withdrawal
                current_amount_into_bank_account -= get_return_of_transaction_withdrawal
                current_number_withdrawals += 1
                bank_extract_dictionary = update_bank_extract(bank_extract_dictionary, current_amount_withdrawn, "w")
        case "e":
            print_bank_extract(bank_extract_dictionary, current_amount_into_bank_account)
        case "l":
            print_bank_extract(bank_extract_dictionary, current_amount_into_bank_account)
            control = not control
        case _:
            print("Choose an available option!")
            continue
