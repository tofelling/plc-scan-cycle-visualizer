# TON Timer Practice Questions

Use these questions to practice how `IN`, `ET`, `PT`, and `Q` change when a TON timer runs across scan cycles.

### Question 1

**Question:**  
If `IN=True` but `ET<PT`, what should `Q` be?

**Given state / cycle:**  
`IN=True`, previous `ET=1`, `PT=3`, `cycle_time=1`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`ET=2`, `Q=False`.

**Explanation:**  
The timer increments `ET` by one cycle time, but `ET=2` has not reached `PT=3`. The done bit `Q` stays False.

### Question 2

**Question:**  
What happens when `ET` reaches `PT`?

**Given state / cycle:**  
`IN=True`, previous `ET=2`, `PT=3`, `cycle_time=1`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`ET=3`, `Q=True`.

**Explanation:**  
The timer increments `ET` from 2 to 3. Since `ET` reaches `PT=3`, the timer done bit `Q` becomes True.

### Question 3

**Question:**  
What happens to `ET` and `Q` when `IN=False`?

**Given state / cycle:**  
`IN=False`, previous `ET=3`, previous `Q=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`ET=0`, `Q=False`.

**Explanation:**  
A TON timer resets when `IN=False`. The elapsed time returns to zero, and the done bit turns off.
