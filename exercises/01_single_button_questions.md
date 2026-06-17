# Single Button Practice Questions

Use these questions before checking the scan cycle log. Focus on predicting how the current `BUTTON` input affects `MOTOR`.

### Question 1

**Question:**  
If `BUTTON=False`, what should `MOTOR` be after the output update?

**Given state / cycle:**  
`BUTTON=False`, previous `MOTOR=False`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=False`.

**Explanation:**  
The fixed teaching logic is `MOTOR = BUTTON`. Since `BUTTON=False`, the output coil is off after this scan.

### Question 2

**Question:**  
If `BUTTON=True`, what should `MOTOR` be after the output update?

**Given state / cycle:**  
`BUTTON=True`, previous `MOTOR=False`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=True`.

**Explanation:**  
The input image contains `BUTTON=True`, so program execution sets `MOTOR=True`. The output update then applies that value.

### Question 3

**Question:**  
Why does the single button example not have latch memory?

**Given state / cycle:**  
Cycle 3 has `BUTTON=True` and `MOTOR=True`. Cycle 4 has `BUTTON=False`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
In Cycle 4, `MOTOR=False`.

**Explanation:**  
This example does not use `previous MOTOR` in its logic. It only uses the current input image, so when `BUTTON=False`, `MOTOR` turns off.
