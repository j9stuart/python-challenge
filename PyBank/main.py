
# coding: utf-8

# In[1]:


import csv


# In[11]:


def bank_statement():
    with open('PyBankData.csv') as file:
        bank_data = csv.reader(file, delimiter=",")
        next(bank_data)
        total_months = 0
        total_profit = 0
        changes = []
        increase = [0,0]
        decrease = [0,0]
        last_row = 0
        for row in bank_data:
            profit = int(row[1])
            if total_months > 0:
                change = profit - last_row
                changes.append(change)
                if change > int(increase[1]):
                    increase = [row[0], row[1]]
                if change < int(decrease[1]):
                    decrease = [row[0], row[1]]
            last_row = profit
            total_months += 1
            total_profit += profit
        avg_change = round(sum(changes)/ len(changes))
        print('Financial Analysis')
        print('----------------------')
        print(f'Total Months: {total_months}')
        print(f'Total: ${total_profit}')
        print(f'Average Change: ${avg_change}')
        print(f'Greatest Increase in Profits: {increase[0]} (${increase[1]})')
        print(f'Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})')
        return('Financial Analysis')
        return('----------------------')
        return(f'Total Months: {total_months}')
        return(f'Total: ${total_profit}')
        return(f'Average Change: ${avg_change}')
        return(f'Greatest Increase in Profits: {increase[0]} (${increase[1]})')
        return(f'Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})')


# In[14]:


output = bank_statement()
file = open("pybank.txt")
file.write(output)
file.close()

