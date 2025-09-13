# CMPS 6610 Problem Set 02

**Name:**_ Aaron Dumont________________________

In this assignment we'll work on applying the methods we've learned to
analyze recurrences, and also see their behavior in practice. As with
previous assignments, some of of your answers will go in
`main.py`. Please add your written answers to `answers.md` which you can convert
to a PDF using `convert.sh`. Alternatively, you may scan and upload written answers
to a file named `answers.pdf`. 


1. Prove that $\log n! \in \Theta(n \log n).$

We must show that $log(n!)$ is bounded above and below by a constant multiple of $nlogn$ for sufficiently large $n$.

$(n!)$ = $n$ * $(n-1)$ * $(n-2)$ *...* $2$ * $1$

$log(n!)$ = $log$($n$ * $(n-1)$ * $(n-2)$ *...* $2$ * $1$)

$log(n!)$ = $log(n)$ + $log(n-1)$ + $log(n-2)$ +...+ $log2$ + $log1$

or rearranging: $log(n!)$ = $log1$ + $log2$ +...+$log(n-2)$ + $log(n-1)$ + $log(n)$

This can be expressed as a summation:
$$
log(n!) = \sum_{i=1}^{n} log(i)
$$

1. Proof of the Upper Bound: $log(n!) \in O(nlogn)$

We must prove $log(n!) \le c * nlogn$ for some constant $c > 0$ and for all $n \ge n_0$

Looking at the summation above, each term $log(i)$ is $\le$ the largest term which is $log(n)$

ie. $log(i) \le log(n)$ for all $i$ from 1 to $n$. Hence, we can establish an upper bound by replacing every term in the sum with $log(n)$:
$$
\sum_{i=1}^{n} log(i) \le \sum_{i=1}^{n} log(n)
$$
Note: The summation below is the same as adding $log(n)$ to itself $n$ times and hence = $nlogn$
$$
\sum_{i=1}^{n} log(n) = n\cdot logn
$$

Therefore we have: $log(n!) \le nlogn$. This fits the definition of Big-O with $c=1$ and $n_0=1$ which therefore proves $log(n!) \in O(nlogn)$.

2. Proof of the Lower Bound: $log(n!) \in \Omega(nlogn)$

We must prove $log(n!) \ge c * nlogn$ for some constant $c > 0$ and for all $n \ge n_0$.

$$
log(n!) = \sum_{i=1}^{n} log(i) = log(1) + ... +log(\frac{n}{4}) +...+ log(n)
$$

The first half of the terms (from $i=1$ to $i=n/2$) is smaller than the second half. To find the lower bound, we can ignore the first half of the terms.

$$
\sum_{i=1}^{n} log(i) \ge \sum_{i=n/2}^{n} log(n)
$$

The smallest value on the right will be $log(\frac{n}{2})$.

$log(i) \ge log(\frac{n}{2})$ for all $i$ from $\frac{n}{2}$ to $n$.

Moreover, the the number of terms in the sum from $i=\frac{n}{2}$ to $n$ is ($n-\frac{n}{2}$) + $1$ = $\frac{n}{2} + 1$ which is greater than $\frac{n}{2}$.

We can use the above now such that the smallest value is $log(\frac{n}{2})$ and there are at least $\frac{n}{2}$ terms:
$$
\sum_{i=1}^{n} log(i) \ge \sum_{i=n/2}^{n} log(n) \ge n/2 *log(\frac{n}{2}) = \frac{n}{2}(log(n) - log(2)) = \frac{n}{2}\cdot log(n) - \frac{n}{2}\cdot log(2)
$$

$log(n!) \ge c * nlogn$ for some constant $c > 0$ and for all $n \ge n_0$.

If we set $n \ge 4$ and take the log of both sides:
$log(n) \ge log(4) = 2log(2)$

We divide both sides by 2: $\frac{1}{2}log(n) \ge log(2)$

We can now substitute back into $(\frac{n}{2})\cdot log(n) - (\frac{n}{2})\cdot log(2) \ge (\frac{n}{2})log(n) - (\frac{n}{2})((\frac{1}{2})log(n))$ = $(\frac{n}{4})log(n)$ = $(\frac{1}{4})n \cdot log(n)$

Therefore we have shown that $log(n!) \ge (\frac{1}{4})n \cdot log(n)$ with $c=\frac{1}{4}$ and $n_0 = 4$.

. 
. 
 
2. Derive asymptotic upper bounds for each recurrence below, using a
   method of your choice.
   
  * $T(n)=2T(n/6)+1$

  $C_(root) = 1$

  $C_(level1) = 2 \cdot 1$ = 2 [2 subproblems at cost of 1 each]

  Therefore, this is leaf dominated and cost is upper bounded by the number of leaves at unit cost 1.

  #leaves = c

  Therefore, **$T(n) = O(n^{(log_62)})$**

. 
.  

  * $T(n)=6T(n/4)+n$
$C_(root) = n$

$C_(level1) = 6 \cdot f(\frac{n}{4}) = 6 \cdot n/4$ = $\frac{3}{2}n$

Therefore this is leaf dominated and cost is upper bounded by the number of leaves.

#leaves = $a^{log_b(n))} = n^{(log_b(a))} = n^{(log_46)}$

Therefore, **$T(n) = O(n^{log_46})$**
 
. 
. 

  * $T(n)=7T(n/7)+n$

$C_(root) = n$

$C_(level1) = 7(\frac{n}{7}) = n$

Cost is same at each level, therefore this is balanced.

Depth = $log_bn = log_7n$. Average cost per level is $n$.
Total cost = depth * average cost per level = $log_7n$ * $n$.
Therefore, $T(n) = O($nlog_7n$)

. 
. 

  * $T(n)=9T(n/4)+n^2$

  $C_(root) = n^2$

  $C_(level 1) = 9(\frac{n}{4})^2 = \frac {9}{16}n^2$ [cost decreased by factor of 9/16]

  Therefore, this is root dominated. **$T(n) = O(n^2)$**

. 
. 

  * $T(n)=4T(n/2)+n^3$

  $C(root) = n^3$

  $C(level1) = 4 \cdot (\frac{n}{2}^3) = \frac{4}{8} n^3 = \frac{1}{2}n^3$ [cost decreased by a factor of 1/2]

  Therefore, this is root dominated. **$T(n) = O(n^3)$**

. 
. 

  * $T(n)=49T(n/25)+n^{3/2}\log n$

$C_(root) = n^{3/2}\log n$
$C_(level1) = 49 \cdot (\frac{n}{25}^{3/2} \cdot log(\frac{n}{25})) = \frac{49}{125} \cdot n^{3/2} \cdot (logn - log25))$ [This is less geometrically less than the root]

Therefore this is root-dominated. **$T(n) = O(n^{3/2}\log n)$

. 
.

  * $T(n)=T(n-1)+2$

This is not a "divde and conquer" recurrence, so the tree is a single long branch.

$C_(root) = 2$

$C_(level1) = 2$

This is a balanced recurrence.

The problem size decreases by 1 each step. $n, n-1, n-2, ... , 1$. Therefore the total number of calls (bricks) is n.

The cost per level is 2. Total cost = $2n + C$ where $C$ is the constant cost of each base case.

Therefore, **$T(n) = O(n)$**

. 
.

  * $T(n)= T(n-1)+n^c$, with $c\geq 1$

$C_(root) = n^c$

$C_(level1) = (n-1)^c$

The work at each level is quite consistent, on the order of $O(n^c)$.

The number of levels or depth: The problem goes from $n$ to $n-1$ ... $1$ so there are n levels.

So the total Cost, $C$, = $O(n^c \cdot n^1)$ = **$O(n^{c+1})$**

. 
.

  * $T(n)=T(\sqrt{n})+1$

$C_(root) = 1

$C_(level1) = 1

Therefore this recurrence is balanced with a work of 1 at each level.

The problem size goes from $n$ to $n^{\frac{1}{2}}$ to $n^{\frac{1}{4}}$...So that at any general level k, the problem size is $n^{\frac{1}{2^k}}$. The recursion stops when the problem size is reduced to a base case, for example 2. We need to find the depth where this occurs.

$n^{\frac{1}{2^k}} = 2$. We can then take $log_2$ of both sides.

$log_2n^{\frac{1}{2^k}} = log_22$

${\frac{1}{2^k}}log_2(n) = 1$

$2^k = log_2(n)$. We need to solve for k so take log_2 of both sides.

$k = log_2log_2(n)$

Now total work is the sum of the work at all levels. Cost at each level is 1 and number of levels = $k$.

Therefore $T(n)=T(\sqrt{n})+1 = O(1 \cdot log_2log_2(n)) = O(log_2log_2(n))$

. 
.


3. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      two subproblems of one fifth of the input size, recursively
      solving each subproblem, and then combining the solutions in quadratic time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively one subproblems of size $n-1$ and then
      combining the solutions in logarithmic time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into a subproblems of size $n/3$ and a subproblem of size
      $2n/3$, recursively solving each subproblem, and then combining
      the solutions in $O(n^{1.1})$ time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions
    (i.e. the non-recursive quantity).
    Which algorithm would you choose? Why?

Algorithm $\mathcal{A}$:

$W_A(n) = 2W_A(n/5) + n^2$

$C_(root) = n^2$

$C_(level1) = 2(n/5)^2 = \frac{2}{25} \cdot n^2$

Therefore this is root dominated. $W_A(n) = O(n^2)$

Span: The recursive calls can be run in parallel, so we can account for the longest one plus the time to combine:

$S_A(n) = S_A(n/5) + O(n^2)$

$C_(root) = n^2$

$C_(level1) = (n/5)^2 = \frac{1}{25} \cdot n^2$

Therefore this is root dominated. $S_A(n) = O(n^2)$

. 
.

Algorithm $\mathcal{B}$:

$W_B(n) = W_B(n-1) + logn$

$C_(root) = logn$

$C_(level1) = log(n-1)$

The work is not geometrically changing and this is therfore a balanced recurrence.

There are $n$ levels ($n$ to $n-1$ ... $1$) with a cost at each level on the order of $logn$.

Therefore total work is: $W_B(n) = O(nlogn)$

Span: For the recursive calls, there is only one subproblem ($S_B(n-1)$) so nothing to run in parallel. So the work and span should be the same.

$S_B(n) = S_B(n-1) + logn$

$S_B(n) = O(nlogn)$

. 
.

Algorithm $\mathcal{C}$:

$W_C(n) = W_C(n/3) + W_C(2n/3) + n^{1.1}$

$C_(root) = n^{1.1}$

$C_(level1) = (n/3)^{1.1} + (2n/3)^{1.1}$

It appears that the work is geometrically decreasing (level one would be 0.897 the size of the root for example).

Therefore the work is asymptotically equivalent to the work of the root: $W_C(n) = O(n^{1.1})$.

Span: The two subproblems will run in parallel but the longest path will be determined by the $(2n/3)$ subproblem.

Hence: $S_C(n) = S_c(2n/3) + n^{1.1}$. This is also root dominated so $S_c(n) = O(n^{1.1})$

I would choose alogrithm $\mathcal{B}$ as its work and span are both polylogarithmic functions and will be asymptotically dominated by the polynomial work and span functions of algorithms $\mathcal{A}$ and $\mathcal{B}$. Work is more important than span overall, but from both work and span perspectives, algorithm $\mathcal{B}$ is superior.

. 
.


4. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions (i.e.,
    the non-recursive quantity). Which algorithm would you choose? Why?

.  
.  
.  
.  
.  


5. In Module 2 we discussed two algoriths for integer multiplication. The
  first algorithm was simply a recapitulation of the "grade school"
  algorithm for integer multiplication, while the second was the
  Karatsaba-Ofman algorithm. For this problem, you will use the stub
  functions in `main.py` to implement these two algorithms for integer
  multiplication. Once you've correctly implemented them, test the
  empirical running times across a variety of inputs to test whether
  your code scales in the manner predicted by our analyses of the
  asymptotic work.


.  
.  
.  
.  
.  



6. A "white hat" conducts hacking activities for the common good, while a
"black hat" hacker does so for nefarious reasons. Let's consider a
computer security class with $n$ students who are all either white hat
or black hat hackers. You're the instructor, and you don't know who is
a white hat or a black hat, but all of the student do. 

Your goal is to identify the white hats and you're allowed to ask a
pair of students about one another. White hats will always tell the
truth, but you cannot trust a black hat's response. For a pair of students $A$ and
$B$ then there are several possible outcomes:


|$A$ says | $B$ says | Conclusion |
|---------|----------|------------|
|$B$ is a white hat | $A$ is a white hat | both are good, or both are bad |
|$B$ is a white hat | $A$ is a black hat | at least one is bad |
|$B$ is a black hat | $A$ is a white hat | at least one is bad |
|$B$ is a black hat | $A$ is a black hat | at least one is bad |

*6a.* Show that if more than $n/2$ students are black hats, you cannot determine which students are white hats based on a pairwise test. Note that you must assume the black hats are conspiring to fool you.


*6b.* Consider the problem of finding a single white hat, assuming strictly more than $n/2$ of the students are white hats. Show that $n/2$ pairwise interviews is enough to reduce the problem size by a constant fraction. 


*6c.* Using the above show that all white hats can be identified using $\Theta(n)$ pairwise interviews.

