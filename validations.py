def validate_amount(amount):
    try:
        amount=float(amount)

        if amount<=0:
            print("Amount must be greater than zero.")
            return False
        return True 
    except ValueError:
        print("Please enter a valid numeric amount.")
        return False
    
def validate_text(value,field_name):
    if value.strip()=="":
        print(f"{field_name} cannot be empty.")
        return False
    return True