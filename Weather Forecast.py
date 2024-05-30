# Import the necessary modules!
import requests

# Input the city name
city = input('Enter City name: ')

# Display the message
print('Displaying Weather report for: ' + city)

# Fetch the weather details
url = 'https://wttr.in/{}'.format(city) # Use of format to pass city as a parameter here
res = requests.get(url)                 # Make use of the requests module

# Display the result
# Resultant data is stored in res. 
# Use of the text method to extract our desired weather details to display the result
print(res.text)
