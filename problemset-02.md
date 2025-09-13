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
 
2. Derive asymptotic upper bounds for each recurrence below, using a
   method of your choice.
   
  * $T(n)=2T(n/6)+1$
.  
.  
.  
.  
.  
  * $T(n)=6T(n/4)+n$
.  
.  
.  
.  
.  
  * $T(n)=7T(n/7)+n$
.  
.  
.  
.  
.  
  * $T(n)=9T(n/4)+n^2$
.  
.  
.  
.  
.  
  * $T(n)=4T(n/2)+n^3$
.  
.  
.  
.  
.  
  * $T(n)=49T(n/25)+n^{3/2}\log n$
.  
.  
.  
.  
.  
  * $T(n)=T(n-1)+2$
.  
.  
.  
.  
.  
  * $T(n)= T(n-1)+n^c$, with $c\geq 1$
.  
.  
.  
.  
.  
  * $T(n)=T(\sqrt{n})+1$
.  
.  
.  
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

.  
.  
.  
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

