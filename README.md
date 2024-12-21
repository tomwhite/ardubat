# Ardubat

Copy the data from the SD card to here:

```shell
cp /Volumes/NO\ NAME/DATALOG.TXT ~/projects-workspace/ardubat
```

Convert to CSV:

```shell
python to_csv.py > datalog.csv
```

Then run code in `bats.R` in RStudio to get a plot.
