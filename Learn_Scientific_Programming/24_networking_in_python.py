# import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 80)
# client_socket.connect(server_address)

# client_socket.send(b"Hello from the client!")
# data = client_socket.recv(1024)
# print("Received response:", data.decode())

# client_socket.close()

# import urllib.request
# import urllib.parse
# import urllib.error
# for_hadle = urllib.request.urlopen(
#     'http://localhost/Python/Learn_Scientific_Programming/scientific-programming.txt')

# for line in for_hadle:
#     print(line.decode().strip())


import urllib.request
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = 'https://ardiansyahirwan.github.io'

# Fetch the page's content using urllib
with urllib.request.urlopen(url) as response:
    html_content = response.read()

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific data from the page using BeautifulSoup's methods
# For example, let's extract all the links on the page
links = soup.find_all('a')

# Print the extracted links
for link in links:
    print(link.get('href'))
