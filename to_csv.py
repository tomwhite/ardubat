# Converts the Ardubat log format to CSV for easier processing.
#
# Example usage:
#   python to_csv.py > datalog.csv
#

import re

def main():
    date = None
    print("date,time,minutes,activity_index,avg_freq,max_tbc")
    for line in open("DATALOG.TXT"):
        match = re.match(r"\d\d/\d\d/\d{4}", line)
        if match:
            date = match.group(0)
            continue
        match = re.match(r"(?P<time>\d\d:\d\d)\s+(?P<minutes>[+-]+)\s+AI:\s+(?P<ai>\d+)% - Avg.Freq:\s+(?P<avg_freq>\d+) kHz - MaxTBC:\s+(?P<max_tbc>\d+) mSecs", line)
        if match:
            time = match.group("time")
            minutes = match.group("minutes")
            activity_index = int(match.group("ai"))
            avg_freq = int(match.group("avg_freq"))
            max_tbc = int(match.group("max_tbc"))

            # if activity_index > 0:
            print(f"{date},{time},{minutes},{activity_index},{avg_freq},{max_tbc}")

if __name__ == "__main__":
    main()