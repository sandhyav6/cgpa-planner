import streamlit as st

st.set_page_config(
    page_title="CGPA Planner",
    page_icon="🎓",
    layout="centered",
)

GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8, 
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0,
}

st.title("🎓 CGPA Planner")
st.write("Calculate your tentative CGPA or find the GPA needed to reach your target CGPA.")

st.markdown("---")

option = st.radio(
    "What do you want to calculate?",
    ["Calculate Tentative CGPA", 
     "Calculate Required GPA for Target CGPA"
    ]
)

st.markdown("---")

if option == "Calculate Tentative CGPA":
    st.header("🧮 Calculate Tentative CGPA")

    current_semester = st.number_input(
        "Current semester number",
        min_value=1,
        max_value=8,
        value=4,
        step=1
    )

    semesters_completed = current_semester - 1

    current_cgpa = st.number_input(
        "CGPA till now",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.01
    )

    credits_this_semester = st.number_input(
        "Credits in current semester",
        min_value=16.0,
        max_value=30.0,
        value=20.0,
        step=1.0
    )

    num_subjects = st.number_input(
        "Number of subjects in current semester",
        min_value=3,
        max_value=10,
        value=5,
        step=1
    )

    st.subheader("Enter Subject Details")

    semester_points = 0
    semester_credits_from_subjects = 0

    for i in range(num_subjects+1):
        st.markdown(f"### Subject {i}")

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            st.text_input(
                "Subject Name",
                value=f"Subject {i}",
                key=f"subject_name_{i}"
            )
        with col2:
            credits = st.number_input(
                "Credits",
                min_value=1.0,
                max_value=4.0,
                value=3.0,
                step=0.5,
                key=f"credits_{i}"
            )
        with col3:
            grade = st.selectbox(
                "Tentative Grade",
                options=list(GRADE_POINTS.keys()),
                key=f"grade_{i}"
            )
        grade_point = GRADE_POINTS[grade]
        semester_points += grade_point * credits
        semester_credits_from_subjects += credits
    
    if st.button("Calculate Tentative CGPA"):
        if semesters_completed == 0:
            previous_gpa_sum = 0
        else:
            previous_gpa_sum = current_cgpa * semesters_completed

        current_semester_gpa = semester_points / semester_credits_from_subjects
        tentative_cgpa = (previous_gpa_sum + current_semester_gpa) / current_semester

        st.markdown("---")
        st.subheader("Result")

        st.write(f"Current semester: **{current_semester}**")
        st.write(f"Semesters completed before this: **{semesters_completed}**")
        st.write(f"CGPA till now: **{current_cgpa:.2f}**")
        st.write(f"Credits this semester: **{credits_this_semester:.0f}**")
        st.write(f"Calculated GPA for this semester: **{current_semester_gpa:.2f}**")
        st.success(f"Tentative CGPA after Semester {current_semester}: **{tentative_cgpa:.2f}**")

        if tentative_cgpa >= 9:
            st.balloons()
            st.success("Congratulations! A CGPA above 9 is excellent. 🎉")
        elif tentative_cgpa >= 8:
            st.success("Great work! This is a strong CGPA.")
        elif tentative_cgpa >= 7:
            st.info("Good CGPA. You still have room to push higher.")
        else:
            st.warning("You can improve this with a stronger semester GPA.")


elif option == "Calculate GPA for Target CGPA":
    st.header("🎯 Calculate GPA for Target CGPA")

    current_semester = st.number_input(
        "Current semester number",
        min_value=1,
        max_value=8,
        value=4,
        step=1
    )

    semesters_completed = current_semester - 1

    current_cgpa = st.number_input(
        "CGPA till now",
        min_value=0.0,
        max_value=10.0,
        value=8.0,
        step=0.01
    )

    credits_this_semester = st.number_input(
        "Credits this semester",
        min_value=1.0,
        max_value=40.0,
        value=20.0,
        step=1.0
    )

    target_cgpa = st.number_input(
        "Target CGPA after this semester",
        min_value=0.0,
        max_value=10.0,
        value=9.0,
        step=0.01
    )

    if st.button("Calculate Required GPA"):
        if semesters_completed == 0:
            previous_gpa_sum = 0
        else:
            previous_gpa_sum = current_cgpa * semesters_completed

        required_gpa = (target_cgpa * current_semester) - previous_gpa_sum

        st.markdown("---")
        st.subheader("Result")

        st.write(f"Current semester: **{current_semester}**")
        st.write(f"Semesters completed before this: **{semesters_completed}**")
        st.write(f"CGPA till now: **{current_cgpa:.2f}**")
        st.write(f"Credits this semester: **{credits_this_semester:.0f}**")
        st.write(f"Target CGPA: **{target_cgpa:.2f}**")

        if required_gpa > 10:
            st.error(
                f"You need a GPA of **{required_gpa:.2f}**, which is above 10. "
                "So this target is not possible in this semester alone."
            )
        elif required_gpa < 0:
            st.success(
                "Your current CGPA is already higher than this target. "
                "You do not need a specific minimum GPA this semester for this goal."
            )
        else:
            st.success(f"You need a GPA of **{required_gpa:.2f}** this semester.")

            if required_gpa >= 9:
                st.info("This is an ambitious target, but possible.")
            elif required_gpa >= 8:
                st.info("This is a strong and realistic target.")
            else:
                st.info("This target looks comfortable based on your current CGPA.")

        if target_cgpa >= 9:
            st.balloons()
            st.success("Congratulations! A target CGPA above 9 is excellent. 🎉")

st.markdown("---")
st.caption(
    "Note: This calculator uses CGPA = sum of semester GPAs / number of semesters. "
    "Semester GPA is calculated using subject credits and grades."
)
