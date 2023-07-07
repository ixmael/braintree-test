import sys
import os.path


def read_input():
    '''
    This determines where comes the text. If a file name is setted, this read
    from that file. If the text comes from STDIN this read it.
    '''

    data_txt = ''

    if len(sys.argv) > 1:
        # The parameter is a file

        # Check if the file exist
        if not os.path.exists(sys.argv[1]):
            raise Exception('The file not exists')

        with open(sys.argv[1], 'r') as f:
            data_txt = f.read()
    elif not sys.stdin.isatty():
        # The script is called with sh/bash redirection
        data_txt = sys.stdin.read()
    else:
        raise Exception('There is not a data source')

    return data_txt
