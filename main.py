import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function that returns a new data frame with the information we are looking for.
def search_dataframe(data, sub):

    # Create an empty DataFrame
    data_match = pd.DataFrame()
    # Find all the instances of the substring we are looking for.
    for i in sub:
        if(coffee_dataframe['Description'].str.contains(i).any()):
            temp_match = data[data['Description'].str.contains(i)]
            data_match = pd.concat([data_match, temp_match])
        else:
            print('NO RESULTS FOUND.')
            break

    return data_match



# Read in the csv file
#df = pd.read_csv('ChaseDebit_Activity_2019.csv')
#print(df[['Balance','Description']])

# Change the date type for the Posting Date from an object to datetime64
#df[['Posting Date']] = df[['Posting Date']].apply(pd.to_datetime)

#df = df.set_index('Posting Date')
#print(df.index)
# Get the datatypes of each column
#print(df.dtypes)

# Convert Date
chase_activity = pd.read_csv('ChaseDebit_Activity_2019.csv', index_col=0, parse_dates=True)
chase_activity[['Posting Date']] = chase_activity[['Posting Date']].apply(pd.to_datetime)
chase_activity = chase_activity.set_index('Posting Date')


# Add columns with year, month, and weekday name to use pandas time-based indexing
chase_activity['Year'] = chase_activity.index.year
chase_activity['Month'] = chase_activity.index.month
chase_activity['Weekday Name'] = chase_activity.index.weekday_name
#print(chase_activity.dtypes)
print(chase_activity.sample(5, random_state=0))

# Find all the transactions in July. Use count() to find the number of transactions. For ex. chase_activity.loc['2019-07'].count() 
#print(chase_activity.loc['2019-10'])

axe = chase_activity.loc['2019-07']

sns.set(rc={'figure.figsize':(11, 4)})

# Infinite loop to get the user to enter the  correct value.
while True:
    month_to_check = input('What month would you like to check? (For example, if July it would be 7) \n')
    if(int(month_to_check) < 1 or int(month_to_check) > 12):
        print('Month is not correct. Please try again.')
    else:
        # Once user enters the month they want to see. A graph showing the activity on that month will pop up.
        month_to_check = str('2019-' + month_to_check)
        #axe = chase_activity.loc[month_to_check, 'Amount'].plot()
        #axe.set_ylabel('Money Spent')
        #plt.show()
        break

# User wants to see coffee activity
coffee_dataframe = chase_activity

# Substrings to be searched
sub = ['COFFEE','VOYAGER CRAFT COFF', 'CAT CLOUD COMPANION', 'CAPTAIN', 'STARBUCKS']
# Search the dataframe for all the coffee shops
coffee_match = search_dataframe(coffee_dataframe, sub)
print('You have spent a total of ' , coffee_match['Amount'].sum() , 'in coffee.')
#axe = coffee_match.loc['2019', 'Amount'].plot(marker='o', linestyle='-')
#axe.set_ylabel('Coffee Spending')
#plt.show()

# Add up all my work checks that get put into my account
income_dataframe = chase_activity
total_income = income_dataframe[income_dataframe['Description'].str.contains('WORK')]
print('Total income ', total_income['Amount'].sum())
# Get the total spendings by not including my work checks
total_spendings = income_dataframe[~income_dataframe['Description'].str.contains('WORK')]
print('Total spending ', total_spendings['Amount'].sum())


gas_stations = ['7-ELEVEN', 'ARCO', 'CHEVRON', 'DE ANZA GASOLINE']
gas_dataframe = chase_activity
total_gas = search_dataframe(gas_dataframe, gas_stations)
print('Total gas spending ', total_gas['Amount'].sum())


##################################### Load Chase Credit Card activity. #####################################

# Convert Date
chase_credit_activity = pd.read_csv('ChaseCredit_Activity2019.csv', index_col=0, parse_dates=True)
chase_credit_activity[['Post Date']] = chase_credit_activity[['Post Date']].apply(pd.to_datetime)
chase_credit_activity = chase_credit_activity.set_index('Post Date')


# Add columns with year, month, and weekday name to use pandas time-based indexing
chase_credit_activity['Year'] = chase_credit_activity.index.year
chase_credit_activity['Month'] = chase_credit_activity.index.month
chase_credit_activity['Weekday Name'] = chase_credit_activity.index.weekday_name
#print(chase_credit_activity.dtypes)

credit_coffee_dataframe = chase_credit_activity

# Substrings to be searched
sub = ['COFFEE', 'CAT CLOUD COMPANION']

coffee_match = pd.DataFrame()
# Find all the instances were the description has coffee in it
for i in sub:
    if(coffee_dataframe['Description'].str.contains(i).any()):
        temp_match = credit_coffee_dataframe[credit_coffee_dataframe['Description'].str.contains(i)]
        coffee_match = pd.concat([coffee_match, temp_match])
    else:
        print('NO RESULTS FOUND.')
        break

    #print(match)
#print(match)
print('Total coffee spending with credit card is', coffee_match['Amount'].sum())

credit_gas_dataframe = chase_credit_activity

# Get all the instances where Gas is the name of the category.
gas_match = credit_gas_dataframe[credit_gas_dataframe['Category'].str.contains('Gas', na=False)]
print('Total gas spent on credit card is', gas_match['Amount'].sum())

# Get the most I have wasted on gas.
print(gas_match['Amount'].min())
print(gas_match.loc[gas_match['Amount'].idxmin()])


