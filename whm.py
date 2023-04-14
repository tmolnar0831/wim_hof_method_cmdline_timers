#!/usr/bin/env python

#
# Tom's Health Cafe Wim Hof Method breathing timer
# URL: https://tomsitcafe.com
#

import time
import argparse
from progress.bar import Bar

def round(round_num, breath_count, retention_times, recovery_time):
    print(f'Round {round_num}')
    bar = Bar('Circular, deep breaths', max=breath_count)
    for breathe in range(breath_count):
        bar.next()
        time.sleep(3) # 3 second for every breath in and out
    bar.finish()

    bar = Bar('Let it go and hold', max=retention_times[round_num-1])
    for retention in range(retention_times[round_num-1]):
        bar.next()
        time.sleep(1)
    bar.finish()

    bar = Bar('Take a deep breath and hold', max=recovery_time)
    for recoverybreath in range(recovery_time):
        bar.next()
        time.sleep(1)
    bar.finish()

def main():
    parser = argparse.ArgumentParser(description='Tom\'s Health Cafe - Wim Hof breathing timer')
    parser.add_argument('--breaths', type=int, default=30,
                        help='Number of breaths per round')
    parser.add_argument('--retentions', type=int, nargs=3,
                        default=[30, 60, 90], help='Retention times in seconds')
    parser.add_argument('--recovery', type=int, default=15,
                        help='Recovery time in seconds')
    parser.add_argument('--rounds', type=int, default=3,
                        help='Number of rounds')
    args = parser.parse_args()

    for i in range(args.rounds):
        round(i+1, args.breaths, args.retentions, args.recovery)

if __name__ == '__main__':
    main()