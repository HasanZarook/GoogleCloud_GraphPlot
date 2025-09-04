# 📊 Medicare Renal Failure Analysis with BigQuery & ReportLab

This project demonstrates how to use **Google BigQuery** with Python to query large-scale public healthcare data (Medicare charges for renal failure from 2011–2014) and generate a **PDF report** containing a bar chart visualization.

---

## 📂 Project Structure

```
.
├── renal_failure_analysis.py    # Main Python script (BigQuery + PDF generation)
├── taskproj-398609-2926bb2e71c9.json  # GCP service account key (NOT to be shared publicly)
├── requirements.txt             # Required Python packages
└── README.md                    # Project documentation
```

---

## ⚙️ Features

* Connects to **Google BigQuery** using a service account.
* Runs queries on **inpatient** and **outpatient** datasets:

  * Total inpatients (renal failure cases)
  * Total outpatients (renal failure cases)
  * Average total payments for inpatients
  * Average total payments for outpatients
* Extracts yearly payment data (2011–2014).
* Uses **ReportLab** to generate a **PDF report** with a bar chart visualization.

---

## 📦 Requirements

Install dependencies before running:

```bash
pip install google-cloud-bigquery google-auth reportlab
```

---

## ▶️ How to Run

1. Set up your **Google Cloud Service Account**:

   * Create a service account in Google Cloud Console.
   * Download the JSON key and place it in your project folder.
   * Update this line in the script with your key name:

     ```python
     credentials = service_account.Credentials.from_service_account_file("your-key.json")
     ```

2. Run the script:

   ```bash
   python renal_failure_analysis.py
   ```

3. Output:

   * A PDF file named **`DBLAB7_Graphs_2021_CE_58.pdf`** will be generated with a **bar chart of renal failure payments (2011–2014)**.

---

## 📊 Example Visualization

The generated PDF contains a bar chart like this:

* X-axis: Years (2011–2014)
* Y-axis: Total Average Payments
* Bars: Payments related to **renal failure inpatient charges**

---

## 🔒 Security Note

⚠️ **Never upload your service account JSON key to GitHub**.
To keep your project secure:

* Add `*.json` to your `.gitignore`.
* Use **environment variables** to store sensitive keys instead of hardcoding.

---

## 👤 Author

**A.G. Hasan Zarook**
📍 University of Engineering and Technology, Lahore

---
