import argparse


def count_string(string):
    char_num = len(string)
    print(char_num)
    return char_num


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Character Counter')
    parser.add_argument('--string', action='store', type=str)
    results = parser.parse_args()
    string = results.string

    count_string(string)
