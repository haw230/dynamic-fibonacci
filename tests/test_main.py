import sys

sys.path.insert(0, '/home/ubuntu/workspace/algorithm-name') #for algorithm function (that the user will write)
sys.path.insert(0, '/home/ubuntu/workspace/solution') #for solution function

from main import func #"func" is user written function
from solution import solved_algo #"solved_algo" is solution for problem
    
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
