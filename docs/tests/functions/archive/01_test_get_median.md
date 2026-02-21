# Test Get Median Pseudocode

This document will be broken up into three sections needed to organize the testing of the function.

## Sections

1. The "Source of Truth" (The Data)
You need a way to store your test cases. Think about how you'll define:

- The input list.
- The expected result.
- A name for the test (so you know which one failed).

2. The "Engine" (The Loop)
This is where the work happens. You’ll need to iterate (loop) through your data. For each case:

- How to retrieve the the input from the data.
- How to save a failure so the "Reporter" can see it later.
- Send the input to `get_median` function.
- Capture the answer.
- Compare it to the "Expected" result.

3. The "Reporter" (The Summary)
This happens after the loop finishes. It needs to look at the total tally and decide:

- Did everything pass?
- If not, how many failed, and what were the details?

## Pseudocode

### The Source of Truth (Data)

_**Objective**_
Before the loop starts, a "clipboard" is needed to record any issues.

- Define a place to store details about failures.
- Define a counter to keep track of the number of failures.
- The expected result.
- A name for the test (so you know which one failed).

_**Pseudocode**_

1. provide a data structure to hold the test cases.
2. define a data structure to hold the test results.
3. define a data structure to hold the test failures.
4. define a data structure to hold the test summary.
5. define a data structure to hold the test details.
6. define a data structure to hold the test failures summary.
7. data structure types:
  - cases: list of dictionaries
  - results: list of dictionaries
  - failures: list of dictionaries
  - summary: dictionary
  - details: dictionary
  - failures_summary: dictionary
8. Example of data structures:
  - cases = [ {"name": "Empty", "input": [], "expected": "Error: Empty"}, ... ]
  - results = [ {"name": "Empty", "input": [], "expected": "Error: Empty", "actual": "Error: Empty"}, ... ]
  - failures = [ {"name": "Empty", "input": [], "expected": "Error: Empty", "actual": "Error: Empty"}, ... ]
  - summary = {"total": 10, "passed": 9, "failed": 1}
  - details = {"Empty": {"input": [], "expected": "Error: Empty", "actual": "Error: Empty"}}
  - failures_summary = {"Empty": 1}

### The Engine (Loop)

_**Strategy**_

1. **Preparation:** The source of truth section
2. **Import Data to function:** Grab the list of numbers from your data.
3. **Call function:** Pass that list into your get_median function and save whatever comes back into a temporary variable (the "Actual Result").
4. **Comparison:** Check if the "Actual Result" matches the "Expected Result" you stored in your data.
5. **Recording:** The Reporter section
6. **Handoff:** The Reporter section

_**Pseudocode**_

1. Import data to function
  - Data stored in a list of dictionaries.  See `preparation` for details
2. Call function
  - Pass the list of numbers into the get_median function
  - loop through the cases
  - for each case
  - get the expected result
    - get the actual result
    - compare the expected result with the actual result using `==` operator
    - record the result in the results list
    - if the result is a failure, record the failure in the failures list
3. Comparison
  - Check if the actual result matches the expected result
  - how to compare the expected result with the actual result
    - use the `==` operator to compare the expected result with the actual result
    - log the failure if the result is a failure
4. Recording
  - Record the result in the results list
5. Handoff
  - Handoff the results to the reporter

### The Reporter (Summary)
