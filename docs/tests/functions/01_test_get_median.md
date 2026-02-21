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

### The Engine (Loop)

### The Reporter (Summary)
