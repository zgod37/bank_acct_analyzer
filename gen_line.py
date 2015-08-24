"""
Generate line graph of account balances over time
by zgod

Generates a simple line graph of account balances over time, with option to combine totals of each account
"""

import re
import matplotlib.pyplot as pyplot
import datetime

def make_account(filepath):
    """
    generates an account of dates vs. balances
    accepts a filename for BoA-generated transaction list
    #parses the txt file and creates two lists of coordinating dates and balances for a bank account
    #returns an account tuple -> ([dates], [balances])
    """

    dates = []
    balances = []

    #each line consists of 4 columns separated by 2 or more spaces
    spaces = re.compile(r'\s{2,}')
    comma = re.compile(',')
    for line in open(filepath):

        breakup = spaces.split(line.rstrip())

        #ensure filename is in correct format
        if len(breakup) > 3:

            #convert date from 'mm/dd/yyyy' to datetime objects
            datebreak = breakup[0].split('/')
            year = int(datebreak[2])
            month = int(datebreak[0])
            day = int(datebreak[1])

            #remove comma from "x,xxx" format
            balance = comma.sub('', breakup[3])

            #add date and balance to lists
            dates.append(datetime.datetime(year, month, day))
            balances.append(float(balance))

    return (dates, balances)

def combine_monthly_balances(accounts):
    """
    takes in 1 or more accounts and computes the monthly balance for each
    returns a combined account -> ([list of monthly dates], [total balances from each account])
    """

    balances = []
    dates = []

    #get monthly balance for each account
    #use index to limit datelist size to one account
    index = 0
    for account in accounts:
        acct_dates, acct_balances = account

        #initialize with first balance and starting month
        monthlybalances = [acct_balances[0]]
        startdate = acct_dates[0]
        curmonth = startdate.month

        #datelist only needs to be populated from one account
        if index == 0:
            dates.append(startdate)

        #pair up dates and balances and grab one from each month
        for date, balance in zip(acct_dates, acct_balances):
            if curmonth != date.month:
                curmonth = date.month
                monthlybalances.append(balance)
                if index == 0:
                    dates.append(date)
        balances.append(monthlybalances)
        index += 1

    #now combine balances
    combined_balances = []
    for i in range(len(balances[0])):
        total = 0
        for j in range(len(balances)):
            total += balances[j][i]
        combined_balances.append(total)

    return (dates, combined_balances)

def generate_graph(filepaths, include_totals=False):
    """
    Takes any number filepaths to BoA-like transaction lists
    Creates an account of dates/balances for each filepath given
    Plots a simple line graph of account balances per month
    Optional argument to include combined totals of all accounts
    """

    accounts = []
    for filepath in filepaths:
        accounts.append(make_account(filepath))

    labels = ["Account "+str(i+1) for i in range(len(accounts))]

    if include_totals:
        accounts.append(combine_monthly_balances(accounts))
        labels.append("Totals")

    #plot each account
    for i in range(len(accounts)):
        x,y = accounts[i]
        pyplot.plot(x,y,label=labels[i])
    
    #set graph display settings
    pyplot.legend(loc=9,bbox_to_anchor=(0.5,1.05))
    pyplot.xlabel('Months')
    pyplot.ylabel('Account Balance')
    pyplot.xticks(rotation=45)
    pyplot.grid()
    pyplot.tight_layout()
    pyplot.show()

#generate_graph([r'C:\code\BoAcheckinglist.txt',r'C:\code\BoAsavingslist.txt'], True)