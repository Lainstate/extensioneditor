import os
import sys

def add_fc2map_extension(filename):
    base_name, _ = os.path.splitext(filename)
    new_filename = f"{base_name}.fc2map"
    os.rename(filename, new_filename)
    print(f"Extension added: .fc2map")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        add_fc2map_extension(file_name)
    else:
        print("Usage: python add_fc2map_extension.py <file_name>")
