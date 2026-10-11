import os
import time

# Enable ANSI escape sequences for Windows console
if os.name == 'nt':
    os.system('')

# --- ANSI COLOR ESCAPE SEQUENCES ---
RED_BG = '\033[41m'
WHITE_BG = '\033[47m'
BLUE_BG = '\033[44m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
RESET = '\033[0m'

def draw_flag():
    print("--- 1. Flag of the Netherlands ---")
    width = 30
    # Print 2 lines for each color
    for _ in range(2):
        print(RED_BG + " " * width + RESET)
    for _ in range(2):
        print(WHITE_BG + " " * width + RESET)
    for _ in range(2):
        print(BLUE_BG + " " * width + RESET)
    print("\n")

def draw_pattern():
    print("--- 2. Repeating Pattern ---")
    # Generate the crossed diamond pattern based on the provided image
    width = 40
    height = 5
    
    for i in range(height):
        line = ""
        for j in range(width):
            # Calculate positions for backslashes, forward slashes, and intersections
            if i == 2 and j % 6 == 2:
                line += "X"
            elif j % 6 == i:
                line += "\\"
            elif j % 6 == 4 - i:
                line += "/"
            else:
                line += " "
        print(line)
    print("\n")

def analyze_sequence():
    print("--- 4. sequence.txt Analysis ---")
    numbers = []
    
    # Attempt 
    try:
        with open("sequence.txt", "r") as file:
            for line in file:
                # If there are multiple numbers on a line separated by spaces
                for num in line.split(): 
                    numbers.append(float(num))
    except FileNotFoundError:
        print("File 'sequence.txt' not found! Using test data instead...")
        numbers = [10.5, -5.0, 20.1, -15.2, 8.0, 10.0]

    if not numbers:
        print("The file is empty.")
        return

    # Condition: Sum of absolute values at even and odd positions
    sum_even = 0
    sum_odd = 0

    for i in range(len(numbers)):
        if i % 2 == 0: # Even indices (0, 2, 4...)
            sum_even += abs(numbers[i])
        else:          # Odd indices (1, 3, 5...)
            sum_odd += abs(numbers[i])

    total = sum_even + sum_odd
    
    if total > 0:
        percent_even = (sum_even / total) * 100
        percent_odd = (sum_odd / total) * 100

        print(f"Sum of even positions: {percent_even:.1f}%")
        print(f"Sum of odd positions: {percent_odd:.1f}%")

        # Generate the chart with colors (40 characters wide)
        bar_width = 40
        blocks_even = int((percent_even / 100) * bar_width)
        blocks_odd = bar_width - blocks_even

        print("Chart (Green = Even, Yellow = Odd):")
        print(GREEN_BG + " " * blocks_even + YELLOW_BG + " " * blocks_odd + RESET)
    print("\n")

def draw_graph():
    print("--- EXTRA TASK: Graph for y = 2x ---")
    height = 9 # Minimum 9 lines high according to instructions
    width = 10
    
    # The console prints from top to bottom, so 'y' goes from 8 down to 0
    for y in range(height - 1, -1, -1):
        line = f"{y} |" # Y-axis
        for x in range(width):
            # Condition for the function y = 2x
            if y == 2 * x:
                line += " * "
            else:
                line += "   "
        print(line)
    
    # Print the X-axis
    print("  +" + "-" * (width * 3))
    x_axis = "   "
    for x in range(width):
        x_axis += f" {x} "
    print(x_axis)
    print("\n")

def animate():
    print("--- 3. Animation ---")
    input("Press ENTER to start the animation ...")
    
    # 4 simple frames
    frames = [
        "   (•_•)   \n   <)   )╯ \n    /  \\   ",
        "   ( •_•)  \n   \\(   (> \n    /  \\   ",
        "   (•_•)   \n   <)   )╯ \n    /  \\   ",
        "   ( •_•)  \n   \\(   (> \n    /  \\   "
    ]
    
    for _ in range(2): # Repeat the animation a couple of times
        for frame in frames:
            # os.system("cls") clears the console on Windows "clear" 
            command = "cls" if os.name == "nt" else "clear"
            os.system(command)
            print("\n" * 5)
            print(frame)
            time.sleep(0.4) # Pause between frames

# Execute all functions in order
if __name__ == "__main__":
    draw_flag()
    draw_pattern()
    analyze_sequence()
    draw_graph()
    animate()