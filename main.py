import requests

def ping_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success ping: {url}")
        else:
            print(f"Error ping: {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Error ping: {url} - Exception: {e}")

def multi_ping(url, num_threads=4):
    for _ in range(num_threads):
        ping_url(url)

url = input("Enter the URL: ")
num_threads = int(input("Enter the number of threads (default is 4): ")) or 4
if requests.get(url).status_code != 200:
    print("Website does not exist.")
while (requests.get(url).status_code == 200):
    multi_ping(url, num_threads)
