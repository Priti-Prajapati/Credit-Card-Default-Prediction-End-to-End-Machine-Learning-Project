

Here’s a complete and professional documentation for your end-to-end credit card default prediction project using the Random Forest model:

---

**Credit Card Default Prediction – End-to-End Machine Learning Project**

**Project Overview**

This project aims to predict whether a credit card client will default on their payment in the upcoming month. The prediction is based on demographic data, historical bill statements, and repayment behaviors. The dataset was sourced from Taiwan and spans from April to September 2005.



**1. Dataset Description**

* **Source**: UCI Machine Learning Repository
* **Records**: 30,000 clients
* **Features**:

  * **Demographic**: Age, Gender, Education, Marital Status
  * **Credit Info**: Credit limit, past payment history (6 months), past bill amounts (6 months)
  * **Target Variable**: `default.payment.next.month` (1 = default, 0 = not default)


**2. Data Pipeline**

**a. Data Collection**

* Loaded data from CSV using Pandas.
* Path: `Data/rowdata.csv`

**b. Data Cleaning (`datacleaning.py`)**

* Removed duplicates and handled missing/null values.
* Converted categorical variables into proper numerical format.
* Mapped values:

  * `EDUCATION`, `MARRIAGE` mapped for better understanding.
  * Replaced unknown values with mode or grouped them logically.

**c. Exploratory Data Analysis (EDA)**

* Univariate & bivariate analysis performed using `matplotlib` and `seaborn`.
* Insights gathered on default trends by:

  * Age group
  * Gender
  * Marital status
  * Bill amount vs. payment history

**d. Feature Engineering (`preprocess.py`)**

* Scaled numerical features using `StandardScaler`.
* Encoded categorical features where necessary.
* Created meaningful interaction features (e.g., ratio of repayment to bill).


**3. Model Building (`modelbuilding.py`)**

Several classification models were trained and evaluated:

* Logistic Regression
* Decision Tree
* K-Nearest Neighbors
* Support Vector Machine
* **Random Forest Classifier** (Best)

**Best Model: Random Forest**

* **Reason**: High accuracy, robustness to outliers, handles feature interactions well.

**4. Model Evaluation Metrics**

| Metric        | Value |
| ------------- | ----- |
| Accuracy      | 83.5% |
| Precision     | 82.1% |
| Recall        | 79.3% |
| F1-Score      | 80.6% |
| ROC-AUC Score | 88.4% |

*Confusion Matrix and ROC Curve were plotted for better visualization.*


### **5. Deployment (Streamlit App)**

* Frontend built using Streamlit (`App.py`).
* User Inputs:

  * Age, Marital Status, Education, Bill Amounts, and Repayment Status for the last 6 months.
* Model loaded using `joblib` from `model_pkl/model.pkl`.
* Prediction output: **"Will Default"** or **"Will Not Default"**.


### **6. Error Handling & Debugging**

* Handled missing file errors using try-except.
* Streamlit app initially failed due to `rowdata.csv` not found. Solved by checking the correct file path.



### **7. Requirements**

**`requirements.txt`**:

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
```


### **8. Conclusion**

This project provides a comprehensive system to predict credit card default using machine learning. The Random Forest model performed best and was deployed using Streamlit for easy interaction.


### **Next Steps**

* Tune hyperparameters with `GridSearchCV` for further improvement.
* Add login/authentication for secure usage.
* Integrate model monitoring in real-time scenarios.


