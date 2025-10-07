<div align="center">
	<h1>42 Data Science Pool — Python Kickstart</h1>
	<p><em>A journey through essential Python concepts and exercises</em></p>
</div>

---

## 🏁 Introduction

Welcome to my 42 Data Science Pool! This repository contains a series of beginner-friendly Python exercises designed to build a strong foundation in programming. Each exercise focuses on a specific concept, from basic data types to custom functions and package creation. Below, you'll find a summary of each exercise, its goal, and a brief explanation of my solution.

---

## 📚 Exercises Overview


### ex00 — Hello.py
**Goal:** Manipulate basic Python data structures (list, tuple, set, dict) and update their values.

**How it works:**

#### List
A list is a mutable sequence of elements. You can change its contents:

```python
ft_list = ["Hello", "tata!"]
ft_list[1] = "World!"  # Changes second element
```

<pre>
Index:   0       1
		 ↓       ↓
ft_list: ["Hello", "World!"]
</pre>

#### Tuple
A tuple is an immutable sequence. You cannot change elements directly, but you can create a new tuple:

```python
ft_tuple = ("Hello", "toto!")
ft_tuple = (ft_tuple[0], "France!")  # Creates a new tuple
```

<pre>
Index:    0        1
		  ↓        ↓
ft_tuple: ("Hello", "France!")
</pre>

#### Set
A set is an unordered collection of unique elements. You can add or remove items:

```python
ft_set = {"Hello", "tutu!"}
ft_set.remove("tutu!")
ft_set.add("Paris!")
```

<pre>
ft_set: {"Hello", "Paris!"}
</pre>

#### Dictionary
A dictionary maps keys to values. You can update values by key:

```python
ft_dict = {"Hello": "titi!"}
ft_dict["Hello"] = "42Paris!"
```

<pre>
Key      Value
----     ---------
"Hello"  "42Paris!"
</pre>

**What I did:**
- Created and modified each data type, showing how to update and print their contents.
- Used print statements to display the final state of each structure.

---

### ex01 — format_ft_time.py
**Goal:** Work with the `time` module, format timestamps, and display time in different representations.

**How it works:**

#### Time Formatting
The program gets the current time in seconds since January 1, 1970 (the Unix epoch):

```python
secs = ft_time.time()
int_part = int(secs)
frac_part = secs - int_part
formatted = f"{int_part:,}" + f"{frac_part:.5f}"[1:]
```

<pre>
Example:
Seconds: 1,695,000,123.12345
Scientific: 1.7e+09
</pre>

It also prints the current date in a readable format:

<pre>
Date: Oct 07 2025
</pre>

**What I did:**
- Fetched and formatted the current time, showing both standard and scientific notation.
- Printed the current date using the time module.

---

### ex02 — find_ft_type.py
**Goal:** Identify the type of a given object and print a custom message based on its type.

**How it works:**

#### Type Checking
The function checks the type of the input object and prints a message:

```python
type_map = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict", str: "String"}
for t, name in type_map.items():
	if isinstance(obj, t):
		print(f"{name} : {t}")
```

<pre>
Input: [1, 2, 3] → List : <class 'list'>
Input: "hello" → hello is in the kitchen : <class 'str'>
</pre>

**What I did:**
- Used a type map to identify and print the type of the input object.
- Provided custom messages for strings and other types.

---

### ex03 — NULL_not_found.py
**Goal:** Recognize and print special values (None, nan, False, 0, empty string) with custom messages.

**How it works:**

#### Special Value Detection
The function matches the input against special values and prints a message:

```python
type_map = {type(None): "Nothing : None", float: "Cheese: nan", bool: "Fake: False", int: "Zero: 0", str: "Empty: "}
```

<pre>
Input: None → Nothing : None
Input: float('nan') → Cheese: nan
Input: False → Fake: False
Input: 0 → Zero: 0
Input: "" → Empty:
</pre>

**What I did:**
- Checked for special values and printed a custom message for each.
- Handled edge cases like `nan` and empty strings.

---

### ex04 — whatis.py
**Goal:** Accept a command-line argument, check if it's an integer, and print whether it's even or odd.

**How it works:**

#### Argument Validation & Parity Check
The program checks if the input is a valid integer and determines its parity:

```python
if arg.lstrip("+-").isdigit():
	num = int(arg)
	if num % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
```

<pre>
Input: 4 → I'm Even.
Input: 7 → I'm Odd.
Input: "abc" → AssertionError: argument is not an integer
</pre>

**What I did:**
- Validated the input and checked for integer type.
- Printed whether the number is even or odd, with error handling for invalid input.

---

### ex05 — building.py
**Goal:** Analyze a text and count uppercase, lowercase, punctuation, spaces, and digits.

**How it works:**

#### Character Statistics
The program counts different types of characters in a string:

```python
print(str(sum(1 for c in text if c.isupper())) + " upper letters")
print(str(sum(1 for c in text if c.islower())) + " lower letters")
print(str(sum(1 for c in text if c in ".,;:!?\"'")) + " punctuation marks")
print(str(sum(1 for c in text if c.isspace())) + " spaces")
print(str(sum(1 for c in text if c.isdigit())) + " digits")
```

<pre>
Text: "Hello, World! 42"
Output:
The text contains 15 characters:
2 upper letters
8 lower letters
2 punctuation marks
2 spaces
2 digits
</pre>

**What I did:**
- Counted and printed statistics for each character type in the input text.
- Supported both command-line and standard input.

---

### ex06 — filterstring.py & ft_filter.py
**Goal:** Filter words longer than a given length using a custom filter function.

**How it works:**

#### Custom Filter Function
`ft_filter` mimics Python's built-in `filter`:

```python
def ft_filter(function, iterable):
	return (item for item in iterable if function(item))
```

Used to filter words:

```python
result = list(ft_filter(lambda w: len(w) > n, words))
```

<pre>
Input: "hello world 42", n=4 → ['hello', 'world']
</pre>

**What I did:**
- Implemented a custom filter and used it to select words longer than a given length.

---

### ex07 — sos.py
**Goal:** Convert a string to Morse code, handling special characters and providing intelligent fallbacks.

**How it works:**

#### Morse Code Encoding
The program maps each character to Morse code, normalizing special letters:

```python
NESTED_MORSE = {"A": ".-", ...}
for c in text.upper():
	c = normalize_char(c)
	if c in NESTED_MORSE:
		morse.append(NESTED_MORSE[c])
```

<pre>
Input: "SOS 42" → ... --- ... / ....- ..---
</pre>

**What I did:**
- Encoded input text to Morse code, handling special characters and errors.

---

### ex08 — Loading.py
**Goal:** Create a custom progress bar (like `tqdm`) for iterating over a range.

**How it works:**

#### Progress Bar Visualization
The function displays a progress bar as items are processed:

```python
for i, item in enumerate(lst):
	pct = int((i + 1) * 100 / total)
	# Print colored bar
```

<pre>
Progress: [█████-----] 50% | 5/10
</pre>

**What I did:**
- Created a colorful, updating progress bar using terminal colors.

---

### ex09 — ft_package
**Goal:** Build a simple Python package and demonstrate its usage.

**How it works:**

#### Package Structure & Usage
The package contains a function to count occurrences in a list:

```python
def count_in_list(lst, value):
	return lst.count(value)
```

<pre>
Input: ["toto", "tata", "toto"], "toto" → 2
</pre>

**What I did:**
- Built a package with a counting function and provided usage instructions.

---

## 🎯 Conclusion

This pool helped me master Python basics, data structures, custom functions, error handling, and packaging. Each exercise was a step forward in my programming journey!

<div align="center">
	<b>Made with ❤️ by sperron</b>
</div>
