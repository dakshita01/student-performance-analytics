# Student Performance Analytics System

## Project Documentation

### 1. Project Overview

The Student Performance Analytics System is a Python-based project developed to analyze student academic performance and attendance. It processes student records stored in a CSV file and generates useful insights through numerical calculations, grading, and data analysis.

The project uses Python, NumPy, and Pandas to convert raw student marks into structured reports that help identify top performers, failing students, weak subjects, and department-wise performance.

### 2. Objectives

The main objectives of this project are:

* Calculate the total and average marks of each student.
* Assign grades and determine pass/fail status.
* Identify students with low attendance.
* Analyze class performance and individual subjects.
* Compare academic performance across departments.
* Identify the top five students.
* Export analyzed data to a CSV file.

### 3. Tools and Technologies

| Technology     | Purpose                                                              |
| -------------- | -------------------------------------------------------------------- |
| Python 3       | Implements the program logic using functions, loops, and conditions. |
| NumPy          | Performs numerical calculations and conditional operations.          |
| Pandas         | Loads, processes, filters, groups, and sorts student records.        |
| VS Code        | Provides the development environment.                                |
| Git and GitHub | Manage version control and host the project.                         |

### 4. Dataset Description

The input dataset, `students.csv`, contains 20 student records and nine columns.

| Column           | Description                        |
| ---------------- | ---------------------------------- |
| Student_ID       | Unique identifier for each student |
| Name             | Student's name                     |
| Department       | Student's department               |
| Maths            | Mathematics marks out of 100       |
| Physics          | Physics marks out of 100           |
| Chemistry        | Chemistry marks out of 100         |
| English          | English marks out of 100           |
| Computer_Science | Computer Science marks out of 100  |
| Attendance       | Attendance percentage              |

The program adds the following calculated columns:

* **Total:** Sum of marks across the five subjects.
* **Average:** Average marks across the five subjects.
* **Result:** Indicates whether the student passed or failed.
* **Grade:** Grade assigned according to the grading criteria.
* **Attendance_Status:** Indicates whether attendance is below the required threshold.

### 5. Project Structure

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
├── README.md
└── PROJECT_DOCUMENTATION.md
```

**File descriptions:**

* `main.py`: Controls program execution and displays the analysis reports.
* `functions.py`: Contains reusable functions for data processing and analysis.
* `data/students.csv`: Stores the input student records.
* `results.csv`: Stores the processed student records and calculated results.
* `requirements.txt`: Lists the Python libraries required to run the project.
* `README.md`: Provides a concise introduction and setup instructions.
* `PROJECT_DOCUMENTATION.md`: Describes the project's objectives, methodology, and implementation.

### 6. Implementation Details

The project is divided into reusable functions to keep the code organized and maintainable.

**6.1 Data Loading — `load_data()`**

Loads the CSV dataset into a Pandas DataFrame. The program displays the dataset dimensions, the first five records, and missing-value information.

**6.2 Total and Average Calculation — `calculate_total_and_average()`**

Converts the subject marks into a NumPy array. It uses `np.sum(axis=1)` to calculate total marks and `np.mean(axis=1)` to calculate average marks for each student.

**6.3 Pass/Fail Evaluation — `add_pass_fail()`**

Checks the marks obtained in each subject. A student passes only when they score at least 40 marks in every subject. NumPy's `np.all()` supports this condition.

**6.4 Grade Assignment — `add_grades()` and `assign_grade()`**

Assigns grades based on average marks. Students who fail in any subject receive an F grade, regardless of their overall average.

| Average Marks         | Grade |
| --------------------- | ----- |
| 90 and above          | A+    |
| 80–89.99              | A     |
| 70–79.99              | B     |
| 60–69.99              | C     |
| 50–59.99              | D     |
| Below 50, if passed   | E     |
| Failed in any subject | F     |

**6.5 Attendance Analysis — `add_attendance_status()`**

Uses `np.where()` to classify attendance below 75% as Low.

**6.6 Class Summary — `class_summary()`**

Calculates the class average, highest and lowest student averages, number of students who passed or failed, and overall pass percentage.

**6.7 Subject-wise Analysis — `subject_analysis()`**

Analyzes each subject to calculate its average, highest and lowest marks, pass percentage, and top-performing student.

**6.8 Department Analysis — `department_analysis()`**

Uses Pandas `groupby()` to compare academic performance across departments.

**6.9 Top Performers — `top_performers()`**

Sorts students by average marks in descending order and identifies the top five performers.

**6.10 Exporting Results**

Saves the processed student records, including calculated columns, to `results.csv`.

### 7. Key Features

The system provides the following functionality:

* Automated calculation of totals and averages.
* Rule-based grading and pass/fail evaluation.
* Identification of low-attendance students.
* Class-level performance summaries.
* Subject-wise performance comparison.
* Department-wise academic analysis.
* Identification of the top five performers.
* Export of processed records to CSV.

### 8. Execution Instructions

**Prerequisites:** Python 3 and the libraries listed in `requirements.txt`.

**Step 1: Open the project directory**

Open the project folder in VS Code.

**Step 2: Install dependencies**

Run the following command in the terminal from the project root:

```bash
python -m pip install -r requirements.txt
```

**Step 3: Execute the program**

```bash
python code/main.py
```

**Step 4: Review the output**

The program displays the dataset overview and analysis reports in the terminal. The processed student records are saved to `results.csv`.

### 9. Output and Analysis

The program generates student-level results and several analytical reports, including:

* Class performance summary.
* Subject-wise performance statistics.
* Department-wise performance comparison.
* Top five performers.
* Lists of failed students and students with low attendance.
* Processed student records in `results.csv`.

The analysis helps identify academic strengths and weaknesses within the dataset.

### 10. Challenges and Learning Outcomes

**Challenge 1: File Path Handling**

* **Problem:** The program initially raised a `FileNotFoundError` while attempting to load the CSV file.
* **Solution:** The file path was corrected to match the project directory structure.
* **Learning:** Relative file paths depend on the current working directory, so project structure and execution commands must be considered.

**Challenge 2: Defining Passing Criteria**

* **Problem:** A student's average alone may not accurately indicate whether they passed every subject.
* **Solution:** The program checks each subject individually and requires a minimum of 40 marks in every subject.
* **Learning:** Clearly defined conditions are essential for implementing accurate business rules.

**Technical Learning**

Through this project, I gained practical experience with:

* NumPy arrays and calculations along a specified axis.
* Pandas DataFrames, grouping, filtering, and sorting.
* Python functions, loops, and conditional statements.
* CSV file handling and relative file paths.
* Organizing code into reusable modules.
* Generating data-driven reports.

### 11. Conclusion

The Student Performance Analytics System demonstrates how Python, NumPy, and Pandas can be used to process student records and generate meaningful academic insights.

The project combines fundamental programming concepts with practical data analysis, producing structured reports that help evaluate individual, subject-wise, and department-wise performance.

It provides a foundation for developing more advanced data analytics applications.

### 12. Project Information

**Project:** Student Performance Analytics System

**Author:** Dakshita Biwal

**Course:** Python with AI — EWB Courses

**GitHub Repository:** https://github.com/dakshita01/student-performance-analytics
