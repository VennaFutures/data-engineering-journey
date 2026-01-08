## Data Engineering Journey

This repository documents my preparation for the ALX Data Engineering program.

### Day 1
- Python environment setup
- Basic variables and printing

### Day 2
- Python variables
- Core data types (int, float, string, boolean)
- Type checking and basic data modeling
#### Reflection
Today I explored Python’s core data types — `int`, `float`, `string`, and `boolean`. I practiced declaring variables and checking their types using `type()`. Then I modeled a real-world scenario by adding `monthly_study_hours` and `expected_salary`, showing how data engineers use variables to represent human goals and system inputs.

This helped me think like a data modeler:
- How do we represent effort and outcomes in code?
- How can simple variables become the foundation for dashboards, predictions, or simulations?

I also caught a bug: writing `expected_salary = 100,000.0` creates a **tuple**, not a float. Fixing it to `100000.0` reminded me that syntax matters — especially when modeling money or metrics.

### Day 3
- Control flow using if / elif / else
- Comparison and logical operators
- Basic decision-making logic

#### Reflection
Today I focused on Python control flow — the ability to make decisions in code. I practiced using comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and combined them with `if`, `elif`, and `else` statements to guide program behavior. Adding logical operators (`and`, `or`, `not`) helped me build more complex rules.

I extended my script with a `goal` and `commitment_level` variable, which made the exercise feel like real data validation. For example, checking if commitment is high or needs improvement mirrors how data engineers enforce rules in pipelines. This showed me that control flow is not just about syntax, but about modeling real-world decisions in code.

Key insight: **Control flow is the bridge between raw data and meaningful outcomes.** By setting conditions, I can ensure that my programs respond intelligently to different scenarios.