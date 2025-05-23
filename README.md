# 💻 Laptop Price Predictor

## 🔍 Objective
Build a machine learning model that can accurately predict the price of a laptop based on its specifications.


## 📁 Dataset Description

- **File Name**: `laptop_data.csv`
- **Total Records**: ~1303 rows 
- **Columns**:  
  - `Company`  
  - `TypeName`  
  - `Ram`  
  - `Weight`  
  - `Touchscreen`  
  - `IPS`  
  - `PPI`  
  - `CPU`  
  - `HDD`  
  - `SSD`  
  - `GPU`  
  - `OperatingSystem`  
  - `Price` (Target)

## 📌 Source
The dataset was collected from publicly available online laptop listings.

---

## 🧹 Data Cleaning & Preprocessing

- Removed null values and duplicate rows
- Extracted features from `CPU`, `GPU`, `Memory` columns
- Converted categorical variables using label encoding and one-hot encoding
- Created new features: `Touchscreen`, `IPS`, `PPI` (pixels per inch)

---

## 📊 Exploratory Data Analysis (EDA)

- Price increases with RAM and SSD size
- Laptops with touchscreen and IPS display tend to be costlier
- Apple and MSI are among the most expensive brands
- The correlation matrix shows that `SSD`, `RAM`, and `PPI` are strong predictors of price

*(Graphs were used for visual validation — scatter plots, heatmaps, bar charts.)*

---

## 🤖 Model Development & Evaluation

### 🧪 Models Tried:
- Linear Regression
- Random Forest Regressor

### 📈 Evaluation Metrics:
- R² Score
- Mean Absolute Error (MAE)

### ✅ Best Model:
- **Random Forest Regressor**
  - R² Score: ~0.877
  - MAE: 0.1658502125022846

---

## 🖥 Deployment

- **Framework Used**: Streamlit
- UI allows user to select:
  - Brand
  - RAM size
  - Weight
  - CPU brand
  - Touchscreen, IPS, HDD/SSD
- Model predicts the laptop price on-the-fly
- UI built-in `app.py` and run using:
  ```bash
  streamlit run app.py

## 🖥 Conclusion

- Built a robust model for predicting laptop prices
- Achieved good accuracy and interpretability
- Deployed using Streamlit for real-time use
