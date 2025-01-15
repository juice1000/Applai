import json


def text_to_json_string(input_file):
    """
    Converts plain text from a file into a JSON-formatted string.
    Args:
        input_file (str): Path to the input text file.
    """

    try:
        # Read the plain text from the file
        with open(input_file, "r") as file:
            text_data = file.read()

        # Convert the plain text into a JSON string
        json_data = text_data.strip()
        return json.dumps(json_data, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")
