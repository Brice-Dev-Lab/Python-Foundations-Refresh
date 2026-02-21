# Test Plan Pseudocode  

## Testing `get_median(data)`

---

## 1. Purpose

Validate that `get_median(data)` satisfies the following conditions:

1. Returns the correct median value.
2. Returns `None` (or defined error value) when input list is empty.
3. Does not modify the original input list (immutability requirement).

---

## 2. Test Architecture

The test script uses the following variables:

### Global Variables

| Variable | Type | Purpose | Initial Value |
|----------|------|---------|---------------|
| `test_cases` | list of dict | Stores all test scenarios to execute | List of test case dictionaries |
| `failures` | list of dict | Accumulates failed test information | Empty list `[]` |

### Per-Test-Case Variables (Loop Scope)

| Variable | Type | Purpose | Source |
|----------|------|---------|--------|
| `case` | dict | Current test case being processed | Iteration over `test_cases` |
| `name` | str | Human-readable identifier for the test | `case["name"]` |
| `input_list` | list of int | Input data to pass to `get_median()` | `case["input"]` |
| `expected_result` | int or None | The correct median value | `case["expected"]` |
| `original_copy` | list of int | Snapshot of input before function call | `input_list.copy()` |
| `actual_result` | int or None | Value returned by `get_median()` | Return value of function |

---

## 3. Test Data Definition

### 3.1 Data Structure: `test_cases`

**Type:** `list` of `dict`

**Purpose:** Define all test scenarios to validate `get_median()` functionality

**Structure:** Each dictionary contains:
- `"name"` (str): Test case identifier
- `"input"` (list of int): Data to pass to function
- `"expected"` (int or None): Expected return value

### 3.2 Data Structure: `failures`

**Type:** `list` of `dict`

**Purpose:** Collect diagnostic information about failed tests

**Structure:** Each failure dictionary contains:

**For correctness failures:**
- `"name"` (str): Test case name
- `"expected"` (int or None): Expected value
- `"actual"` (int or None): Actual returned value
- `"reason"` (str): Error description

**For immutability failures:**
- `"name"` (str): Test case name
- `"reason"` (str): Error description
- `"original"` (list): Input before function call
- `"modified"` (list): Input after function call

---

### 3.3 Test Case Specification

```pseudo
test_cases = [

    {
        "name": "Odd Length List",
        "input": [5, 2, 9, 1, 7],
        "expected": 5
    },

    {
        "name": "Even Length List",
        "input": [40, 10, 30, 20],
        "expected": 20
    },

    {
        "name": "Empty List",
        "input": [],
        "expected": None
    }

]
```
Define failures as an empty list

`failures = []`

---

## 4. Execution Engine

### 4.1 Test Loop

For each `case` in `test_cases`:

#### Step 1 --- Extract Values

    name = case["name"]
    input_list = case["input"]
    expected_result = case["expected"]

#### Step 2 --- Preserve Original State

    original_copy = input_list.copy()  # Shallow copy of the list

#### Step 3 --- Execute Function

    actual_result = get_median(input_list)

#### Step 4 --- Validate Functional Correctness

    IF actual_result != expected_result THEN
        failures.append({
            "name": name,
            "expected": expected_result,
            "actual": actual_result,
            "reason": "Incorrect median value"
        })
    END IF

#### Step 5 --- Validate Immutability

    IF input_list != original_copy THEN
        failures.append({
            "name": name,
            "reason": "Input list modified (side effect detected)",
            "original": original_copy,
            "modified": input_list
        })
    END IF

---

## 5. Result Reporting

After all test cases are executed:

    IF len(failures) == 0 THEN
        PRINT "All tests passed."
    ELSE
        PRINT "Test failures detected."
        PRINT "Failure count:", len(failures)
        PRINT ""  # Blank line for readability

        FOR each failure in failures DO
            PRINT "Test Case:", failure["name"]
            IF "expected" in failure THEN
                PRINT "  Expected:", failure["expected"]
                PRINT "  Actual:", failure["actual"]
            END IF
            PRINT "  Reason:", failure["reason"]
            IF "original" in failure THEN
                PRINT "  Original:", failure["original"]
                PRINT "  Modified:", failure["modified"]
            END IF
            PRINT ""  # Blank line between failures
        END FOR
    END IF

---

## 6. Logical Flow Summary

```pseudo
# 1. Initialize test data
test_cases = [list of test case dictionaries]
failures = []

# 2. Execute all test cases
FOR each case in test_cases:
    # 2a. Extract test data
    name = case["name"]
    input_list = case["input"]
    expected_result = case["expected"]

    # 2b. Preserve original input
    original_copy = input_list.copy()

    # 2c. Execute function under test
    actual_result = get_median(input_list)

    # 2d. Validate correctness
    IF actual_result != expected_result:
        failures.append(failure_dict_with_comparison)
    END IF

    # 2e. Validate immutability
    IF input_list != original_copy:
        failures.append(failure_dict_with_mutation_details)
    END IF
END FOR

# 3. Report test results
IF len(failures) == 0:
    PRINT "All tests passed."
ELSE:
    PRINT failure summary and detailed failure information
END IF
```
