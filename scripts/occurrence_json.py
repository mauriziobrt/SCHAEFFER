import os
import json
from collections import Counter, defaultdict

def get_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files
def analyze_json_attributes(json_files):
    # Initialize counters
    attribute_counters = defaultdict(Counter)
    missing_definitions = defaultdict(list)
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if "object" in data and "labels" in data["object"]:
                labels = data["object"]["labels"]
                
                for category, attribute in labels.items():
                    # Check if the attribute is null or "null"
                    if attribute is None or attribute == "null":
                        missing_definitions[category].append(file_path)
                        continue
                        
                    # Handle both string values and list values
                    if isinstance(attribute, list):
                        # For lists, count each item separately
                        for item in attribute:
                            attribute_counters[category].update([item])
                    else:
                        # For string values, count directly
                        attribute_counters[category].update([attribute])
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return attribute_counters, missing_definitions

def old_analyze_json_attributes(json_files):
    attribute_counters = {
        "Processes": Counter(),
        "PulseTypology": Counter(),
        "Complexity": Counter(),
        "Onset": Counter(),
        "Sustain": Counter(),
        "Offset": Counter(),
        "Type": Counter(),
        "MassType": Counter(),
        "Directionality": Counter()
    }
    missing_definitions = defaultdict(list)  # Stores files missing specific classes
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "object" in data and "labels" in data["object"]:
                    labels = data["object"]["labels"]
                    present_classes = set()
                    for key, value in labels.items():
                        category, attribute = value.split("::")
                        if category in attribute_counters:
                            attribute_counters[category].update([attribute])
                            present_classes.add(category)
                    
                    # Check for missing classes
                    for category in attribute_counters.keys():
                        if category not in present_classes:
                            missing_definitions[category].append(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return attribute_counters, missing_definitions

def save_results_to_file(attribute_counters, missing_definitions, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for key, counter in attribute_counters.items():
            f.write(f"\nOccurrences in '{key}':\n")
            for attribute, count in counter.most_common():
                f.write(f"  {attribute}: {count}\n")
        
        f.write("\nFiles missing definitions in some classes:\n")
        for category, files in missing_definitions.items():
            f.write(f"\nCategory '{category}' is missing in {len(files)} files:\n")
            for file in files:
                f.write(f"  {file}\n")

if __name__ == "__main__":
    # directory = input("Enter the path to the folder: ").strip()
    # directory = "*"
    directory = "*"
    # output_file = "old_analysis_results.txt"
    output_file = "analysis_results.txt"
    json_files = get_json_files(directory)
    # attribute_counters, missing_definitions = old_analyze_json_attributes(json_files)
    attribute_counters, missing_definitions = analyze_json_attributes(json_files)

    save_results_to_file(attribute_counters, missing_definitions, output_file)
    print(f"Results saved to {output_file}")
