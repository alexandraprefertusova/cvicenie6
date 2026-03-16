import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):

    fig, ax = plt.subplots()


    c1 = plt.Circle((circle_1['x'], circle_1['y']), circle_1['r'],
                    fill=False, color="blue", label="Kružnice 1")
    c2 = plt.Circle((circle_2['x'], circle_2['y']), circle_2['r'],
                    fill=False, color="red", label="Kružnice 2")


    ax.add_patch(c1)
    ax.add_patch(c2)

    ax.set_aspect("equal")

    limit = max(
        abs(circle_1['x']) + circle_1['r'],
        abs(circle_2['x']) + circle_2['r'],
        abs(circle_1['y']) + circle_1['r'],
        abs(circle_2['y']) + circle_2['r']
    ) + 1

    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Vizualizace průniku kružnic")
    plt.show()