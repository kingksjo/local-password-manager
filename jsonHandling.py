import json
import os


def update_json_file(filename, new_data):
    """
    Efficiently update a JSON file with new data.
    
    Args:
        filename (str): Path to the JSON file
        new_data (dict): Dictionary to update or merge with existing data
    """
    try:
        # Check if file exists and is not empty
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r") as file:
                existing_data = json.load(file)

            # Merge new data with existing data
            existing_data.update(new_data)
            write_data = existing_data
        else:
            # If file doesn't exist or is empty, use new data directly
            write_data = new_data

        # Write updated data to file
        with open(filename, "w") as file:
            json.dump(write_data, file, indent=4)

    except json.JSONDecodeError:
        # Handle potential JSON parsing errors
        print(f"Error reading {filename}. Creating a new file.")
        with open(filename, "w") as file:
            json.dump(new_data, file, indent=4)
    except IOError as e:
        # Handle file I/O errors
        print(f"Error writing to {filename}: {e}")
