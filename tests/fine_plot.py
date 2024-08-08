from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np

from orienteer.general.utils.calculations import calculate_fine


def main():
    time_values = [timedelta(minutes=t) for t in np.linspace(0, 60 * 24 * 14, 1000)]

    fine_mocviu = [calculate_fine(t) for t in time_values]

    pardon = [int(calculate_fine(t) * 2) for t in time_values]
    orientiks = [int(t.total_seconds() / 60 / 60 * 2) for t in time_values]

    time_seconds = [t.total_seconds() / 60 / 60 for t in time_values]

    plt.figure(figsize=(10, 6))
    plt.plot(time_seconds, fine_mocviu, label='Fine mocviu')
    plt.plot(time_seconds, pardon, label='Pardon')
    plt.plot(time_seconds, orientiks, label='Orientiks')
    plt.xlabel('Time (hours)')
    plt.ylabel('Fine Values')
    plt.title('Fine Values vs Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('fine_values_plot.png')