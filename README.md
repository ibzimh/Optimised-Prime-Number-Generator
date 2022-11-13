# Optimised-Prime-Number-Generator

Testing different prime number generator algorithms and primality tests. (Under Construction)

Naive Generator - Naive/Basic Implementation of Prime Number Generator <br />
Classical Generator - Using some basic Number Theory theorems to make improvements to the Naive Generator <br />
Optimised Generator - Using further number theory concepts to minimise random guessing and maximise accuracy <br />
Composite Test - Miller-Rabin Deterministic Composite Test (more tests to be added soon!) <br />
PrimeHelpers - List of functions to used in the generators. <br />
HelperFunctions - List of useful array (and non-array) functions to avoid redundancy and make code cleaner <br />

the markdown in brackets, i.e., (`name`) refer to the variable name in the code <br />

To minimise random guessing we select numbers with certain prime-like properties. <br />

$\delta$ (`delta`) is a sequence of small exponents, $p$ (`p`) is a sequence of small prime numbers, $t = C \cdot max | \ p_{i}^{\delta_{i}} |$ (`t`, `C`), $\alpha$ is a sequence of sequences (`alfi`) of random numbers and $\theta$ (`theta`) is a sequence of $\theta_{i}$'s (`theti`)  which are sequences of $0$'s with a $1$ at the $i^{\text{th}}$ position.

$$\mathit{\Pi} = \prod_{i=1}^{k}{p_{i}^{\delta_{i}}}$$ (`prod`) 
\mathit{\Pi} = \prod_{i=1}^{k}{ \alpha_{i}^{\delta_{i}} \ \theta_{i} }$$

Misc.: <br />
Primes1.txt - List of primes up until $2^{23}$ <br />
MakeListOfPrimes - Imports Primes.txt <br />
CodeDump - Temporary local repository of the code. <br />
