# war-copilot
Simple python package to simulate outcomes to the game war. 
Created for fun to test out GitHub Copilot.

The package is called **WarSim**.

## Example

```python
import matplotlib.pyplot as plt

# Simulate 1000 games
y = simulate_war(1000)

# Plot outcome
plt.bar(["player", "computer"], y)
plt.show()
```