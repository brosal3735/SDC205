# PA_PandasGraphics.py
import pandas as pd
import matplotlib.pyplot as plt

def main():
    student_id = "Brosal3735"
    print(student_id)
    print()

    ballroom_names = ["Ballroom 1", "Ballroom 2", "Ballroom 3"]
    ballroom_capacity = [25000, 11000, 5000]

    demo_labels = ["Children", "Adults", "Teens"]
    demo_counts = [18000, 13000, 10000]

    df_capacity = pd.DataFrame({"Names": ballroom_names, "Capacity": ballroom_capacity})
    print(df_capacity)
    print()

    # Bar chart
    fig1 = plt.figure()
    plt.bar(ballroom_names, ballroom_capacity, label="Capacity")
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()          # Close this window to continue
    plt.close(fig1)     # Important in IDLE

    # Pie chart
    fig2 = plt.figure()
    plt.pie(demo_counts, labels=demo_labels)
    plt.ylabel("Attendees")
    plt.legend(demo_labels, loc="upper right")
    plt.tight_layout()
    plt.show()
    plt.close(fig2)

if __name__ == "__main__":
    main()



