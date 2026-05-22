import json

def save_expenses(expenses):
    try:
        with open("expenses.json","w") as file:
            json.dump(expenses,file,indent=4)
    except Exception as error:
        print("Error saving expenses:",error)

def load_expenses():
    try:
        with open("expenses.json","r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Expenses file is corrupted. Starting with empty expense list.")
        return []
    
    except Exception as error:
        print("Unexpected error while loading expenses:",error)
        return []