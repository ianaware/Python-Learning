import json # Import the json module

data = '''
{
    "name": {
       "title": "Dr.",
       "name": "Chuck"
    },
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes" 
    }
}''' # Define a JSON string

info = json.loads(data) # Load the JSON string into a Python dictionary
print('Title:', info['name']['title'])# Print the value of the "title" key
print('Name:', info['name']['name'])# Print the value of the "name" key
print('Phone:', info['phone']['number']) # Print the value of the "number" key in the "phone" key
print('Hide:', info["email"]["hide"]) # Print the value of the "hide" key in the "email" key
