# Simple Bank Account Analyzer and Graph Maker
### Written in Python 3.4 by zgod

## Introduction

Hello! This is the very first program that I ever wrote (circa 2014).  I was dissatisfied with my bank's online spending tracker and how it presented its data. I wanted a much more simple presentation, but yet more customizable.  So I decided that I would write my own program to present the data in a way that I wanted.  In the process, I learned alot about coding, graphs, and even some UI! Plus, it sparked an interest in software development that I didn't know I had!

## Input constraints

This program was designed to read an auto-generated .txt file from Bank of America's online banking system. consisting of a list of transactions from a given checking/savings account. However, it can be used with any file where transactions are listed in the following format:

The following fields from left -> right on a single line, each separated by 2 or more spaces

1. Date of transaction (mm/dd/yyyy)
2. Transaction description
3. Change in account balance (xxx,xxx.xx)
4. New account balance (xxx,xxx.xx)

Example entries

>04/08/2014     CHECKCARD CHIPOTLE YOURTOWN,USA 34095096              -7.00     2,837.00

>04/09/2014     TRADER JOES MYTOWN,USA 20030445 CHECKCARD            -37.00     2,800.00

## Quick guide

1. First put your account files in the "accts" folder. Make sure they are .txt files!
2. Double click 'main.py' to open the simple console interface
3. Select which type of graph you want to make
  * Option 1 will generate a line graph of your account balance over time, for each account file in the accts folder
  * Option 2 will generate a stacked graph showing how much you spend at each month at the locations you choose! (see below for details)
4. Use the data to gain insight on your spending habits
5. Rinse & Repeat

### Notes about entering locations for stacked graphs

* Be sure to use only one word per location (e.g. "whole" instead of "whole foods")
* Check your file's transaction description to get an idea of how they're stored in your bank's database. For example, Marathon gas stations are listed in my bank as "MARATHO"
* Beware! Some purveyors have seemingly random transaction descriptions, e.g. Wal-Mart is sometimes listed as "WM SUPERCENTER" and "WAL-MART" other times. YMMV
