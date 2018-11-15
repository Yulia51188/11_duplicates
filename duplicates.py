import argparse
import os


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