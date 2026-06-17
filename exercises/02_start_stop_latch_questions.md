# Start/Stop Latch Practice Questions

Use these questions to practice predicting how latch memory affects `MOTOR`.

### Question 1

**Question:**  
What happens when `START=True`, `STOP=True`, and previous `MOTOR=False`?

**Given state / cycle:**  
`START=True`, `STOP=True`, previous `MOTOR=False`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=True`.

**Explanation:**  
The latch logic is `MOTOR = STOP and (START or previous MOTOR)`. Since `STOP=True` and `START=True`, the new `MOTOR` output becomes True.

### Question 2

**Question:**  
What happens when `START=False`, `STOP=True`, and previous `MOTOR=True`?

**Given state / cycle:**  
`START=False`, `STOP=True`, previous `MOTOR=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=True`.

**Explanation:**  
Even though `START` is released, `previous MOTOR=True` keeps the latch active. This is why the motor remains on after the start button is released.

### Question 3

**Question:**  
Why must `MOTOR=False` when `STOP=False`?

**Given state / cycle:**  
`START=False`, `STOP=False`, previous `MOTOR=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=False`.

**Explanation:**  
`STOP=False` means the stop circuit is broken or the stop button is pressed. Because `STOP` is the first condition in the latch logic, it forces the whole expression to False.
