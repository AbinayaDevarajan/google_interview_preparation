Google interview preparations:

Dynamic programming:
 - This is used only when  the problem can be broken in to multiple sub problems and if the sub problem results can be 
 used in order to solve the main problem 

 - The subproblems can be solved recursively 

 - If the problems can be solved by identifying and grouping repeated tasks 

 Three major approaches to solve this problem 

 1. Top Down approach: also known as the recursive approach where in recursion is used to solve repeated tasks.

 2. Top Down approach with memoization : this is called as caching , we cache the already computed subproblem results to ac hieve the results at faster speeds , trade off memory complexity.

 3. Bottom up approach: This is not a recursive methodology. usage of DAG's or tabulation method , the previously computed results are tabulated and used, we can used minimal number of variables or table to achieve this. memory can be reduced drastically than caching memoization method.

 --- NOTE that this algorithmic paradigm / techique  is only used to strictly avoid repetitive tasks and for optimizing the repeated tasks.


Two major properties of Dynamic programming:

1. Optimal substructure 
2. Overlapping Subsequence.


Overlapping subproblems:
------------------------

Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. ```So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again```

Optimal subproblem :
----------------------

https://en.wikipedia.org/wiki/Optimal_substructure


The problem can be solved by using the optimized versions of its sub problems.
Note if the sub-problems can be solved optimally then solving the main problem becomes trivial.
