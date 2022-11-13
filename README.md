# Optimised-Prime-Number-Generator

Testing different prime number generator algorithms and primality tests. (Under Construction)

Naive Generator - Naive/Basic Implementation of Prime Number Generator <br />
Classical Generator - Using some basic Number Theory theorems to make improvements to the Naive Generator <br />
Optimised Generator - Using further number theory concepts to minimise random guessing and maximise accuracy <br />
Composite Test - Miller-Rabin Deterministic Composite Test (more tests to be added soon!) <br />
PrimeHelpers - List of functions to used in the generators. <br />
HelperFunctions - List of useful array (and non-array) functions to avoid redundancy and make code cleaner <br />

$\delta_{i}$ (named `delta` in the code) is a sequence of small exponents, $p_{i}$ is a sequence of small prime numbers, and $t = C \cdot max | \ p_{i}^{\delta_{i}} \ | and $\theta$ is a sequence of $\theta_{i}$'s where each $\theta_{i}$ is a sequence of $0$'s with a $1$ at the $i^{\text{th}}$ position.

$$\mathit{\Pi} = \prod_{i=1}^{k}{p_{i}^{\delta_{i}}}$$ 

Misc.: <br />
Primes1.txt - List of primes up until $2^{23}$ <br />
MakeListOfPrimes - Imports Primes.txt <br />
CodeDump - Temporary local repository of the code. <br />
