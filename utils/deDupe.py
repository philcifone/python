import os
import filecmp
import shutil

def remove_duplicate_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            current_dir = os.path.join(dirpath, dirname)
            comparison = filecmp.dircmp(root_dir, current_dir)

            if not comparison.left_only and not comparison.right_only:
                # The directories have identical content, remove one of them
                print(f"Removing duplicate directory: {current_dir}")
                shutil.rmtree(current_dir)

if __name__ == '__main__':
    root_directory = "/home/phil/exampleDir"
    remove_duplicate_directories(root_directory)

