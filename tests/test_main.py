import sys

sys.path.insert(0, '/home/ubuntu/workspace/linear_search') #for main.py
sys.path.insert(0, '/home/ubuntu/workspace/solution') #solved_search.py

from main import func
from solution import solved_algo
    
def simple_test():
    assert(func()) == solved_algo()
    assert(func()) == solved_algo()
    assert(func()) == solved_algo()
    
def rand_test():
    pass

def hard_test():
    pass
            
def main():
    simple_test()
    rand_test()
    hard_test()

if __name__ == '__main__':
    main()
