import urllib.request
import urllib.parse
import json

# Set up the initial service URL
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"  # Ensure this URL is correct

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Prepare the parameters and encode them
    params = {'q': address.strip()}
    query_string = urllib.parse.urlencode(params)
    full_url = serviceurl + query_string

    # Make the API request using urllib
    with urllib.request.urlopen(full_url) as response:
        # Read the response
        data = response.read()
        # Decode the data (from bytes to string)
        text = data.decode()

    try:
        # Try to decode the JSON response
        js = json.loads(text)
    except json.JSONDecodeError:
        print('Error parsing JSON')
        continue

    # Validate the JSON structure for expected fields
    if 'features' not in js or len(js['features']) == 0:
        print('==== Object not found or Download error ====')
        continue  # Skip the rest of this loop iteration and prompt for location again

    # Extracting and printing details from the first feature
    feature = js['features'][0]
    properties = feature['properties']  # A dictionary of the properties

    # Ensure 'lat', 'lon', and 'formatted' are in properties
    lat = properties.get('lat', 'No latitude provided')
    lon = properties.get('lon', 'No longitude provided')
    formatted_location = properties.get('formatted', 'No formatted location provided')

    # Now also extract and print the plus_code, if available
    plus_code = properties.get('plus_code', 'No Plus Code provided')

    print(f'Latitude: {lat}, Longitude: {lon}')
    print(f'Location: {formatted_location}')
    print(f'Plus Code: {plus_code}')
