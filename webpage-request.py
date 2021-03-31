import requests
import sys
import argparse

response = 0

def retrieveURL():
    """ Rtrieves URL by using argparse and adds the https prefix to it."""
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    prefix = "https://"
    return prefix + args.url

def checkPage(url):
    url = str(url)
    print("URL, famiglia:")
    print(url)
    global response
    try:
        response = requests.get(url)
        if response.status_code:
            if response.status_code == 200:
                # THAT'S WHY WE GOT THE CHARACTER CONVERSION (IT WAS ON UNICODE ON THE WEBSITE) ON LINE 132!!
                # Standard of this page will be utf-8 because it has special characters
                response.encoding = "utf-8"
                return response
            elif response.status_code == 204:
                print("Retrieved data but no content.")
            elif response.status_code == 304:
                print("Not modified.")
    except(requests.exceptions.ConnectionError):
        print("[ERROR]: Could not connect to the internet, network error. Check if you're connected to the internet.")
        sys.exit(1)
    except(requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
        print("[ERROR]: Connection timed out.")
    except requests.exceptions.HTTPError as errh:
        print ("[ERROR]: HTTP Error:", errh)
    except(requests.exceptions.RequestException):
        print("[ERROR]: Didn't catch the error with the previous exceptions, something is going on...")
        sys.exit(1)

def checkContent(response):
    pageContent = response.content
    # Transform the page into a string so we can parse it
    pageText = response.text
    return pageText

def main():
    url = 'https://pt.surf-forecast.com/breaks/Vilas/forecasts/latest'
    url = retrieveURL()
    response = checkPage(url)
    pageText = checkContent(response)
    print(pageText)
    print("LOGGING: Page requested succesfully.")
    url = str(url[8:])
    file_str = url + ".txt"
    #with open(file_str, "w") as text_file:
    #    text_file.write(pageText)

main()