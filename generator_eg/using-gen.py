# Ways to build efficient range-like objects
import itertools
# NB the reason itertools is so fast id it is written in C !!!!

# this one keeps returning 0-9
g = ( i%10 for i in range(10,51) ) # instead of 50, use a really big number
for _ in g:
    print(_)

# here we use itertools for an infinite loop
for i in itertools.count():
    if i>10:
        break
    print(i)

## Create multiple independent iterators (up to two identical generators)
gen1, gen2 = itertools.tee(i**2 for i in range(0,10))

print(list(gen1))  ## [0, 1, 2, 3, 4]
print(list(gen2))  ## [0, 1, 2, 3, 4]


# Best Practices
#     Prefer recreation for simple generators
#     Use itertools.tee() for parallel iterations
#     Implement custom caching for complex scenarios
