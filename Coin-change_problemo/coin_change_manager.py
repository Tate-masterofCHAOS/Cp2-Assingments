import csv


def coin_change_main():
    with open('Coin-change_problemo/currencies.csv', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)  

        try:
            
            currencyLine = int(input("USD(1), BRL(2), JPY(3), or GBP(4)? "))  
            if currencyLine not in [1, 2, 3, 4]:
                print("Invalid choice")  
                return
            
           
            amount = float(input("How much money? ").replace(",", "."))  

            
            if currencyLine in [1, 2, 4]:  
                
                if len(str(amount).split(".")[1]) > 2:
                    print("Money only goes to two decimals (extra decimals will be rounded).")
                amount = round(amount, 2)  
            elif currencyLine == 3:  
                if amount % 1 != 0:
                    print("Yen doesn't have decimals. The decimal portion will be removed.")
                amount = int(amount)  
            
            amount = round(amount * 100)  
            

            if amount == 0:
                print("You need 0 coins/bills.")
                return
            
         
            elif amount < 0:
                print("You are in debt, you don't get any denominations.")
                return

        
            elif isinstance(amount, complex) and amount.imag != 0:
                print("You only have money in your imagination, get a job please!!")
                return
            
        except ValueError:
          
            print("Please enter numbers.")
            return

        
        def process_currency_row(currencyLine, rows):
            row = rows[currencyLine]  
            denominations = []  

           
            for i in range(1, len(row) - 1, 2):
                name = row[i]  
                try:
                    
                    value = float(row[i + 1])  
                    value = round(value * 100)  
                    denominations.append((value, name))  
                except ValueError:
                    print(f"Skipping invalid entry: {row[i + 1]}")
                    continue

            return denominations

        denominations = process_currency_row(currencyLine, rows)

        denominations.sort(reverse=True)

        change = {}
        for value, name in denominations:
            if amount >= value:
                count = amount // value  
                amount %= value  
                change[name] = count  

        
        print("\nChange breakdown:")
        for name, count in change.items():
            print(f"{count} × {name}")

       
        if amount > 0:
            print(f"Leftover: {amount / 100:.2f}")  

