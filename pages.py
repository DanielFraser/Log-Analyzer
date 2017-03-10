import sys       
import subprocess
import re
import os

# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR():
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
#
def log2hist(logfilename):
    hashtable = dict()  # stores one of each name and assigns their # of pages to each one
    with open(logfilename) as f:  # opens the file (its designed to read large text files
        for line in f:  # goes through each line, one at a time
            nameStr = re.search('user:\s+(\w+)\s+', line)  # gets user's name
            pageStr = re.search('pages:\s+(\d+)\s+', line)  # gets the pages
            if pageStr and nameStr: # makes sure each line has both a name and # of pages before getting name and pages
                name = nameStr.group(1)  # takes the name from the string
                pages = int(pageStr.group(1))  # takes the # of pages in the string
                if name in hashtable:
                    hashtable[name] += pages  # changes the amount of the name exists
                else:
                    hashtable[name] = pages  # creates a new entry along with pages
        f.close() # closes the file
    g = open('data','w+')  # create a file name data if needed
    for keys, values in hashtable.items():  # goes through each value
        g.write(str(values)+"\n")  # writes each value to data
    g.close()  # close data
    runR()  # now executes R to create histogram
    return

if __name__ == '__main__':
    log2hist("log")   # get the log file name from command line

# line above may be changed to log2hist("log") to make the file name
#    always be log
