import pandas as pd
from pathlib import Path

def financial_analysis(x):
    path = Path().resolve() / x
    budget_data = pd.read_csv(path)
    
    profit = budget_data['Profit/Losses']
    date = budget_data['Date']
    change = []
    date_of_change = dict()
    for index, value in enumerate(profit):
        if index == 0:
            pass
        else:
            difference = value - profit[(index - 1)]
            change.append(difference)
            date_of_change[date[index]] = difference
    
    date_list = list(date_of_change.keys())
    difference_list = list(date_of_change.values())
    
    total_months = len(date)
    total = sum(profit)
    average = sum(change)/len(change)
    greatest_increase = max(change)
    greatest_decrease = min(change)
    date_of_greatest_increase = date_list[difference_list.index(max(difference_list))]
    date_of_greatest_decrease = date_list[difference_list.index(min(difference_list))]
    return (
        f'''  
        Financial Analysis 
        {"-"*30} 
        Total Months: ${total_months}
        Total: ${total}
        Average Change: {round(average, 2)}
        Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})
        Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})
        '''
    )
           
def create_financial_analysis_text(x):
    body = financial_analysis(x)
    with open('analysis.txt', 'w') as f:
        f.write(body)
    return print(body)


if __name__ == '__main__':
    create_financial_analysis_text('budget_data.csv')