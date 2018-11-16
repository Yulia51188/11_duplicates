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
    file_tree = os.walk(directory)
    filename_dict = {}
    for address, dirs, files in file_tree:
        for filename in files:
            filepath = os.path.join(address, filename)
            filesize = os.path.getsize(filepath)
            file_index = (filename, filesize)
            if file_index in filename_dict:
                filename_dict[file_index].append(filepath)
            else:
                filename_dict[file_index] = [filepath]
    duplicate_dict = {}
    for file_index, path_list in filename_dict.items():
        if len(path_list) > 1:
            duplicate_dict[file_index] = path_list
    return duplicate_dict


if __name__ == '__main__':
    args = parse_arguments()
    if not os.path.exists(args.directory):
        exit("The specified directory doesn't exist!")
    duplicates = find_duplicates(args.directory)
    if duplicates is None:
        exit('There are no duplicates in the directory')
    print(duplicates)
    for fileindex, path_list in duplicates.items():
        filename, filesize = fileindex
        print('{name}, file size is {size} bytes:'.format(name=filename,
                                                          size=filesize))
        for filepath in path_list:
            print(filepath)
        print()