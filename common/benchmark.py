import os
import subprocess
import time
import pandas as pd

results = []

SOLVER_PATH = '../Module-2-Knapsack/knapsack/solver.py'
DATA_DIR = '../Module-2-Knapsack/knapsack/data/'
OUTPUT_PATH = '../Module-2-Knapsack/knapsack/benchmark.md'
TARGET_DATASETS = ['ks_lecture_dp_1', 'ks_lecture_dp_2', 'ks_4_0', 'ks_19_0', 'ks_30_0', 'ks_40_0']#, 'ks_45_0', 'ks_50_0', 'ks_50_1', 'ks_60_0']

for filename in os.listdir(DATA_DIR):
    if filename not in TARGET_DATASETS:
        print("Skipped dataset " + filename)
        results.append([filename, "inf", "out of memory"]) # this line is only for dynamic programming
        continue
    else:
        print("Solving dataset " + filename)

    start_time = time.time()

    process = subprocess.Popen(['python', SOLVER_PATH, DATA_DIR + filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    end_time = time.time()
    runtime = end_time - start_time
    print("Solved dataset " + filename)

    obj_val = output.decode().split()[0]

    results.append([filename, str(round(runtime, 5)) +"sec", obj_val])


df = pd.DataFrame(results, columns=['Dataset', 'Runtime', 'Result'])

df.to_markdown(OUTPUT_PATH, index=False)