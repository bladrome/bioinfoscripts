# Entropy Shifts of Abundance Vectors under Boolean Operations (ESABO)
[ESABO](Boolean analysis reveals systematic interactions among low-abundance species in the human gut microbiome)

## Algorithm
Propose a novel analysis method based on Boolean operations applied to microbial co-occurrence patterns in low aboundance species.
The interaction bewteen two species is expected to be seen in ESABO score.
**steps**:
1. Give two low aboundance vectors $a$ and $b$ of two species.
2. Binarize $a$ and $b$.
3. Let $c$ = $a$ OP $b$(OP could be a boolean operation, maybe AND).
4. Calculate 
$$p_{0} = \frac{|0|}{|a|}$$ 
$$p_{1} = \frac{|0|}{|a|}$$
and **entropy**:
$$x = -\sum{p_0ln(p_0) + p_1ln(p_1)}$$
5. Reshuffle binary vector $b$, calculate a series of entropies named $y$, $y = {y_1, y_2, \cdots, y_n}, n$ is shuffle tiems.
6. ESABO score is defined as the $z-score$ of $x$:
$$ ESABO\ score = \frac{x-mean(y)}{stardard\ deviation\ of\ y}$$


## Data
- aboundance: 
9 samples x 17 species


## Source code
- esabo: method prototype
    functions:
    - esabo:Given a binary aoundance matrix, return the esabo matrix
    - esabo\_jaccardindex:Given a binary aboundance matrix, return the entropy matrix of jaccard index


## Run
```sh
python esabo.py
```
for details: read the code.
