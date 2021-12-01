#!/usr/bin/python3

import os
import sys
import re


def summary(path):
    p = re.compile(r'\s*(WRITE|READ):\sbw=(?P<bw>\d*[.]*\d*)(?P<unit>(KiB|MiB|GiB))')
    file_list = os.listdir(path)
    file_list.sort()

    with open(path + '/results', 'w') as results:
        for filename in file_list:
            filepath = path + '/' + filename
            with open(filepath, 'r') as f:
                try:
                    lines = f.readlines()
                except UnicodeDecodeError as e:
                    print(filepath + ': ' + str(e))
                    continue

                completed = False
                bw_orig = bw = 0.0
                unit = ''

                for line in lines:
                    m = p.search(line)
                    if m:
                        bw_orig = float(m.group('bw'))
                        unit = m.group('unit')
                        if unit == 'GiB':
                            bw = bw_orig * 1000
                        elif unit == 'KiB':
                            bw = bw_orig / 1000
                        else:
                            bw = bw_orig
                        results.write(filename + ', ' + str(bw) + '\n')
                        completed = True

                if completed:
                    base_string = 'completed: %s, %s %s -> %s'
                    print(base_string % (filename, bw_orig, unit, bw))
                else:
                    base_string = 'failed: %s'
                    print(base_string % filename)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('./summary.py [result_dir]')
        sys.exit(1)
    path = sys.argv[1]
    summary(path)

