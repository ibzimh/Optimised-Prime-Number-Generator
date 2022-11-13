# Optimised-Prime-Number-Generator

What is the difference between the Optimised Generator and the Classical Generator? <br />

(the markdown in brackets, i.e., (`name`) refer to the variable name in the code) <br />

We try to minimise 'randomly' guessing candidates (c) for primes by selecting numbers with certain prime-like properties. <br />

$\delta$ (`delta`) is a sequence of small exponents, $p$ (`p`) is a sequence of small prime numbers, $t = C \cdot max | \ p_{i}^{\delta_{i}} |$ (`t`, `C`), $\alpha$ is a sequence of sequences (`alfi`) of random numbers and $\theta$ (`theta`) is a sequence of $\theta_{i}$'s (`theti`)  which are sequences of $0$'s with a $1$ at the $i^{\text{th}}$ position.

$$ \mathit{\Pi} = \prod_{i=1}^{k}{p_{i}^{\delta_{i}}} $$

$$ ( \alpha_{i}^{\delta_{i}} \cdot \theta_{i} \ ( \mathrm{mod} ) \ \mathit{\Pi} \neq 0 ) \ \longrightarrow \ c = 
\sum^{n} _ {i=1}{\alpha_{i}^{\delta_{i}} \cdot \theta_{i} \ ( \mathrm{mod} ) \ \mathit{\Pi}} \{  \}$$ 

Where $c$ is an invertible number modulo $\mathit{\Pi}$ <br />

(This is as a result of the Chinese Remainder Theorem)

Now, like the classical generators, we generate $c$'s until we find a prime. (To be updated). <br />

Files: <br />

Naive Generator - Naive/Basic Implementation of Prime Number Generator <br />
Classical Generator - Using some basic Number Theory theorems to make improvements to the Naive Generator <br />
Optimised Generator - Using further number theory concepts to minimise random guessing and maximise accuracy <br />
Composite Test - Miller-Rabin Deterministic Composite Test (more tests to be added soon!) <br />
PrimeHelpers - List of functions to used in the generators. <br />
HelperFunctions - List of useful array (and non-array) functions to avoid redundancy and make code cleaner <br />

Misc. Files: <br />
Primes1.txt - List of primes up until $2^{23}$ <br />
MakeListOfPrimes - Imports Primes.txt <br />
CodeDump - Temporary local repository of the code. <br />
