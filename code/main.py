import pandas as pd
from functions import (
    load_data, get_subject_columns, calculate_total_and_average,
    add_grades, add_pass_fail, add_attendance_status, class_summary,
    subject_analysis, top_performers, department_analysis,
)

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)


def print_heading(title):
    """Print a neat section heading."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Read the data 
    df = load_data("data/students.csv")
    subjects = get_subject_columns(df)

    print_heading("1. DATASET OVERVIEW")
    print("Number of records :", df.shape[0])
    print("Number of columns :", df.shape[1])
    print("Subjects          :", ", ".join(subjects))
    print("\nFirst 5 records:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum().to_string())

    # Process the data 
    df = calculate_total_and_average(df, subjects)
    df = add_pass_fail(df, subjects)
    df = add_grades(df)
    df = add_attendance_status(df)

    print_heading("2. STUDENT-WISE RESULT")
    print(df[["Student_ID", "Name", "Total", "Average",
              "Grade", "Result", "Attendance_Status"]].to_string(index=False))

    # Analysis 
    summary = class_summary(df)
    best = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    print_heading("3. CLASS SUMMARY")
    print("Total students    :", summary["total_students"])
    print("Class average     :", summary["class_average"])
    print("Highest average   :", summary["highest_average"], "-", best["Name"])
    print("Lowest average    :", summary["lowest_average"], "-", lowest["Name"])
    print("Students passed   :", summary["passed"])
    print("Students failed   :", summary["failed"])
    print("Pass percentage   :", summary["pass_percentage"], "%")

    print("\nGrade distribution:")
    print(df["Grade"].value_counts().sort_index().to_string())

    print("\nFailed students:")
    failed = df[df["Result"] == "Fail"]
    print(failed[["Student_ID", "Name", "Department", "Average"]]
          .to_string(index=False))

    print("\nStudents with low attendance (< 75%):")
    low_att = df[df["Attendance_Status"] == "Low"]
    print(low_att[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    print_heading("4. SUBJECT-WISE ANALYSIS")
    subject_table = subject_analysis(df, subjects)
    print(subject_table.to_string(index=False))
    best_subject = subject_table.loc[subject_table["Average"].idxmax()]
    weak_subject = subject_table.loc[subject_table["Average"].idxmin()]
    print("\nBest subject (highest average) :", best_subject["Subject"])
    print("Weakest subject (lowest average):", weak_subject["Subject"])

    print_heading("5. DEPARTMENT-WISE ANALYSIS")
    print(department_analysis(df).to_string(index=False))

    print_heading("6. TOP 5 PERFORMING STUDENTS")
    print(top_performers(df, 5).to_string(index=False))

    # Save the final results
    df.to_csv("results.csv", index=False)
    print("\nFull results saved to results.csv")


if __name__ == "__main__":
    main()
