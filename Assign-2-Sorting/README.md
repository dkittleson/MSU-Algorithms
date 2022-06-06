### Coding directions

In this second assignment we will be implementing several common sorting
algorithms but with some slight variations. As with the first assignment, you'll
use assign02.py as a starting point and complete the functions from there. Of
course, you're free to implement new functions that can serve as helper
functions that can be called from the ones in assign02.py.  As with the earlier
assignment, we'll want to return the run time again so that we can compare their
performance. 

Note that you should remove/replace: 
  * any and all comments that are in ALL CAPS,
  * any instances of _pass_, and 
  * all other placeholder code/comments. 

It is probably most helpful to look at the starter code in assign02.py and then
to refer back to the directions below for any additional info needed. Also, be
sure to document your code properly by adding
[docstrings](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring).  In
addition to documentation, be sure that a reasonable coding style is followed as
well (e.g. two blank lines between functions). Your program will not pass the
first checks/tests if there is not proper documentation and styling.

### Functions to be implemented
* __bubbleSort(list_of_items)__ should sort items in list_of_items in ascending order
* __mergeSort(list_of_items, split_by_3=False)__ should sort items in list_of_items in ascending order
* __quickSort(list_of_items, pivot_to_use='first')__ should sort items in list_of_items in ascending order
* __radixSort(list_of_items)__ should sort items in list_of_items in ascending order

Note that there are essentially two version of mergeSort() and two versions of
quickSort() that need to be implemented. The reason is that we want to
understand how mergeSort behaves when we split by 3 (rather than 2), and how
the choice of the pivot location in quickSort affects runtime for different
types of input lists (e.g. shuffled vs sorted in reverse). 

The above functions should return a tuple containing two elements, namely:
1. a `list` with all the items from the input list now in ascending sorted order
2. a `float` representing number of seconds needed to sort the items
