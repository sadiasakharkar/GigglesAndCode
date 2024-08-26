import time
import sys

def print_line_by_line(song_lines, delay=0.1):
    """
    Prints each line of the song one letter at a time.
    
    :param song_lines: List of lines (strings) to be printed
    :param delay: Delay between printing each letter (in seconds)
    """
    for line in song_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()  # Ensure the character is printed immediately
            time.sleep(delay)
        sys.stdout.write('\n')  # Move to the next line after printing all characters
        sys.stdout.flush()  # Ensure the newline is printed immediately

song_lines = [
    "Baby, I'm dancing in the dark,",
    "With you between my arms.",
    "Barefoot on the grass",
    "Listening to our favorite song",
    "I have faith in what I see",
    "Now I know I have met an angel in person",
    "And she looks perfect"
]

print_line_by_line(song_lines, delay=0.1)
