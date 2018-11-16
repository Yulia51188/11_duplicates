import argparse
import os
from collections import Counter


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Looking for duplicates in the specified directory.'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='directory is need to be checked for duplicates'
    )
    return parser.parse_args()


def find_duplicates(directory):
    file_tree = os.walk(directory)
    filename_dict = {}
    print(type(filename_dict))
    for address, dirs, files in file_tree:
        for filename in files:
            filepath = os.path.join(address, filename)
            if filename in filename_dict:
                filename_dict[filename].append(filepath) 
            else
        filename_dict[filename] = filepath
    duplicate_dict = {}
    for filename, path_list in filename_dict:
        if len(path_list) > 1:
            duplicate_dict[filename] = path_list
    print(duplicate_dict)
    
    return None

if __name__ == '__main__':
    args = parse_arguments()
    if not os.path.exists(args.directory):
        exit("The specified directory doesn't exist!")
    duplicates = find_duplicates(args.directory)
    if duplicates is None:
        exit('There are no duplicates in the directory')
    for filename, path_list in duplicates:
        print('{filename}:'.format(filename))
        for filepath in path_list:
            print(filepath)