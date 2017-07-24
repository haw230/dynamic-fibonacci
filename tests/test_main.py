import sys

sys.path.insert(0, '/home/ubuntu/workspace/selection_sort') #for algorithm function (that the user will write)
sys.path.insert(0, '/home/ubuntu/workspace/solution') #for solution function
sys.path.insert(0, '/home/ubuntu//.virtualenvs/d/lib/python2.7/site-packages')

from main import selection_sort
from solution import solved_selection_sort 
import pytest
from delayed_assert import expect, assert_expectations

def test_answer():
    expect(selection_sort([1,3,4,2]) == solved_selection_sort([1,3,4,2]))
    expect(selection_sort([3,6,2,3,4]) == solved_selection_sort([3,6,2,3,4]))
    expect(selection_sort([3,4,2,12,43,5]) == solved_selection_sort([3,4,2,12,43,5]))
    assert_expectations()
    
#def test_simple():
#    assert(1) == 1
            
def main():
    test_answer()
    #test_simple()
    #hard_test()

if __name__ == '__main__':
    main()