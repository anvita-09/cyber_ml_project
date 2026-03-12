import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# 1. Load dataset
# =========================
df = pd.read_csv("C:/Users/anvit/college/experience/cyber_ml_project/data/traffic.csv.csv")  # adjust path if needed

# =========================
# 2. Clean data
# =========================
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

df.columns = df.columns.str.strip()

# Convert labels: BENIGN -> 0, ATTACK -> 1
df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

# =========================
# 3. Split features & label
# =========================
X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 4. Train Random Forest
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# =========================
# 5. Predictions & metrics
# =========================
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# =========================
# 6. Confusion Matrix (NO seaborn)
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
plt.imshow(cm)
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("DDoS Detection - Confusion Matrix")

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()

importances = model.feature_importances_

fi = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print("\nTop 10 Important Features:\n")
print(fi.head(10))


joblib.dump(model, "ddos_rf_model.pkl")
joblib.dump(X.columns.tolist(), "feature_names.pkl")

import joblib

joblib.dump(model, "ddos_rf_model.pkl")
joblib.dump(X.columns.tolist(), "feature_names.pkl")

print("✅ Model and feature names saved successfully")