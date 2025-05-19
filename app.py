import os
import json

# Create two dictionaries
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

# Combine the dictionaries
data = {
    "person1": dict1,
    "person2": dict2
}

# Define the folder and file path
folder_name = "output_data"
file_name = "data.json"
file_path = os.path.join(folder_name, file_name)

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Save the data into the file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print(f"Data saved to {file_path}")
