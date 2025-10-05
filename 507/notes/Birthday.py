import matplotlib.pyplot as plt
import time
from decimal import Decimal, getcontext

def birthday_problem_precise(num_people, precision=50):
    """
    Calculates the probability of a shared birthday with high precision
    using the decimal module.
    """
    # Set the precision (number of significant digits) for decimal calculations
    getcontext().prec = precision

    if num_people > 365:
        return Decimal(1)
    if num_people <= 1:
        return Decimal(0)

    # Use Decimal objects for all parts of the calculation
    prob_unique = Decimal(1)
    days_in_year = Decimal(365)
    
    for i in range(num_people):
        # All arithmetic is now high-precision
        prob_unique *= (days_in_year - i) / days_in_year
    
    return Decimal(1) - prob_unique

# --- Setup for Dynamic Plotting ---
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 6))

# Lists to store the data points for plotting
n_values = []
prob_values = []

print("--- Dynamic Birthday Problem Visualizer (High Precision) ---")
print("Enter the number of people to see the probability.")
print("The plot will update with each new entry.")
print("Type 'quit' or 'q' to exit.")

# --- Main loop for continuous input and plotting ---
while True:
    try:
        # Get user input
        user_input = input("\nEnter group size 'n' (or 'quit'): ")
        
        if user_input.lower() in ['quit', 'q', 'exit']:
            print("Exiting the program. Goodbye!")
            break

        group_size = int(user_input)
        if group_size < 0:
            print("Please enter a positive number.")
            continue

        # --- High-Precision Calculation ---
        # Calculate probability with high precision (e.g., 50 digits)
        probability_precise = birthday_problem_precise(group_size, precision=50)
        
        # For plotting, we can convert the Decimal back to a standard float
        probability_float = float(probability_precise)

        n_values.append(group_size)
        prob_values.append(probability_float)
        
        # --- Display Results ---
        print(f"-> For n={group_size}:")
        # Print the high-precision result to see the difference
        print(f"   - High-Precision Value: {probability_precise*100}")

        # --- Update the Plot ---
        ax.clear() # Clear the previous plot
        
        # Sort values for a clean line plot
        sorted_points = sorted(zip(n_values, prob_values))
        sorted_n = [p[0] for p in sorted_points]
        sorted_probs = [p[1] for p in sorted_points]

        # Draw the line and the points
        ax.plot(sorted_n, sorted_probs, marker='o', linestyle='-', label='Probability')
        ax.scatter(n_values, prob_values, color='red') # Highlight individual entered points

        # Formatting
        ax.set_title('Live Birthday Problem Probability', fontsize=16)
        ax.set_xlabel('Number of People in Group (n)', fontsize=12)
        ax.set_ylabel('Probability of a Shared Birthday', fontsize=12)
        ax.set_xlim(0, max(80, max(n_values) + 10)) # Adjust x-axis dynamically
        ax.set_ylim(0, 1.1)
        ax.grid(True)
        ax.axhline(y=0.5, color='r', linestyle='--', label='50% Threshold')
        ax.legend()
        
        # Redraw the canvas
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)

    except ValueError:
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Turn off interactive mode when the loop is done
plt.ioff()
plt.show()