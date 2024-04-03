
import os

def create():
    os.makedirs("tree/c/other_courses/cpp")
    os.makedirs("tree/c/other_courses/python")
    os.makedirs("tree/cpp/other_courses/c")
    os.makedirs("tree/cpp/other_courses/python")
    
def find(path, target_dir):
    # List all items in the current directory
    items = os.listdir(path)
    
    # Iterate through each item
    for item in items:
        # Get the absolute path of the item
        item_path = os.path.join(path, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # If the item matches the target directory, print its path
            if item == target_dir:
                print(item_path)
            # Recursively call find function to search in subdirectories
            find(item_path, target_dir)


path = "./tree"
dir = "python"
# create()
find(path, dir)