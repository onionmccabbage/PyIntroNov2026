import itertools

# https://labex.io/tutorials/python-how-to-reset-python-generator-iteration-419666
def number_generator():
    yield from range(5)

## Create multiple independent iterators
gen1, gen2 = itertools.tee(number_generator())

print(list(gen1))  ## [0, 1, 2, 3, 4]
print(list(gen2))  ## [0, 1, 2, 3, 4]


# Best Practices
#     Prefer recreation for simple generators
#     Use itertools.tee() for parallel iterations
#     Implement custom caching for complex scenarios
