#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```

**Key points about this solution:**

1. **Tuple unpacking**: Python allows simultaneous assignment using `a, b = b, a`
2. **One line swap**: No need for a temporary variable
3. **Exactly 5 lines**: Meets the requirement of being exactly 5 lines long
4. **Line 4 insertion**: The swap code `a, b = b, a` is inserted at line 4 where the comment was

**How it works:**
- Python evaluates the right side `b, a` first, creating a tuple `(10, 89)`
- Then unpacks this tuple into `a` and `b` respectively
- Result: `a` becomes 10 and `b` becomes 89

**Output:**
```
a=10 - b=89
