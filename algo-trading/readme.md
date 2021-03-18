# 2021 Algorithmic Trading

It has been shown with a high correlation that turning memes into integers, and ordering them chronologically gives you data that you can predict the value of GameStop stock with 70% confidence. Every meme gives a value indicating how many memes forward you can jump. You must move chronologically. Once you have the shortest path through all of the memes, you can use this information to put memes into google reverse image search. If there is more green than red, you invest now. If there is more red than green, you hold. If there is an equal amount of green and red, you have hit the lotto, you should sell your home and buy call options.

## Description

Given all the values of memes in chronological order. Then the corresponding meme names, find the path of memes `A->B->C->D` such that you take the shortest path to Gamestop riches.

## Input
 
You will receive an integer `n` that will correspond to the number of memes you will receive on the first line. You will then receive the meme's value `v_i` space delimitted on the same line. Then you will receive the meme names. Meme names will be in the regex `[A-z]*` and have length less than or equal to 15 ascii characters.

```
n
v_1 v_2 v_3 ... v_n
m_1 m_2 m_3 ... m_n
```

## Constraints

$$1 \leq n \leq 500000$$

$$1 \leq v_i \leq 100$$

$$m_i \in [A-z]\*$$

## Output

```
p_1 p_2 ... p_k
```

Where you can legally jump from $$p_1$$->$$p_2$$->...$$p_k$$, where $$p_k = m_n$$.


### Disclaimer

This is not a financial strategy, advice, or anything more than a problem statement for the USC Codeathon.
