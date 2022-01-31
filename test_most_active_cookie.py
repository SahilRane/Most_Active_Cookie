import unittest
from most_active_cookie import CookieLogProcessor

class CookieLogProcessorTester(unittest.TestCase):
    def testWrongDate1(self):
        '''
        tests the case where the most active cookie is asked for on a date that is not mentioned in the log file
        test.csv
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2017-12-08')

        self.assertEqual(None, computed_cookies)

    def testWrongDate2(self):
        '''
        tests the case where the most active cookie is asked for on a date that is not mentioned in the log file
        test2.csv
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test2.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2017-12-08')

        self.assertEqual(None, computed_cookies)

    def testSingleCase1(self):
        '''
        tests a case where a date is given and there is only one such most active cookie on that date in 
        the file test.csv
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2018-12-09')
        solution = 'AtY0laUfhglK3lC7'
        self.assertEqual(solution, computed_cookies)
    
    def testSingleCase2(self):
        '''
        tests a case where a date is given and there is only one such most active cookie on that date in 
        the file test2.csv
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test2.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2017-12-09')
        solution = 'SAZuXPGUrfbcn5UA'
        self.assertEqual(solution, computed_cookies)

    def testMultipleCase1(self):
        '''
        tests a case where a date is given and there are multiple active cookies on that date in the test.csv file
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2018-12-08')
        solution = 'SAZuXPGUrfbcn5UA' + '\n' + '4sMM2LxV07bPJzwf' + '\n' + 'fbcn5UAVanZf6UtG'
        self.assertEqual(solution, computed_cookies)
    
    def testMultipleCase2(self):
        '''
        tests a case where a date is given and there are multiple active cookies on that date in the test2.csv file
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test2.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2018-12-09')
        solution = '5UAVanZf6UtGyKVS' + '\n' + 'AtY0laUfhglK3lC7' + '\n' + 'AtY0LaUfhglK3lC7'
        self.assertEqual(solution, computed_cookies)

    def testMultipleOnSameDayCase1(self):
        '''
        tests a case where a date is given and there are multiple active cookies on that date in the test.csv
        file but the frequency of each cookie on that day is more than 1.
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2016-12-08')
        solution = '4sMm2LxV07bPJzwf' + '\n' + '4sMM2LxV07bPJzwf' + '\n' + 'fbcn5UAVanZf6UtG'
        self.assertEqual(solution, computed_cookies)

    def testMultipleOnSameDayCase2(self):
        '''
        tests a case where a date is given and there are multiple active cookies on that date in the test2.csv
        file but the frequency of each cookie on that day is more than 1.
        '''
        cookie_log_processor = CookieLogProcessor()
        cookie_log_processor.processFile('test2.csv')
        computed_cookies = cookie_log_processor.findMostActiveCookie('2020-12-09')
        solution = '4sMM2LxV07bPJzwf' + '\n' + '5UAVanZf6UtGyKVS' + '\n' + 'AtY0laUfhglK3lC7' + '\n' + 'AtY0LaUfhglK3lC7'
        self.assertEqual(solution, computed_cookies)

if __name__ == '__main__':
    unittest.main()