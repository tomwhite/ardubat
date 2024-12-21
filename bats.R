library(tidyverse)
library(lubridate)

logging <- read_csv("datalog.csv") %>%
  filter(date >= "04/20/2024") %>%  # start date
  mutate(date = mdy(date))

bats <- logging %>%
  filter(activity_index > 0) %>%
  filter(max_tbc > 0)

bats %>%
  ggplot(aes(x=date, y=time)) +
  geom_point(aes(size=activity_index), alpha=0.4) +
  theme_minimal() +
  labs(
    title = "Bats at Berllan",
    subtitle = "Activity detected using ArduBat hardware",
    x = "Date",
    y = "Time",
    size = "Bat Activity Index"
  )

logging %>%
  ggplot(aes(x=date, y=time)) +
  geom_point(alpha=0.4) +
  theme_minimal() +
  labs(
    title = "Bats at Berllan",
    subtitle = "Detector enabled",
    x = "Date",
    y = "Time"
  )

# TODO:
# Reverse y scale so time goes down.
# Show every hour on y scale
# Show sunset/twilight bands
# Add background fill to indicate when the detector was running.

