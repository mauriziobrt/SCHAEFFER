import os
import json
import csv
import sys

# def extract_metadata_from_json(json_path, relative_path):
#     """
#     Extract metadata from a JSON file, preserving lists for each category.
    
#     Args:
#         json_path (str): Path to the JSON file
#         relative_path (str): Relative path from the root directory
        
#     Returns:
#         dict: Extracted metadata or None if error
#     """
#     try:
#         with open(json_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
            
#         obj = data.get("object", {})
        
#         # Use the relative path + filename as the file_name
#         file_path = os.path.join(relative_path, obj.get("filename", ""))
        
#         # Extract basic metadata
#         metadata = {
#             "file_name": file_path,
#             "username": obj.get("username", ""),
#             "description": obj.get("description", "")
#         }
        
#         # Initialize category lists
#         categories = {
#             "Processes": [],
#             "PulseTypology": [],
#             "Complexity": [],
#             "Onset": [],
#             "Sustain": [],
#             "Offset": [],
#             "Type": [],
#             "MassType": [],
#             "Directionality": []  # Will be mapped to Direction
#         }
        
#         # Extract labels
#         labels = obj.get("labels", {})
        
#         # Process each label and categorize
#         for _, label_value in labels.items():
#             if "::" in label_value:
#                 category, value = label_value.split("::", 1)
                
#                 # Handle Type and MassType specifically to avoid confusion
#                 if category == "Type":
#                     categories["Type"].append(value)
#                 elif category == "MassType":
#                     categories["MassType"].append(value)
#                 else:
#                     # For other categories, use partial matching
#                     for key in categories:
#                         if key in category and key not in ["Type", "MassType"]:
#                             categories[key].append(value)
        
#         # Add categories to metadata
#         for key, values in categories.items():
#             column_name = "Direction" if key == "Directionality" else key
#             metadata[column_name] = values
        
#         return metadata
    
#     except Exception as e:
#         print(f"Error processing {json_path}: {e}")
#         return None
def extract_metadata_from_json(json_path, relative_path):
    """
    Extract metadata from a JSON file, preserving lists for each category.
    Args:
        json_path (str): Path to the JSON file
        relative_path (str): Relative path from the root directory
    Returns:
        dict: Extracted metadata or None if error
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            obj = data.get("object", {})
            
            # Use the relative path + filename as the file_name
            file_path = os.path.join(relative_path, obj.get("filename", ""))
            
            # Extract basic metadata
            metadata = {
                "file_name": file_path,
                "username": obj.get("username", ""),
                "description": obj.get("description", ""),
                # "filelength": obj.get("filelength(seconds)", 0)
            }
            
            # Initialize category lists
            categories = {
                "processes": [],
                "pulse-typology": [],
                "complexity": [],
                "onset": [],
                "sustain": [],
                "offset": [],
                "type": [],
                "mass-type": [],
                "directionality": [] # Will be mapped to Direction
            }
            
            # Extract labels
            labels = obj.get("labels", {})
            
            # Process each label and categorize
            for category, value in labels.items():
                if category in categories:
                    # Handle lists
                    if isinstance(value, list):
                        categories[category].extend(value)
                    # Handle null values
                    elif value == "null" or value is None:
                        pass  # Skip null values
                    # Handle string values
                    else:
                        categories[category].append(value)
            
            # Add categories to metadata
            for key, values in categories.items():
                column_name = "direction" if key == "directionality" else key
                metadata[column_name] = values
                
            return metadata
            
    except Exception as e:
        print(f"Error processing {json_path}: {e}")
        return None
    
def create_metadata_csv(root_dir, output_file):
    """
    Walk through all directories starting from root_dir,
    find JSON files, extract metadata, and write to a CSV file.
    
    Args:
        root_dir (str): Root directory to start searching
        output_file (str): Path to output CSV file
    """
    all_metadata = []
    
    # Walk through all directories
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, root_dir)
                
                metadata = extract_metadata_from_json(json_path, relative_path)
                if metadata:
                    all_metadata.append(metadata)
    
    # Define columns for the CSV
    columns = [
        "file_name", "username", "processes", "pulse-typology", 
        "complexity", "onset", "sustain", "offset", "type", "mass-type", 
        "direction", "description"
    ]
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        
        # Write rows, converting lists to string representation
        for metadata in all_metadata:
            row_dict = {}
            for key, value in metadata.items():
                if isinstance(value, list):
                    row_dict[key] = str(value)
                else:
                    row_dict[key] = value
            writer.writerow(row_dict)
    
    print(f"Metadata CSV created at {output_file} with {len(all_metadata)} entries.")

def main():
    # Check if root directory is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python json_to_csv_lists.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    output_file = os.path.join(root_dir, "metadata.csv")
    
    # Check if the provided path exists and is a directory
    if not os.path.exists(root_dir):
        print(f"Error: Path '{root_dir}' does not exist.")
        sys.exit(1)
    
    if not os.path.isdir(root_dir):
        print(f"Error: Path '{root_dir}' is not a directory.")
        sys.exit(1)
    
    create_metadata_csv(root_dir, output_file)

if __name__ == "__main__":
    main()