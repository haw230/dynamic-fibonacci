# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '/home/ubuntu/workspace/dynamic_fibonacci') #change this to correct folder name
sys.path.insert(0, '/home/ubuntu/workspace/solution')

from main import fib #change to proper function name
from solution import solved_fib #change to proper function name
from time import sleep
from random import sample

class aethetics(object):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    LINE = '\033[95m———————————————————————————————————————————————————————————————\033[0m'

class TestCases(object):
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0

    def tests(self): #add tests here
        f1,f2 = fib, solved_fib #change to proper function names
        self.test(f1, f2, 4)
        self.test(f1, f2, 5)
        self.test(f1, f2, 6)
        self.test(f1, f2, 7)
        self.test(f1, f2, 8)
        self.test(f1, f2, 9)
        self.test(f1, f2, 30)
        self.test(f1, f2, 60)
    
    def test(self, func1, func2, n):
        x, y = func1(n), func2(n)
        if(x == y):
            print(aethetics.GREEN + 'Test passed with param of ' + aethetics.BLUE + str(n) + aethetics.END + '\n' + aethetics.END)
            print(aethetics.BOLD + str(x) + aethetics.END + ' matches the answer ' + aethetics.BOLD + str(y) + aethetics.END)
            self.passed_tests += 1
        else:
            print(aethetics.FAIL + 'Test failed with param of ' + aethetics.BLUE + str(n) + aethetics.END + '\n' + aethetics.END)
            print(aethetics.BOLD + str(x) + aethetics.END + ' does not match the answer ' + aethetics.BOLD + str(y) + aethetics.END)
        self.total_tests += 1
        print(aethetics.LINE + '\n')
        sleep(0.7)
        
    def end(self):
        if(self.passed_tests == self.total_tests):
            print(aethetics.GREEN + 'All ' + str(self.total_tests) + ' tests passed.' + aethetics.END)
        else:
            print(aethetics.WARNING + 'Passed ' +  str(self.passed_tests) + ' of ' + str(self.total_tests) + ' tests.' + aethetics.END)

if(__name__ == '__main__'):
    print('\n' + aethetics.GREEN + "Running Tests..." + aethetics.END)
    print(aethetics.LINE + '\n')
    t = TestCases()
    t.tests()
    t.end()