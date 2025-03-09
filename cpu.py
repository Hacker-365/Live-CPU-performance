import psutil
import matplotlib.pyplot as plt
import time

def show_cpu_info():
    print("CPU Details:")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpu_freq = psutil.cpu_freq()
    print(f"Max Frequency: {cpu_freq.max:.2f}Mhz")
    print(f"Min Frequency: {cpu_freq.min:.2f}Mhz")
    print(f"Current Frequency: {cpu_freq.current:.2f}Mhz")
    print(f"CPU Usage per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def plot_cpu_usage(duration=3600):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    usage_data = []
    times = []

    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_usage = psutil.cpu_percent()
        usage_data.append(cpu_usage)
        times.append(time.time() - start_time)

        ax.clear()
        ax.plot(times, usage_data, label="CPU Usage (%)")
        ax.set_title("Real-time CPU Usage")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("CPU Usage (%)")
        ax.legend()
        ax.set_ylim(0, 100)
        plt.pause(0.1)  # Pause to update the plot

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    show_cpu_info()
    print("\nStarting real-time CPU usage graph...")
    plot_cpu_usage(duration=3600)  # Run for 10 seconds
