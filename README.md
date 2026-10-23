# Student Performance Analytics System

A Python-based data analytics project that analyzes student marks and attendance to generate meaningful academic insights using NumPy and Pandas.

## About the Project

Student Performance Analytics System converts raw student records into useful information, including student grades, pass/fail status, attendance status, subject-wise performance, and department-wise analysis.

The project demonstrates fundamental Python programming, numerical computation, and data analysis through reusable functions and structured reports.

## Technologies Used

* **Python 3** — Core programming and logic
* **NumPy** — Numerical calculations and conditional operations
* **Pandas** — Data loading, filtering, grouping, and sorting
* **Git & GitHub** — Version control and project hosting
* **VS Code** — Development environment

## Dataset

The project uses `students.csv`, containing 20 student records with 9 original columns.

| Column           | Description                   |
| ---------------- | ----------------------------- |
| Student_ID       | Unique student identifier     |
| Name             | Student name                  |
| Department       | Student's academic department |
| Maths            | Mathematics marks             |
| Physics          | Physics marks                 |
| Chemistry        | Chemistry marks               |
| English          | English marks                 |
| Computer_Science | Computer Science marks        |
| Attendance       | Attendance percentage         |

The program calculates additional columns, including `Total`, `Average`, `Result`, `Grade`, and `Attendance_Status`.

## Key Features

* Calculates total marks and average marks for each student.
* Assigns grades based on academic performance.
* Determines pass/fail status using subject-wise passing criteria.
* Identifies students with low attendance.
* Generates class performance summaries.
* Analyzes subject-wise and department-wise performance.
* Identifies the top five performers.
* Exports the analyzed student records to `results.csv`.

## Grading Criteria

Grades are assigned according to the student's average marks. Students who fail in any subject receive an F grade.

| Average Marks         | Grade |
| --------------------- | ----- |
| 90 and above          | A+    |
| 80–89                 | A     |
| 70–79                 | B     |
| 60–69                 | C     |
| 50–59                 | D     |
| Below 50, if passed   | E     |
| Failed in any subject | F     |

**Passing criteria:** A student must score at least 40 marks in every subject to pass.

**Attendance criteria:** Attendance below 75% is classified as Low.

## Project Structure

```text
student-performance-analytics/
│
├── code/
│   ├── main.py
│   └── functions.py
│
├── data/
│   └── students.csv
│
├── results.csv
├── requirements.txt
└── README.md
```

* `main.py` — Controls program execution and displays the reports.
* `functions.py` — Contains reusable functions for calculations and analysis.
* `data/students.csv` — Input dataset.
* `results.csv` — Generated output containing analyzed student records.
* `requirements.txt` — Lists the required Python libraries.

## Sample Insights

Based on the current dataset, the analysis identifies:

* **Highest average:** Sneha Iyer and Divya Reddy — 92.4
* **Lowest average:** Vikram Rao — 41.8
* **Class average:** 69.9
* **Students passed:** 17 out of 20 (85%)
* **Students failed:** 3
* **Best-performing subject:** English — 75.25
* **Weakest subject:** Maths — 67.2
* **Best-performing department:** CSE — average of 83.47

These figures describe the current dataset and will depend on the input records.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/dakshita01/student-performance-analytics.git
```

### 2. Open the Project Directory

```bash
cd student-performance-analytics
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Program

```bash
python code/main.py
```

After execution, the program displays the analysis reports and generates `results.csv`.

## What I Learned

Through this project, I practiced:

* Working with CSV files and Pandas DataFrames.
* Performing numerical calculations using NumPy.
* Applying loops, conditions, and reusable functions.
* Analyzing grouped data using Pandas.
* Handling file paths and organizing a Python project.
* Using Git and GitHub for version control.

## Author

**Dakshita Biwal**

B.Tech Computer Science Engineering

[GitHub Profile](https://github.com/dakshita01)

---

*Developed as part of the Python with AI — EWB Courses, one-month internship project.*
