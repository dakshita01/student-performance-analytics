# Reusable functions for the Student Performance Analytics System.

import numpy as np
import pandas as pd

PASS_MARK = 40            # a student must score >= 40 in EVERY subject
MIN_ATTENDANCE = 75       # attendance below 75% is flagged as "Low"

# A student who fails any subject gets grade F, whatever the average.

GRADE_RULES = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "E"),
]

def load_data(file_path):
    """Read the CSV file and return a pandas DataFrame."""
    return pd.read_csv(file_path)


def get_subject_columns(df):
    """Return the list of subject columns (everything except details)."""
    non_subject = ["Student_ID", "Name", "Department", "Attendance"]
    return [col for col in df.columns if col not in non_subject]


def calculate_total_and_average(df, subjects):
    """Add 'Total' and 'Average' columns using NumPy."""
    marks = df[subjects].to_numpy()                # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)            # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average, result):
    """Return the grade for one student. A failed student always gets F."""
    if result == "Fail":
        return "F"
    for minimum, grade in GRADE_RULES:
        if average >= minimum:
            return grade
    return "F"


def add_grades(df):
    """Add a 'Grade' column by looping over every student.
    Needs the 'Average' and 'Result' columns, so call it after add_pass_fail."""
    grades = []
    for avg, result in zip(df["Average"], df["Result"]):
        grades.append(assign_grade(avg, result))
    df["Grade"] = grades
    return df


def add_pass_fail(df, subjects):
    """Add 'Result' column: Pass only if every subject >= PASS_MARK."""
    results = []
    for _, row in df.iterrows():                   # loop over each student
        if np.all(row[subjects].to_numpy() >= PASS_MARK):
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    return df


def add_attendance_status(df):
    """Add 'Attendance_Status' column (Good / Low)."""
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "Good", "Low"
    )
    return df


def class_summary(df):
    """Return key class-level numbers as a dictionary."""
    averages = df["Average"].to_numpy()
    passed = int((df["Result"] == "Pass").sum())
    return {
        "total_students": len(df),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": float(np.max(averages)),
        "lowest_average": float(np.min(averages)),
        "passed": passed,
        "failed": len(df) - passed,
        "pass_percentage": round(passed / len(df) * 100, 2),
    }


def subject_analysis(df, subjects):
    """Return a DataFrame with average/highest/lowest/pass% per subject."""
    rows = []
    for subject in subjects:                       # loop over each subject
        scores = df[subject].to_numpy()
        topper = df.loc[df[subject].idxmax(), "Name"]
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(scores)), 2),
            "Highest": int(np.max(scores)),
            "Lowest": int(np.min(scores)),
            "Pass_%": round(float(np.mean(scores >= PASS_MARK) * 100), 1),
            "Topper": topper,
        })
    return pd.DataFrame(rows)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    ranked = df.sort_values("Average", ascending=False).head(n)
    ranked = ranked[["Student_ID", "Name", "Department",
                     "Total", "Average", "Grade"]]
    return ranked.reset_index(drop=True)


def department_analysis(df):
    """Return average marks, attendance and pass count per department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    )
    return summary.round(2).reset_index()
