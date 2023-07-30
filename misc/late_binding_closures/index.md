# Late Binding Closures

```{note}
forked from <https://docs.python-guide.org/writing/gotchas/#late-binding-closures>
```


Another common source of confusion is the way Python binds its variables in closures (or in the surrounding global scope).

**What You Wrote**

```python
def create_multipliers():
    return [lambda x : i * x for i in range(5)]
```

**What You Might Have Expected to Happen**

```python
for multiplier in create_multipliers():
    print(multiplier(2))
```

A list containing five functions that each have their own closed-over i variable that multiplies their argument, producing:

```python
0
2
4
6
8
```

**What Actually Happens**

```python
8
8
8
8
8
```

Five functions are created; instead all of them just multiply x by 4.

Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.

Here, whenever any of the returned functions are called, the value of i is looked up in the surrounding scope at call time. By then, the loop has completed and i is left with its final value of 4.

What’s particularly nasty about this gotcha is the seemingly prevalent misinformation that this has something to do with lambdas in Python. Functions created with a lambda expression are in no way special, and in fact the same exact behavior is exhibited by just using an ordinary def:

```python
def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append  (multiplier)

    return multipliers
```

**What You Should Do Instead**

The most general solution is arguably a bit of a hack. Due to Python’s aforementioned behavior concerning evaluating default arguments to functions (see Mutable Default Arguments), you can create a closure that binds immediately to its arguments by using a default arg like so:

```python
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]
```

Alternatively, you can use the functools.partial function:

```python
from functools import partial
from operator import mul

def create_multipliers():
    return [partial(mul, i) for i in range(5)]
```

**When the Gotcha Isn’t a Gotcha**

Sometimes you want your closures to behave this way. Late binding is good in lots of situations. Looping to create unique functions is unfortunately a case where they can cause hiccups.

