import streamlit as st
import pandas as pd

def authenticate():
    st.title("Secure Login")
    password = st.text_input("Enter the password:", type="password")
    if password == st.secrets["general"]["password"]:
        st.success("Access Granted!")
        return True
    else:
        if password:  # Show error only if user tries to login
            st.error("Access Denied!")
        return False

# Main App Logic
if authenticate():  # Block access if authentication fails
    # App content goes here
    st.title("Patient Data Tally Checker")
    st.write("Welcome to the secure app!")
    # Rest of your app code
else:
    st.stop()  # Prevent unauthorized users from accessing the app


# Streamlit app
def main():
    st.title("Patient Data Tally Checker with Babies Filter")
    st.write("Upload an Excel file with the specified format to validate the tally for each row and perform additional calculations.")

    # File uploader
    uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type="xlsx")
    if uploaded_file:
        try:
            # Read Excel file
            df = pd.read_excel(uploaded_file)

            # Display the uploaded table
            st.write("Uploaded Table:")
            st.dataframe(df)

            # Validate the columns
            expected_columns = [
                "Ward Name",
                "Bed Strength",
                "Total Patients Beginning of the Day",
                "Total Patients End of Day",
                "New Admission",
                "Discharges",
                "Deaths",
                "Transfer In",
                "Transfer Out"
            ]

            if all(col in df.columns for col in expected_columns):
                # Perform tally check
                incorrect_rows = []
                for index, row in df.iterrows():
                    calculated_end_day = (
                        row["Total Patients Beginning of the Day"]
                        + row["New Admission"]
                        + row["Transfer In"]
                        - row["Discharges"]
                        - row["Deaths"]
                        - row["Transfer Out"]
                    )

                    if calculated_end_day != row["Total Patients End of Day"]:
                        incorrect_rows.append(index)

                # Output result of tally check
                if not incorrect_rows:
                    st.success("Tally is correct for all rows!")
                    st.info("All rows have consistent data.")
                else:
                    st.error(
                        f"Tally mismatch found in the following row(s): {', '.join(map(str, incorrect_rows))}"
                    )

                # Additional feature: Calculate based on "Babies"
                st.header("Additional Calculations")
                total_patients_end = df["Total Patients End of Day"].sum()
                babies_rows = df[df["Ward Name"].str.contains("Babies", case=False, na=False)]
                babies_patients_sum = babies_rows["Total Patients End of Day"].sum()
                result = total_patients_end - babies_patients_sum

                # Display each calculation as a banner with bold numerical values
                st.info(f"Sum of all 'Total Patients End of Day': **{total_patients_end}**")
                st.info(f"Sum of 'Total Patients End of Day' for rows with 'Babies': **{babies_patients_sum}**")
                st.info(f"Result (excluding 'Babies' patients): **{result}**")

            else:
                st.error("Uploaded file does not have the required columns.")
        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
