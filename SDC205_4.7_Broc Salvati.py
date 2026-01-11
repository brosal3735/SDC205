# Performance Assessment: Advanced Pandas
# Student ID: Brosal3735

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # 1. Print student ID
    print("Brosal3735")

    # 2. Store a classroom roster of 10 students in an array
    students = [
        "Alex", "Brooke", "Chris", "Dana", "Evan",
        "Faith", "George", "Hannah", "Ian", "Julia"
    ]

    # Store subject names (two subjects per student)
    subjects = ["Math", "Science"] * 10

    # Store grades for each student and subject
    grades = [
        90, 85, 88, 92, 76, 80, 84, 79, 91, 87,
        89, 90, 93, 88, 85, 82, 78, 86, 94, 91
    ]

    # 3. Create a MultiIndex for student and subject
    index = pd.MultiIndex.from_arrays(
        [students * 2, subjects],
        names=("Student", "Subject")
    )

    # 4. Create a DataFrame of grades for each student for two subjects
    df = pd.DataFrame({"Grade": grades}, index=index)

    # 5. Display the DataFrame
    print(df)

    # 6. Group by the mean of the subject
    subject_means = df.groupby("Subject").mean()
    print(subject_means)

    # 7. Display the vertical bar graph
    subject_means.plot(
        kind="bar",
        legend=False
    )

    plt.xlabel("Subject")
    plt.ylabel("Average Grade")
    plt.title("Average Grade by Subject")
    plt.xticks(rotation=0)
    plt.show()


if __name__ == "__main__":
    main()


