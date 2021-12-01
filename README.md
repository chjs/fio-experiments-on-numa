# fio-experiments-on-numa
This provides python scripts for [FIO](https://github.com/axboe/fio) experiments.

## Getting Started

1. Edit the ```run.py``` file to set up experimental parameters. (_e.g._, NUMA policy, ioengien, workload and so on) 
2. Run the ```run.py``` with the directory name where the experimental results will be written.
```
$ ./run.py dirname
```
3. After the experiments, run the ```summary.py``` to summarize the experiment results.
```
$ ./summary.py dirname
```
