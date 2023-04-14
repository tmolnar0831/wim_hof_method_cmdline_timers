# Wim Hof Method command line breathing timer scripts

These scripts are for exercising the Wim Hof Method breathing with timers in the command line interface.

More info: https://www.wimhofmethod.com/breathing-exercises

I plan to build more sophisticated scripts and there is the possibility of a graphical interface in the future.

Visit my website: https://tomsitcafe.com

# Scripts

## whm.py

This is a simple Python3 script with a simple user interface for setting the breathing rounds, the number of breaths, the retention time and the recovery breath time.

The script requires the `progress.bar` library.

Install it with 

```
pip install progress
```

then the script is functional.

**Usage:**

```
usage: whm.py [-h] [--breaths BREATHS] [--retentions RETENTIONS RETENTIONS RETENTIONS] [--recovery RECOVERY] [--rounds ROUNDS]

optional arguments:
  -h, --help            show this help message and exit
  --breaths BREATHS     Number of breaths per round
  --retentions RETENTIONS RETENTIONS RETENTIONS
                        Retention times in seconds
  --recovery RECOVERY   Recovery time in seconds
  --rounds ROUNDS       Number of rounds
```

**Defaults:**

- 3 rounds
- 30 breaths per round
- 30, 60 and 90 seconds retentions
- 15 seconds recovery breaths

## whm.sh

Basic shell script written in BASH for even simpler environments.

**Usage:**

```
./whm.sh
```

The first lines of the script can be modified to change the default breathing session.

**Defaults:**

- 3 rounds
- 30 breaths per round
- 30, 60 and 90 seconds retentions
- 15 seconds recovery breaths

# Author

Tamas Molnar - <tmolnar0831@gmail.com> - https://tomsitcafe.com

# License

MIT