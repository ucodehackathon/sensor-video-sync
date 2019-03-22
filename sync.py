import sys
import matplotlib.pyplot as plt
import adidasSensor
from adidasSensor.sync import sync_video

def getSyncedData(csv_file):
    synced = sync_video(
        csv_file=csv_file,
        best_candidate_begin=1967,
        best_candidate_end=4204,
        video_synch_init=2.7,
        video_synch_end=13.93,
        sampling_rate=500).values

    acc = synced[:, 0:3]
    gyr = synced[:, 3:6]
    time = synced[:, 6:7]

    return acc, gyr, time

def main():
    acc_raw, gyr_raw, time_raw = getSyncedData('./csv_file.csv')

    indexes = []

    times = []

    acc = []
    gyr = []
    time = []

    for index, (acc_value, gyr_value, time_value) in enumerate(zip(acc_raw, gyr_raw, time_raw)):
      if (time_value == 0):
        continue

      acc.append(acc_value)
      gyr.append(gyr_value)
      time.append(time_value)
    

    plt.figure()
    plt.suptitle('hack')

    ax1 = plt.subplot(211)
    plt.plot(time, acc)
    plt.ylabel('Linear acceleration [m/s^2]')

    ax2 = plt.subplot(212, sharex=ax1)
    plt.plot(time, gyr)
    plt.ylabel('Angular velocity [s]')

    plt.show()


if __name__ == "__main__":

    main()
