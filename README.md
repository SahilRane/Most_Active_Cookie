# MostActiveCookie

This repository contains two main files: most_active_cookie.py and test_most_active_cookie.py. The most_active_cookie.py file contains the program for the calculation of the most active cookie/(s) on a particular date given to us. The most_active_cookie.py uses the csv, argparse, and sys python libraries for reading the arguments and the log csv file. We are given a csv log file and most_active_cookie.py will process the data in the csv file and will find the most active cookie/(s) on a particular date and we return a string containing the cookie/(s). The second file test_most_active_cookie.py contains some test cases run on the log files test.csv and test2.csv. They are 4 main cases that we are testing: 
1. Date given to us on which to find the active cookie is not in the log file 
2. There is only one most active cookie on the date given to us 
3. There are multiple most active cookies on the date given to us
4. The frequency of occurences of the most active cookie/(s) on the date given to us is more than one.

We test all of the above types of test cases on both the test.csv and test2.csv log files.

# Usage
The file-path and the date in YYYY-MM-DD format must be passed as arguments in the command line.
The code can be run using the command:

$python3 most_active_cookie.py test.csv -d 2018-12-08

The test case file can be run using:

$python3 test_most_active_cookie.py
