import matplotlib.pyplot as plt

def load_signal_from_txt(path):
    with open(path, "r") as f:
        return [float(line.strip()) for line in f]


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values):
    plt.plot(values)
    plt.title("Signal")
    plt.xlabel("Sample")
    plt.ylabel("Value")
    plt.show()



if __name__ == "__main__":

    values = load_signal_from_txt("ekg_signal.txt")

    print("Min:", signal_min(values))
    print("Max:", signal_max(values))
    print("Avg:", signal_avg(values))

    plot_signal(values)