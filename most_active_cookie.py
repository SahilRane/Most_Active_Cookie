import sys
import argparse
import csv

class CookieLogProcessor:
    def __init__(self):
        '''
        Constructor for the CookieLogProcessor object that has a dictionary data member to store the values
        read from the cookie-log csv file. The dictionary has the dates as keys and the values are a
        dictionary whose keys are cookies and values are the frequencies of the cookies
        '''
        self.cookie_date_table = {}
    
    def getDate(self, date):
        '''
        This function converts the date as given in the log csv file into the same format as our input date
        for direct comparison
        '''
        for i in range(len(date)):
            if date[i] == 'T':
                return date[:i]
        

    def processFile(self, file_path):
        '''
        This function accesses the csv file using its file path and reads each of its rows updating the
        cookie and date dictionary according to the values in each row.
        '''
        file = open(file_path)
        csvreader = csv.reader(file)
        next(csvreader)
        # iterates through each row in csv file and processes the data
        for row in csvreader:
            cookie = row[0]
            row_date = self.getDate(row[1])
            # updates the cookie date dictionary
            if row_date not in self.cookie_date_table:
                self.cookie_date_table[row_date] = {cookie: 1}
            else:
                if cookie not in self.cookie_date_table[row_date]:
                    self.cookie_date_table[row_date][cookie] = 1
                else:
                    self.cookie_date_table[row_date][cookie] += 1
        file.close()
    
    def findMostActiveCookie(self, date):
        '''
        This function iterates through the cookie date dictionary to find the most active cookie(s) on the 
        particular day that we are asked to check and returns a string containing these cookies on separate
        lines
        '''
        # if no such date is in our log we return None
        if date not in self.cookie_date_table.keys():
            return None
        count_dict = self.cookie_date_table[date]
        output = []
        count = 0
        # iterate through the cookies on a particular date to find the most active cookies
        for cookie in count_dict.keys():
            if count_dict[cookie] > count:
                output = []
                count = count_dict[cookie]
                output.append(cookie)
            elif count_dict[cookie] == count:
                output.append(cookie)
        # create a string to store our output result
        outputstr = ''
        for i, cookie in enumerate(output):
            if i == len(output) - 1:
                outputstr += cookie
            else:
                outputstr += cookie + '\n'
        return outputstr

if __name__ == '__main__':
    # reads the terminal and stores the arguments in a list
    read_terminal = sys.argv
    parser = argparse.ArgumentParser(prog='most_active_cookie.py', 
                                     description='Find the most active cookie on a particular date')
    parser.add_argument("file_path")
    parser.add_argument("date")
    # parses the command line and stores the arguments in a dictionary
    arguments = vars(parser.parse_args(read_terminal[1::2]))
    cookie_log_processor = CookieLogProcessor()
    cookie_log_processor.processFile(arguments['file_path'])
    print(cookie_log_processor.findMostActiveCookie(arguments['date']))