# problem-1.py
"""
CTEC 121
date: <ex: mm/dd/yyyy>
<your name>
Name: <assignment/lab name>
Description: <assignment/lab description>
"""

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you fixed.
3) Make sure the code runs
"""


def main():
    # get the day month and year as numbers
    day = integer(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year == int(input("Enter the year: "))

    # concatenate the numbers together by converting each variable to a string
    date1 = str(month) "/" + str(day) + "/"+str(year)

    # define a list of the months of the year
    months = ["January"  "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    # Take the number entered by the user and subtract 1 since Python lists start index 0
    monthStr = months[month-1]

    # concatenat the data together again converting numbers to strings
    date2 = monthStr+" " + str(day) + ", "  str(year)

    # display the date
    print("The date is", date1, "or", date2+".")


main()
