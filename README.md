# CGPA Planner

A simple and useful Streamlit web app that helps college students calculate their tentative CGPA and find the GPA they need in the current semester to reach a target CGPA.

This project started with a very normal student problem:

**“What will my CGPA become after this semester?”**

and

**“What GPA do I need this semester to reach my target CGPA?”**

Instead of just guessing, I built a small solution for it using Streamlit.

---

## Live Demo

https://sandhyav6-cgpa-calculator.streamlit.app/

---

## About the Project

I wanted to learn **Streamlit** because I plan to build better Machine Learning projects in the future.

Jupyter Notebooks are useful for experimenting, training models, and understanding data. But real ML projects also need an interface where users can enter inputs, interact with the system, and see useful results clearly.

So before directly jumping into bigger ML deployments, I decided to start small.

I took a daily college problem, not knowing how my GPA and CGPA might turn out, and built a simple Streamlit app to solve it.

This is a small project, but it helped me practice turning logic into a real interactive app.

---

## Features

- Calculate tentative CGPA after the current semester
- Calculate the GPA required this semester to reach a target CGPA
- Supports up to 8 semesters
- Uses two clear options on the home page
- Allows subject-wise credit and tentative grade entry
- Calculates current semester GPA using credits and grades
- Shows whether a target CGPA is possible
- Congratulates the user if the CGPA is above 9
- Uses Streamlit session state for simple page navigation
- Clean and beginner-friendly UI

---

## How the Calculation Works

This app follows the CGPA logic:

```text
CGPA = Sum of semester GPAs / Number of semesters completed
```

For example, if a student completed 3 semesters and has a CGPA of 8.5:

```text
Sum of previous GPAs = 8.5 × 3 = 25.5
```

If the current semester is Semester 4 and the tentative GPA is 9.2:

```text
New CGPA = (25.5 + 9.2) / 4
New CGPA = 8.675
```

So the tentative CGPA becomes:

```text
8.68
```

---

## GPA Needed for Target CGPA

To calculate the GPA needed in the current semester:

```text
Required GPA = (Target CGPA × Current Semester Number) - Sum of Previous GPAs
```

Example:

```text
Current semester = 4
CGPA till now = 8.5
Target CGPA = 9.0

Semesters completed before this = 3
Sum of previous GPAs = 8.5 × 3 = 25.5

Required GPA = (9.0 × 4) - 25.5
Required GPA = 10.5
```

Since GPA is out of 10, the app will show that this target is not possible in the current semester alone.

---

## Grade Point Mapping

The app uses the following grade mapping:

| Grade | Grade Point |
|---|---:|
| S | 10 |
| A | 9 |
| B | 8 |
| C | 7 |
| D | 6 |
| E | 5 |
| F | 0 |

---

## Tech Stack

- Python
- Streamlit
- Streamlit Community Cloud

---

## Project Structure

```text
cgpa-planner/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

Move into the project folder:

```bash
cd your-repo-name
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

---

## Requirements

The project only needs Streamlit.

```text
streamlit
```

---

## Deployment

This app is deployed using **Streamlit Community Cloud**.

To deploy:

1. Push the project to GitHub.
2. Go to Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Set the main file path as:

```text
app.py
```

6. Deploy the app.

---

## Why I Built This

I built this project as a small but meaningful step toward improving my skills in creating real-world applications.

Since I want to work on better Machine Learning projects, I knew I needed to go beyond notebooks. I needed to understand how to build simple user interfaces, take inputs, process them, and show useful results.

This CGPA Planner helped me practice exactly that.

It may be a small project, but it taught me how to:

- Build an interactive web app using Streamlit
- Handle user inputs
- Use conditional page navigation
- Apply calculation logic in a real use case
- Deploy a Python app to the cloud
- Turn a common student problem into a working solution

---

## Future Improvements

Some features I can add later:

- Save previous calculations
- Add custom grade point systems
- Add percentage conversion
- Add downloadable result report
- Add better mobile responsiveness
- Add semester-wise history
- Add a target planner for multiple future semesters
- Add a cleaner dashboard-style result page

---

## Final Note

This project is not meant to be overly complex.

It is a small project built with a clear purpose:

**to learn Streamlit, solve a real student problem, and take one step closer to building better ML-ready applications.**
