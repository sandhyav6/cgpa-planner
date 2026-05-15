import streamlit as st

st.set_page_config(
    page_title="CGPA Planner",
    page_icon="🎓",
    layout="centered"
)

GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0
}

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_home():
    st.session_state.page = "home"


def go_tentative():
    st.session_state.page = "tentative"


def go_target():
    st.session_state.page = "target"


st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 20px;
    }

    div.stButton > button {
        min-height: 82px;
        border-radius: 18px;
        font-size: 18px;
        font-weight: 700;
        border: 1px solid #ddd;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }

    div.stButton > button:hover {
        transform: scale(1.01);
        border-color: #999;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Home Page
# -----------------------------
if st.session_state.page == "home":
    st.markdown("<div class='main-title'>🎓 CGPA Planner</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Choose what you want to calculate</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    left, middle, right = st.columns([2, 3, 2])

    with middle:
        if st.button("🧮 Calculate Tentative CGPA", use_container_width=True):
            go_tentative()
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🎯 Calculate Required GPA", use_container_width=True):
            go_target()
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    st.info(
        "Use this app to calculate your tentative CGPA using expected grades, "
        "or find the GPA you need this semester to reach a target CGPA."
    )

    st.caption(
        "Formula used: CGPA = sum of semester GPAs / number of semesters completed."
    )

# -----------------------------
# Tentative CGPA Page
# -----------------------------
elif st.session_state.page == "tentative":
    if st.button("⬅ Back to Home"):
        go_home()
        st.rerun()

    st.title("🧮 Calculate Tentative CGPA")
    st.write("Enter your current semester details and tentative grades.")

    current_semester = st.number_input(
        "Current semester number",
        min_value=1,
        max_value=8,
        value=None,
        step=1,
        placeholder="Enter current semester number"
    )

    current_cgpa = None

    if current_semester is not None:
        semesters_completed = current_semester - 1

        if current_semester == 1:
            current_cgpa = 0.0
            st.info("Since this is semester 1, your CGPA till now is considered 0.")
        else:
            current_cgpa = st.number_input(
                "CGPA till now",
                min_value=0.0,
                max_value=10.0,
                value=None,
                step=0.01,
                placeholder="Enter your CGPA till now"
            )

        credits_this_semester = st.number_input(
            "Credits this semester",
            min_value=1.0,
            max_value=40.0,
            value=None,
            step=1.0,
            placeholder="Enter total credits this semester"
        )

        num_subjects = st.number_input(
            "Number of subjects this semester",
            min_value=1,
            max_value=15,
            value=None,
            step=1,
            placeholder="Enter number of subjects"
        )

        semester_points = 0
        semester_credits_from_subjects = 0

        if num_subjects is not None:
            st.subheader("Subject Details")

            for i in range(1, num_subjects + 1):
                st.markdown(f"#### Subject {i}")

                col1, col2, col3 = st.columns([2, 1, 1])

                with col1:
                    st.text_input(
                        "Subject name",
                        value="",
                        placeholder="Enter subject name",
                        key=f"subject_name_{i}"
                    )

                with col2:
                    credit = st.number_input(
                        "Credits",
                        min_value=1.0,
                        max_value=10.0,
                        value=None,
                        step=1.0,
                        placeholder="Credits",
                        key=f"credit_{i}"
                    )

                with col3:
                    grade = st.selectbox(
                        "Tentative grade",
                        ["Select grade"] + list(GRADE_POINTS.keys()),
                        key=f"grade_{i}"
                    )

                if credit is not None and grade != "Select grade":
                    grade_point = GRADE_POINTS[grade]
                    semester_points += credit * grade_point
                    semester_credits_from_subjects += credit

            if st.button("Calculate Tentative CGPA"):
                if current_semester is None:
                    st.error("Please enter your current semester number.")
                elif current_cgpa is None:
                    st.error("Please enter your CGPA till now.")
                elif credits_this_semester is None:
                    st.error("Please enter credits this semester.")
                elif semester_credits_from_subjects == 0:
                    st.error("Please enter valid credits and grades for all subjects.")
                else:
                    previous_gpa_sum = current_cgpa * semesters_completed
                    current_semester_gpa = semester_points / semester_credits_from_subjects
                    tentative_cgpa = (
                        previous_gpa_sum + current_semester_gpa
                    ) / current_semester

                    st.markdown("---")
                    st.subheader("Result")

                    st.write(f"Current semester: **{current_semester}**")
                    st.write(f"Semesters completed before this: **{semesters_completed}**")
                    st.write(f"Current semester GPA: **{current_semester_gpa:.2f}**")
                    st.success(
                        f"Tentative CGPA after Semester {current_semester}: "
                        f"**{tentative_cgpa:.2f}**"
                    )

                    if tentative_cgpa >= 9:
                        st.balloons()
                        st.success("Congratulations! A CGPA above 9 is excellent. 🎉")
                    elif tentative_cgpa >= 8:
                        st.success("Great work! This is a strong CGPA.")
                    elif tentative_cgpa >= 7:
                        st.info("Good CGPA. You still have room to push higher.")
                    else:
                        st.warning("You can improve this with a stronger semester GPA.")
        else:
            st.info("Enter the number of subjects to add subject details.")


# -----------------------------
# Target CGPA Page
# -----------------------------
elif st.session_state.page == "target":
    if st.button("⬅ Back to Home"):
        go_home()
        st.rerun()

    st.title("🎯 Calculate Required GPA")
    st.write("Find the GPA you need this semester to reach your target CGPA.")

    current_semester = st.number_input(
        "Current semester number",
        min_value=1,
        max_value=8,
        value=None,
        step=1,
        placeholder="Enter current semester number",
        key="target_current_semester"
    )

    if current_semester is not None:
        semesters_completed = current_semester - 1

        if current_semester == 1:
            current_cgpa = 0.0
            st.info("Since this is semester 1, your CGPA till now is considered 0.")
        else:
            current_cgpa = st.number_input(
                "CGPA till now",
                min_value=0.0,
                max_value=10.0,
                value=None,
                step=0.01,
                placeholder="Enter your CGPA till now",
                key="target_current_cgpa"
            )

        credits_this_semester = st.number_input(
            "Credits this semester",
            min_value=1.0,
            max_value=40.0,
            value=None,
            step=1.0,
            placeholder="Enter total credits this semester",
            key="target_credits"
        )

        target_cgpa = st.number_input(
            "Target CGPA after this semester",
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.01,
            placeholder="Enter target CGPA",
            key="target_cgpa"
        )

        if st.button("Calculate Required GPA"):
            if current_cgpa is None:
                st.error("Please enter your CGPA till now.")
            elif credits_this_semester is None:
                st.error("Please enter credits this semester.")
            elif target_cgpa is None:
                st.error("Please enter your target CGPA.")
            else:
                previous_gpa_sum = current_cgpa * semesters_completed
                required_gpa = (target_cgpa * current_semester) - previous_gpa_sum

                st.markdown("---")
                st.subheader("Result")

                st.write(f"Current semester: **{current_semester}**")
                st.write(f"Semesters completed before this: **{semesters_completed}**")
                st.write(f"Current CGPA: **{current_cgpa:.2f}**")
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
    else:
        st.info("Enter your current semester number to continue.")

    st.caption(
        "Note: This calculator uses CGPA = sum of semester GPAs / number of semesters. "
        "Credits this semester is collected for academic context."
    )