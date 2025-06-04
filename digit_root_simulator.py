from mpmath import mp
import matplotlib.pyplot as plt

# Set precision
mp.dps = 1000  # digits of precision

# Function to get digit root
def digit_root(n):
    return 9 if n == 0 else n % 9 or 9

# Compute digit root convergence
def digit_root_convergence(irrational_str, steps=100):
    digits = [int(d) for d in irrational_str if d.isdigit()]
    roots = []
    cumulative_sum = 0
    for i in range(min(steps, len(digits))):
        cumulative_sum += digits[i]
        roots.append(digit_root(cumulative_sum))
    return roots

# Use π
pi_str = str(mp.pi)
roots = digit_root_convergence(pi_str, steps=150)

# Plot the result
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(roots)+1), roots, marker='o', linestyle='-')
plt.title("Digit Root Convergence of π")
plt.xlabel("Digits Summed")
plt.ylabel("Digit Root of Cumulative Sum")
plt.grid(True)
plt.tight_layout()
plt.show()