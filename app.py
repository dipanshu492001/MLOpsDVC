import os
import json

# New dictionary to append
dict3 = {
    "name": "Charlie",
    "age": 28,
    "city": "Chicago"
}

# Define the folder and file path
folder_name = "output_data"
file_name = "data.json"
file_path = os.path.join(folder_name, file_name)

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Load existing data if file exists, otherwise start fresh
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    # Initial data
    dict1 = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }

    dict2 = {
        "name": "Bob",
        "age": 30,
        "city": "Los Angeles"
    }

    data = {
        "person1": dict1,
        "person2": dict2
    }

# Add the new person with the next available key
next_key = f"person{len(data) + 1}"
data[next_key] = dict3

# Save the updated data to the file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print(f"New row added as '{next_key}' and saved to {file_path}")
