# Price Movements

You are given the price movements of some security. Find the number of 3 length *strictly* decreasing subsequences that can be made from elements of the sequence(order preserving).

## Description

Given the price movements in chronological order, find how many decreasing subsequences of length 3. As in, $a_i < a_j < a_k$ where $i < j < k$.

## Input
 
You will receive an integer `n` that will correspond to the number of price movements you will receive on the first line. You will then receive the price movements `a_i` in order delimitted by spaces.


```
n
a_1 a_2 a_3 ... a_n
```

## Constraints

$$1 \leq n \leq 10000$$

$$-2^20 \leq a_i \leq 2^20$$

## Output

```
x
```

Where `x` is the number of decreasing subsequences of length 3.