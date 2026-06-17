# Emergency Stop Practice Questions

Use these questions to practice emergency stop override behavior.

### Question 1

**Question:**  
Why must `MOTOR=False` when `E_STOP=False`?

**Given state / cycle:**  
`START=True`, `STOP=True`, `E_STOP=False`, previous `MOTOR=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=False`.

**Explanation:**  
In this teaching scenario, emergency stop has priority over normal start and latch logic. When `E_STOP=False`, `MOTOR` is forced off regardless of `START` or previous `MOTOR`.

### Question 2

**Question:**  
After `E_STOP` is reset, why should `MOTOR` not automatically restart?

**Given state / cycle:**  
Previous scan: `E_STOP=False`, output `MOTOR=False`. Current scan: `START=False`, `STOP=True`, `E_STOP=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=False`.

**Explanation:**  
The emergency stop scan forced `MOTOR=False`, so the latch memory is no longer active. After reset, the operator must press `START` again.

### Question 3

**Question:**  
Why should emergency stop override be handled carefully?

**Given state / cycle:**  
`START=True`, `STOP=True`, `E_STOP=False`, previous `MOTOR=True`.

**Your prediction:**  
Write your prediction before checking the answer.

**Answer:**  
`MOTOR=False`, and the logic should make that outcome easy to inspect.

**Explanation:**  
Emergency stop logic is safety-related. In this teaching tool, `E_STOP=False` overrides both `START` and latch memory so the output cannot remain energized.
