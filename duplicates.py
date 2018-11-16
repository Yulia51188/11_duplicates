import argparse
import os
import collections
import itertools

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
    filename_dict = collections.defaultdict(lambda: [])
    for address, dirs, filenames in file_tree:
        for filename in filenames:
            filepath = os.path.join(address, filename)
            filesize = os.path.getsize(filepath)
            file_index = (filename, filesize)
            filename_dict[file_index].append(filepath)
    duplicate_dict = {}
    for file_index, path_list in filename_dict.items():
        if len(path_list) > 1:
            duplicate_dict[file_index] = path_list
    if len(duplicate_dict) > 0:
        return duplicate_dict
    return None


def print_duplicates(duplicates_dictionary):
    for (filename, filesize), path_list in duplicates_dictionary.items():
        print('{name}, file size is {size} bytes:'.format(name=filename,
                                                          size=filesize))
        print('\n'.join(path_list))
        print()


if __name__ == '__main__':
    args = parse_arguments()
    if not os.path.isdir(args.directory):
        exit("The specified directory doesn't exist!")
    duplicates = find_duplicates(args.directory)
    if duplicates is None:
        exit('There are no duplicates in the directory')
    print_duplicates(duplicates)
