"""
Generate Stacked Graph
by zgod

Generates a stacked bar graph of dollar amounts spent each month at given locations
"""

import re
import matplotlib.pyplot as pyplot
import datetime
import numpy as np
from calendar import month_abbr


def generate_stacked_graph(filename, locations):
    """
    takes a BoA-generated like file and list of locations
    generates a stacked bar graph with monthly amounts spent at each location
    """

    #set constants for left offset and width of bars
    LEFT_OFFSET = 0.4
    BAR_WIDTH = 0.6

    print('num of locations:', len(locations))
    print(locations)

    #first scan file to determine sample size (# of months)
    lines = []
    months = []
    curmonth = 0
    for line in open(filename):
        lines.append(line)
        month = int(line[:2])
        if month != curmonth:
            curmonth = month
            months.append(month)


    # print('sample size:', len(months))
    # print('months: ', months)

    #set sample size
    N = len(months)

    #initialize data matrix for totals
    #total amount spent for each month at location
    totals = [[0.0 for i in range(N)] for j in range(len(locations))]

    #now scan filelines to calc amounts spent at each location for each month
    spaces = re.compile(r'\s{2,}')
    comma = re.compile(',')
    i = 0
    curmonth = months[0]
    for line in lines:

        #split up each tx entry by word
        breakup = spaces.split(line.rstrip())
        month = int(breakup[0][:2])
        if month != curmonth:
            curmonth = month
            i += 1

        txwords = breakup[1].split(' ')

        #if txword matches location, add the amount spent to total
        #use done flag to break out
        done = False
        for word in txwords:
            for j in range(len(locations)):
                if word.upper() == locations[j]:
                    totals[j][i] += abs(float(breakup[2]))
                    done = True
                    break
            if done:
                break
    
    #set stacking specs and labels
    col_start = np.arange(N) + LEFT_OFFSET
    y_offset = np.array([0.0] * N)
    colors = pyplot.cm.Set1(np.linspace(0, 1, N))
    x_labels = [month_abbr[x] for x in months]
    

    #plot bar graph - stacking row by row
    for row in range(len(totals)):
        pyplot.bar(col_start, totals[row], BAR_WIDTH, label=locations[row], bottom=y_offset, color=colors[row])
        y_offset += totals[row]

    #set graph display settings
    pyplot.legend(loc=1, bbox_to_anchor=(1.3,1.15))
    pyplot.xticks(col_start + BAR_WIDTH/2.0, x_labels, rotation=45)
    pyplot.grid(axis='y')
    pyplot.tight_layout()
    pyplot.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.75)
    pyplot.xlabel('Months')
    pyplot.ylabel('Amount Spent')

    #display graph
    pyplot.show()

#generate_stacked_graph(r'C:\code\testtransactionlist.txt', ['PUBLIX', 'WHOLE', 'WAL-MART', 'KROGER'])