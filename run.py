#!/usr/bin/python3

import os
import sys

#numa_policy = 'numactl --all'
#numa_policy = 'numactl --cpunodebind=0'
numa_policy = ''

#fio_path = 'fio-flex'
fio_path = 'fio'

fio_cmd_form = '%s %s ' \
        '--name=test --ioengine=%s ' \
        '--rw=%s ' \
        '--directory=%s ' \
        '--filesize=%s ' \
        '--bs=%s ' \
        '--thread --numjobs=%s ' \
        '2>&1 | tee %s'

echo_cmd_form = 'echo "%s" >> %s'

logname_form = '%s-%s-%s'

directory = '/mnt/pmem'

rw_list = ['read', 'write', 'randread', 'randwrite']

ioengine_list = ['sync']

numjobs_list = ['1', '2', '4', '8', '16', '32', '64', '128']

filesize = '4g'

blocksize = '4k'

# Colors
yellow = '\033[93m'
endc = '\033[0m'


def execute(cmd, output=False):
    if output:
        print(yellow + cmd + endc)
    os.system(cmd)


def make_dir(dir_name):
    if not os.path.isdir(dir_name):
        cmd = 'mkdir ' + dir_name
        execute(cmd)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('./run.py [testname]')
        sys.exit(1)

    testname = sys.argv[1]
    make_dir(testname)

    for ioengine in ioengine_list:
        for readwrite in rw_list:
            for numjobs in numjobs_list:
                logname = logname_form % (testname, readwrite, numjobs.zfill(3))
                logpath = testname + '/' + logname
                fio_cmd = fio_cmd_form % (numa_policy, fio_path, ioengine, readwrite, \
                        directory, filesize, blocksize, numjobs, logpath)
                execute(fio_cmd, True)

                echo_cmd = echo_cmd_form % (fio_cmd, logpath)
                execute(echo_cmd)

