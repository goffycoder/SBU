import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# --- Configuration ---
MAX_N = 10000  # The maximum row of Pascal's triangle to calculate and plot.
INTERVAL_MS = 10000 # Milliseconds between each frame of the animation.
OUTPUT_FILENAME = 'pascal_triangle_animation.gif' # The name of the output file.

# --- Plot Setup ---
fig, ax = plt.subplots(figsize=(10, 6))

def combinations(n, k):
    """
    Calculates the binomial coefficient "n choose k" efficiently.
    Uses math.comb for Python 3.8+ for accuracy and speed.
    """
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def get_pascals_row(n):
    """
    Generates all coefficients for a given row 'n' of Pascal's triangle.
    """
    return [combinations(n, k) for k in range(n + 1)]

def update(n):
    """
    This function is called for each frame of the animation.
    It clears the previous plot and draws the bar chart for the current row 'n'.
    """
    # Clear the current axes
    ax.clear()

    # Get the coefficients for the current row
    coefficients = get_pascals_row(n)
    k_values = list(range(n + 1))

    # Create the bar plot
    ax.bar(k_values, coefficients, color='skyblue', edgecolor='darkblue')

    # --- Styling the Plot ---
    ax.set_title(f"Binomial Coefficients (Pascal's Triangle): n = {n}", fontsize=16)
    ax.set_xlabel("k (Term number in row)", fontsize=12)
    ax.set_ylabel("Coefficient Value (nCk)", fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Set x-axis ticks to be integers
    if n < 20:
        ax.set_xticks(k_values)

    # Set aesthetic limits for the plot
    ax.set_xlim(-1, n + 1)

    # Add a text annotation for clarity
    fig.tight_layout()


# --- Create and Save the Animation ---
# FuncAnimation runs the 'update' function for each frame.
# 'frames' determines the value of 'n' passed to the update function.
# Here, it will animate from n=0 to n=MAX_N.
ani = animation.FuncAnimation(fig, update, frames=range(MAX_N + 1), interval=INTERVAL_MS, repeat=False)

# To prevent the plot from showing in interactive environments before saving
plt.ioff()

print(f"Generating animation for n=0 to n={MAX_N}...")
print(f"This may take a moment. The output will be saved as '{OUTPUT_FILENAME}'.")

# Save the animation as a GIF.
# This requires the 'imagemagick' writer, which you might need to install.
# If you get an error, you may need to run:
# pip install Pillow
# And also install ImageMagick on your system.
try:
    ani.save(OUTPUT_FILENAME, writer='pillow', fps=10)
    print(f"Successfully saved animation to '{OUTPUT_FILENAME}'")
except Exception as e:
    print(f"Error saving animation: {e}")
    print("Please ensure you have 'Pillow' installed (`pip install Pillow`).")
    print("Displaying plot instead...")
    plt.ion() # Turn interactive mode back on
    plt.show() # Show a static plot of the final frame as a fallback
