"""
Count frequency of each word in txt files.
Count all txt files in current directory: $ python poem_word_count.py
Count all txt files in the selected directory: $ python poem_word_count.py --path 'folder_name'
Count a list of selected files in current directory: $ python peom_word_count.py --list poem1.txt poem2.txt ...
Count a list of selected files in the selected directory: $ python peom_word_count.py --path 'folder_name' --list poem1.txt poem2.txt ...
"""

from pathlib import Path#
import argparse


def file_word_count(file):
    word_count = {}
    with open(file, 'r') as fi:
        # read file word by word
        for line in fi:
            for word in line.split():
                # check if the word already exist in the word count dictionary
                if word.lower() in word_count:
                    # if yes, increase the value of the word by one
                    word_count[word.lower()] += 1
                else:
                    # if not, add this word as key in the dictionary with 1 as value
                    word_count[word.lower()] = 1
    # sort the dictionary by descending order of value
    # items() returns a list of the dict's key-value pairs
    # sort() sorts the list by values (item[1])
    # key=lambda returns the second element of each item (the score).
    # default sort in ascending order, thus when descending, reverse=True
    # dict() converts them back to a dictionary
    word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return word_count


def make_report(file_name, word_count):
    with open(f'./reports/{file_name}_reports.txt', 'w') as fi:
        # loop through each key value pair
        for key, value in word_count.items():
            # write each key value pair in the form of key:value and newline
            fi.write('%s:%s\n' % (key, value))


# create a new folder for reports
report_path = Path('reports')
if not report_path.exists():
    report_path.mkdir()


# user input files
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word Counter')
    parser.add_argument('--path', type=Path)
    parser.add_argument('--list', nargs='*', action='store', type=str)
    args = parser.parse_args()

    # if a path argument is supplied, process files from the supplied path
    if args.path:
        # if a list of files are supplied, apply word counter to the list of files
        if args.list:
            for item in args.list:
                for file in args.path.glob(item):
                    file_name = Path(file).name.split('.')[0]
                    word_count = file_word_count(file)
                    make_report(file_name, word_count)
        # if no list is supplied, apply word counter to all the txt files in the folder
        else:
            for file in args.path.glob('*.txt'):
                word_count = file_word_count(file)
                # retireve the file name
                file_name = Path(file).name.split('.')[0]
                make_report(file_name, word_count)
    # if no path argument is supplied, process from the current working directory
    else:
        # if a list of files are supplied, apply word counter to the list of files
        if args.list:
            for file in args.list:
                word_count = file_word_count(file)
                # retireve the file name
                file_name = Path(file).name.split('.')[0]
                make_report(file_name, word_count)
        # if no list is supplied, apply word counter to all the txt files in the current folder
        else:
            for file in Path().glob('*.txt'):
                word_count = file_word_count(file)
                # retireve the file name
                file_name = Path(file).name.split('.')[0]
                make_report(file_name, word_count)
    print('Word frequency in files counted successfully.')
