
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
        return \
        f'''Financial Analysis'
----------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${avg_change}
Greatest Increase in Profits: {increase[0]} (${increase[1]})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})
'''
# In[14]:
output = bank_statement()
print(output)
with open("pybank.txt", "w") as file:
    file.write(output)




