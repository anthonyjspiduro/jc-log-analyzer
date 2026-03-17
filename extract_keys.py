import json
import sys
import argparse

def extract_keys(data, prefix=''):
    """ Recursively extract all unique dot-notation keys from a JSON object or list. """
    keys = set()
    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{prefix}{k}"
            keys.add(full_key)
            if isinstance(v, (dict, list)):
                keys.update(extract_keys(v, f"{full_key}."))
    elif isinstance(data, list):
        for item in data:
            keys.update(extract_keys(item, prefix))
    return keys

def main():
    parser = argparse.ArgumentParser(description="Extract all unique field keys from a JumpCloud JSON activity log.")
    parser.add_argument("file", help="Path to the JSON log file")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            logs = json.load(f)
            
            # If the file is a single object instead of a list, wrap it
            if isinstance(logs, dict):
                logs = [logs]
                
            all_keys = set()
            for log in logs:
                all_keys.update(extract_keys(log))
            
            for key in sorted(list(all_keys)):
                print(key)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{args.file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
