# fio-experiments-on-numa
This provides python scripts for [FIO](https://github.com/axboe/fio) experiments.

1. Edit the ```run.py``` file to set up experimental parameters.
2. Run the ```run.py``` with the directory name where the experimental results will be written.
```
$ ./run.py dirname
```
3. After the experiments, run the ```summary.py``` to summarize the experiment results.
```
$ ./summary.py dirname
```
