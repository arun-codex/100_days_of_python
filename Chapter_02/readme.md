# Chapter 2: Variables and Data Types

This directory contains resources and programs related to Chapter 2: Variables and Data Types.

## Key Concepts

### 1. Variables and Identifiers
A **Variable** in Python is like a container that stores data.
- **Red Container** = Sugar
- **Blue Container** = Salt

When we write:
```python
a = 1
```
- `a` is the **identifier** (the name of the container).
- `1` is the **data** (the item stored in the container).

Like how people identify you by your name (e.g., "Arun" is the identifier, and you are the data/person).

### 2. Data Types
Python has several primary data types:
1.  **Integer (`int`)**: Whole numbers, positive or negative, without a decimal component.
    *   *Examples:* `1`, `-1`, `100`
2.  **Floating Point Number (`float`)**: Numbers with a decimal component.
    *   *Examples:* `1.5`, `-1.5`, `100.5`
3.  **String (`str`)**: A sequence of characters wrapped in quotes.
    *   *Examples:* `"Arun"`, `"Hello"`, `"123"`
4.  **Boolean (`bool`)**: Truth values representing `True` or `False`.
    *   *Examples:* `True`, `False`
5.  **NoneType (`None`)**: A special value representing the absence of a value.
    *   *Examples:* `None`

### 3. Checking the Type of a Variable
You can use the built-in `type()` function to check the data type of any variable.
```python
a = 1
print(type(a))  # Output: <class 'int'>
```

### 4. Rules for Defining Variable Names (Identifiers)
1.  A variable name must start with a letter or an underscore (`_`).
2.  A variable name cannot start with a number.
3.  It can only contain alphanumeric characters and underscores (`A-z`, `0-9`, and `_`).
4.  Variable names are case-sensitive (`a` and `A` are different variables).
5.  Variable names cannot be Python keywords (like `def`, `class`, `if`, etc.).

---

## Files in this Chapter

*   **[01_Variables.py](./01_Variables.py)**: Demonstrates variable declaration, string values, and basic addition.
*   **[02_datatypes.py](./02_datatypes.py)**: Demonstrates various Python data types and how to check them using `type()`.
*   **[notes.txt](./notes.txt)**: Hand-written notes containing simplified explanations of these concepts.

