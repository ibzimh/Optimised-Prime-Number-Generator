# Optimised-Prime-Number-Generator

Testing different prime number generator algorithms and primality tests. (Under Construction)

$$\pi$$

Let $\mathit{\Pi} = \prod_{i=1}^{k}{p_{i}^{\delta_{i}}}$ be the $n$-bit product of the first $k$ primes with some small exponents $\delta_{i}$, and let $\Delta = \textrm{max}_{i}\delta_{i}$. We denote by $x = ( x_{1},\dots,x_{k} ) _{\equiv}$ the modular representation of $x \in \mathbb{Z}_{\mathit{\Pi}}$, i.e., $x_{i} = x \bmod \ p_{i}^{\delta_{i}}$. For $i = 1, \dots, k$, one then defines  $\theta_{i} = (0, \dots, 1, \dots, 0)_{\equiv}$ where the "$1$" stands for the $i^{\text{th}}$ position. It is obvious to see that we always have:
$$\forall x \in \mathbb{Z}_{\mathit{\Pi}}\qquad x = \sum_{i=1}^{k}x_{i} \theta_{i} \bmod{\mathit{\Pi}}$$ 
[some proof/reasoning here for the calculations below]
$$\begin{align}\forall x \in \mathbb{Z}_{\mathit{\Pi}} \qquad \forall x \in \mathbb{Z}^{*}_{\mathit{\Pi}} 
&\Longleftrightarrow x_{i} \in \mathbb{Z}^{*}_{p_{i}^{\delta_{i}}} \\
&\Longleftrightarrow x_{i}^{\delta_{i}} \not\equiv 0 \pmod{ p_{i}^{\delta_{i}}} \\
&\Longleftrightarrow x_{i}^{\delta_{i}} \theta_{i} \not\equiv 0 \pmod{\mathit{\Pi}} \;\text{for $i = 1, \dots, k$}
\end{align}$$ 
