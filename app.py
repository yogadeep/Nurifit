
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Health and Nutrition", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":

    st.title("Health and Nutrition")
    st.write("Choose a section to continue.")
    st.header("Choose an option")

    if st.button("Health Calculator", use_container_width=True):
        st.session_state.page = "Health Calculator"
        st.rerun()

    if st.button("Diet Calculator", use_container_width=True):
        st.session_state.page = "Diet Calculator"
        st.rerun()

    if st.button("Healthy Food vs Junk Food", use_container_width=True):
        st.session_state.page = "Healthy Food vs Junk Food"
        st.rerun()

elif st.session_state.page == "Health Calculator":

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("Health Calculator")
    st.write("BMI Calculator, Weight Checker and Daily Food Calorie Calculator")

    # 1. BMI CALCULATOR

    st.header("1. BMI Calculator")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=None
    )

    weight = st.number_input(
        "Enter your weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=None
    )

    height = st.number_input(
        "Enter your height (cm)",
        min_value=50,
        max_value=250,
        value=None
    )

    if st.button("Calculate BMI"):

        if age is None or weight is None or height is None:
            st.warning("Please enter all the details.")

        else:
            height_m = height / 100
            bmi = weight / (height_m * height_m)

            st.write("Your BMI is:", round(bmi, 2))

            if bmi < 18.5:
                category = "Below usual range"
            elif bmi < 25:
                category = "Usual range"
            elif bmi < 30:
                category = "Above usual range"
            else:
                category = "Well above usual range"

            st.write("Your category is:", category)

            categories = [
                "Below usual range",
                "Usual range",
                "Above usual range",
                "Well above usual range"
            ]

            values = [15, 55, 20, 10]

            explode = []

            for item in categories:
                if item == category:
                    explode.append(0.1)
                else:
                    explode.append(0)

            fig, ax = plt.subplots()

            ax.pie(
                values,
                labels=categories,
                explode=explode,
                autopct="%1.0f%%",
                startangle=90
            )

            ax.set_title("BMI Categories")

            st.pyplot(fig)
            plt.close(fig)

            st.info(
                "The highlighted part shows your category. "
                "The percentages are illustrative values for the "
                "project and are not actual population statistics."
            )

            if age < 20:
                st.warning(
                    "For people below 20, BMI is normally interpreted "
                    "using age- and sex-specific growth charts."
                )

    # 2. WEIGHT CHECKER

    st.divider()
    st.header("2. Weight Checker")

    weight_age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=None,
        key="weight_age"
    )

    weight_value = st.number_input(
        "Enter your weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=None,
        key="weight_value"
    )

    if st.button("Check Weight"):

        if weight_age is None or weight_value is None:
            st.warning("Please enter age and weight.")

        else:

            if weight_age < 20:

                if weight_value < 40:
                    weight_category = "Underweight"
                elif weight_value <= 60:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            elif weight_age <= 30:

                if weight_value < 50:
                    weight_category = "Underweight"
                elif weight_value <= 70:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            elif weight_age <= 40:

                if weight_value < 55:
                    weight_category = "Underweight"
                elif weight_value <= 75:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            elif weight_age <= 50:

                if weight_value < 55:
                    weight_category = "Underweight"
                elif weight_value <= 80:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            elif weight_age <= 60:

                if weight_value < 55:
                    weight_category = "Underweight"
                elif weight_value <= 80:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            else:

                if weight_value < 50:
                    weight_category = "Underweight"
                elif weight_value <= 80:
                    weight_category = "Normal"
                else:
                    weight_category = "Above average"

            st.write("Your category is:", weight_category)

            categories = [
                "Underweight",
                "Normal",
                "Above average"
            ]

            values = [15, 60, 25]

            explode = []

            for item in categories:
                if item == weight_category:
                    explode.append(0.1)
                else:
                    explode.append(0)

            fig, ax = plt.subplots()

            ax.pie(
                values,
                labels=categories,
                explode=explode,
                autopct="%1.0f%%",
                startangle=90
            )

            ax.set_title("Weight Categories")

            st.pyplot(fig)
            plt.close(fig)

            st.info(
                "The highlighted part shows your category. "
                "The percentages are illustrative values for the project."
            )

            if weight_category == "Underweight":

                st.write("### General Healthy Habits")
                st.write("- Eat regular balanced meals.")
                st.write("- Include rice, roti, dal, beans, eggs, milk, fruits and vegetables.")
                st.write("- Avoid skipping meals.")
                st.write("- Get enough sleep.")

            elif weight_category == "Normal":

                st.write("### General Healthy Habits")
                st.write("- Eat a balanced diet.")
                st.write("- Include vegetables and fruits.")
                st.write("- Include whole grains and protein-rich foods.")
                st.write("- Drink enough water.")
                st.write("- Stay physically active.")

            else:

                st.write("### General Healthy Habits")
                st.write("- Eat balanced meals.")
                st.write("- Include vegetables and fruits.")
                st.write("- Include whole grains and protein-rich foods.")
                st.write("- Limit highly processed foods and foods with a lot of added sugar.")
                st.write("- Stay physically active.")

    # 3. DAILY FOOD CALORIE CALCULATOR

    st.divider()
    st.header("3. Daily Food Calorie Calculator")

    st.write(
        "Enter the food you ate during the day and its estimated calories."
    )

    calorie_age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=None,
        key="calorie_age"
    )

    total_calories = 0

    for i in range(1, 6):

        st.subheader("Food " + str(i))

        food_name = st.text_input(
            "Enter food name",
            key="food_name" + str(i)
        )

        calories = st.number_input(
            "Enter estimated calories (kcal)",
            min_value=0.0,
            value=0.0,
            key="food_calories" + str(i)
        )

        total_calories += calories

    if st.button("Calculate Total Calories"):

        if calorie_age is None:
            st.warning("Please enter your age.")

        elif total_calories == 0:
            st.warning("Please enter the food items and their calories.")

        else:

            st.write(
                "Total daily calories:",
                round(total_calories),
                "kcal"
            )

            if calorie_age <= 3:
                minimum = 1000
                maximum = 1400

            elif calorie_age <= 8:
                minimum = 1200
                maximum = 2000

            elif calorie_age <= 13:
                minimum = 1400
                maximum = 2600

            elif calorie_age <= 18:
                minimum = 1800
                maximum = 3200

            elif calorie_age <= 30:
                minimum = 1800
                maximum = 3000

            elif calorie_age <= 50:
                minimum = 1800
                maximum = 3000

            elif calorie_age <= 60:
                minimum = 1600
                maximum = 2800

            else:
                minimum = 1600
                maximum = 2800

            st.write(
                "Educational reference range:",
                minimum,
                "-",
                maximum,
                "kcal"
            )

            if total_calories < minimum:
                calorie_category = "Below reference"

            elif total_calories <= maximum:
                calorie_category = "Within reference"

            else:
                calorie_category = "Above reference"

            st.write("Your category is:", calorie_category)

            categories = [
                "Below reference",
                "Within reference",
                "Above reference"
            ]

            values = [20, 60, 20]

            explode = [
                0.1 if item == calorie_category else 0
                for item in categories
            ]

            fig, ax = plt.subplots()

            ax.pie(
                values,
                labels=categories,
                explode=explode,
                autopct="%1.0f%%",
                startangle=90
            )

            ax.set_title("Daily Calorie Categories")

            st.pyplot(fig)
            plt.close(fig)

            st.info(
                "The highlighted section shows your category. "
                "Percentages are illustrative and are not actual "
                "population statistics."
            )

            st.header("General Healthy Recommendations")

            if calorie_category == "Below reference":

                st.write("- Eat regular balanced meals.")
                st.write("- Include rice, roti, dal, beans, fruits and vegetables.")
                st.write("- Include protein-rich foods such as eggs, milk and pulses.")
                st.write("- Avoid skipping meals.")
                st.write("- Maintain regular sleep habits.")

            elif calorie_category == "Within reference":

                st.write("- Continue eating balanced meals.")
                st.write("- Include fruits and vegetables daily.")
                st.write("- Include whole grains and protein-rich foods.")
                st.write("- Drink enough water.")
                st.write("- Stay physically active.")

            else:

                st.write("- Focus on balanced and varied meals.")
                st.write("- Include fruits and vegetables.")
                st.write("- Choose whole grains and protein-rich foods.")
                st.write("- Limit sugary drinks and highly processed foods.")
                st.write("- Maintain regular physical activity.")

            st.warning(
                "Important: This calculator is for educational purposes only. "
                "Calorie requirements vary depending on age, sex, growth and "
                "activity level. These reference ranges are not individual "
                "nutrition targets. Consult a qualified healthcare professional "
                "for personal nutrition advice."
            )

    st.divider()

    st.warning(
        "The calculator is for educational purposes only. "
        "The results are estimates and are not a medical diagnosis "
        "or a substitute for advice from a qualified doctor or "
        "nutrition professional."
    )

elif st.session_state.page == "Diet Calculator":

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("Diet Calculator")
    st.write("This section will be created next.")

elif st.session_state.page == "Healthy Food vs Junk Food":

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("Healthy Food vs Junk Food")
    st.write("This section will be created next.")
