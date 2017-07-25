# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '/home/ubuntu/workspace/selection_sort') #main.py
sys.path.insert(0, '/home/ubuntu/workspace/solution') #solution.py

from main import selection_sort
from solution import solved_selection_sort
from time import sleep



class aethetics(object): #https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m' #yellow
    FAIL = '\033[91m' #red
    END = '\033[0m' #must put at the end of every LINE
    BOLD = '\033[1m'
    LINE = '———————————————————————————————————————————————————————————————'

class test_cases(object):
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0

    def tests(self): #add tests here
        self.test(selection_sort, solved_selection_sort, [1, 3, 2])
        self.test(selection_sort, solved_selection_sort, [1, 2, 3])
        self.test(selection_sort, solved_selection_sort, [3, 2, 1])
    
    def test(self, func1, func2, ls):
        ls1 = list(ls)
        x, y = func1(ls), func2(ls1)
        if(x == y):
            print(aethetics.GREEN + 'Test passed with param of ' + aethetics.BLUE + str(ls) + aethetics.END + '\n' + aethetics.END)
            print(aethetics.BOLD + str(x) + aethetics.END + ' matches the answer ' + aethetics.BOLD + str(Y) + aethetics.END)
            self.passed_tests += 1
        else:
            print(aethetics.FAIL + 'Test failed with param of ' + aethetics.BLUE + str(ls) + aethetics.END + '\n' + aethetics.END)
            print(aethetics.BOLD + str(x) + aethetics.END + ' does not match the answer ' + aethetics.BOLD + str(y) + aethetics.END)
        self.total_tests += 1
        print(aethetics.LINE + '\n')
        sleep(0.6)
        
    def end(self):
        if(self.passed_tests == self.total_tests):
            print(aethetics.GREEN + 'All ' + str(self.total_tests) + ' tests passed.' + aethetics.END)
        else:
            print(aethetics.WARNING + 'Passed ' +  str(self.passed_tests) + ' of ' + str(self.total_tests) + ' tests.' + aethetics.END)

if __name__ == '__main__':
    print('\n' + aethetics.GREEN + "Running Tests..."  + '\n' + aethetics.END)
    t = test_cases()
    t.tests()
    t.end()