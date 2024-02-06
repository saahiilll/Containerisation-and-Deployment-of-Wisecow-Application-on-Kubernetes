import requests
import time

def check_application_health(url):
    try:
        # Attempting to connect to the application
        response = requests.get(url)
        
        # Checking the status code of the response
        if response.status_code == 200:
            # If the status code is 200, it means the application is UP
            return "The application is UP and running smoothly!"
        else:
            # If the status code is not 200, it indicates some issue with the application
            return f"The application is DOWN with status code: {response.status_code}"
    except requests.ConnectionError:
        # If there's a connection error, it means the application is DOWN
        return "Connection Error: Unable to connect to the application."
    except requests.Timeout:
        # If there's a timeout error, it means the application is DOWN
        return "Timeout Error: Connection to the application timed out."
    except requests.RequestException:
        # If there's any other request exception, it means the application is DOWN
        return "Request Exception: Unable to access the application."


if __name__ == "__main__":
    # Prompting the user to input the URL of the application to check
    url = input("Please enter the URL of the application you want to check: ")
    
    # Prompting the user to input the interval for checking the application health
    interval = int(input("Enter the interval (in seconds) between checks: "))
    
    # Continuously checking the application health
    while True:
        print("\nChecking application health...")
        # Calling the function to check the application health and printing the result
        status = check_application_health(url)
        print(status)
        
        # Waiting for the specified interval before checking again
        time.sleep(interval)
