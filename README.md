# GMC-Dietetics-Department

---

# **Patient Data Tally Checker**

## **Overview**
This Streamlit-based application helps healthcare facilities to verify patient data for consistency in tally calculations. The app allows users to upload an Excel file containing patient data, check if the tally is correct based on the provided formula, and also perform additional calculations to ensure data accuracy. A built-in password authentication system ensures the security of the app, making it suitable for handling sensitive medical data.

---

## **Features**
- **File Upload:** Users can upload an Excel file (.xlsx) containing columns like "Total Patients Beginning of the Day," "New Admission," "Transfer In," "Discharges," "Deaths," "Transfer Out," and "Total Patients End of Day."
- **Tally Check:** Automatically checks if the sum of "Total Patients Beginning of the Day" + "New Admission" + "Transfer In" - "Discharges" - "Deaths" - "Transfer Out" equals "Total Patients End of Day."
- **Additional Calculations:** Computes the sum of all values in the "Total Patients End of Day" column and subtracts values associated with "Babies" ward names.
- **Authentication:** Password protection to secure the app and restrict access to authorized users only.
- **User-Friendly Interface:** A clean and simple interface where users can upload data and see real-time results with clear messages for tally correctness and additional calculations.

---

## **Requirements**

The application is built using the following libraries:

- **streamlit**: Framework for building the app.
- **pandas**: For handling and processing Excel files.
- **openpyxl**: Required to read `.xlsx` files.

To install the necessary dependencies, create a virtual environment and run:

```bash
pip install -r requirements.txt
```

---

## **Setup & Deployment**

### **1. Clone the repository**

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/patient-tally-checker.git
cd patient-tally-checker
```

### **2. Set up the environment**

- Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

- Install the required packages:

```bash
pip install -r requirements.txt
```

### **3. Authentication Configuration**

To enable authentication, you need to set up a `secrets.toml` file with your password. In your project root directory, create a file named `secrets.toml` with the following content:

```toml
[general]
password = "your_secure_password"
```

Replace `"your_secure_password"` with a password of your choice. This password will be required to access the app.

### **4. Run the app locally**

Once the setup is complete, run the following command to start the app:

```bash
streamlit run app.py
```

The app will be accessible at `http://localhost:8501`.

---

## **Deployment on Streamlit Cloud**

1. **Create a GitHub Repository**: Upload your project to GitHub if it's not already there.
2. **Deploy to Streamlit Cloud**: Go to [Streamlit Cloud](https://streamlit.io/cloud), log in with your GitHub account, and deploy the app from your repository.
3. **Add Secrets**: In Streamlit Cloud, navigate to the **Secrets** section in your app's settings and add the secrets as shown earlier (`[general] password = "your_secure_password"`).

---

## **How It Works**

The app performs the following tasks:

1. **Tally Verification:**
   For each row in the uploaded Excel file, the app verifies if:
   ``` 
   Total Patients Beginning of the Day + New Admission + Transfer In - Discharges - Deaths - Transfer Out = Total Patients End of Day
   ```

   If the calculation is correct, a success message is shown. If incorrect, the row number(s) with mismatched totals are displayed.

2. **Additional Calculations:**
   - The sum of the "Total Patients End of Day" column is calculated.
   - If the ward name contains "Babies," those rows are excluded from the sum, and the result is displayed.

---

## **File Format**

Ensure that the uploaded Excel file follows this format:

| Ward Name | Bed Strength | Total Patients Beginning of the Day | Total Patients End of Day | New Admission | Discharges | Deaths | Transfer In | Transfer Out |
|-----------|--------------|--------------------------------------|---------------------------|---------------|------------|--------|-------------|--------------|
| Ward 1    | 100          | 80                                   | 90                        | 10            | 5          | 2      | 3           | 1            |
| Babies    | 50           | 30                                   | 35                        | 5             | 2          | 1      | 1           | 0            |
| Ward 2    | 120          | 100                                  | 120                       | 15            | 10         | 4      | 8           | 5            |

Make sure that the following columns exist:
- `Ward Name`
- `Bed Strength`
- `Total Patients Beginning of the Day`
- `Total Patients End of Day`
- `New Admission`
- `Discharges`
- `Deaths`
- `Transfer In`
- `Transfer Out`

---

## **Contributing**

Contributions are welcome! Feel free to fork the repository and submit pull requests with any improvements or bug fixes.

---

## **License**

This project is open-source and available under the [MIT License](LICENSE).

---
