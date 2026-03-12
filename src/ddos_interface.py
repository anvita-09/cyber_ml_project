import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =========================
# Load & prepare data
# =========================
df = pd.read_csv("data/traffic.csv")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
df.columns = df.columns.str.strip()

df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# Train model
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# =========================
# Menu Interface
# =========================
while True:
    print("\n" + "="*40)
    print(" DDoS ATTACK DETECTION SYSTEM ")
    print("="*40)
    print("1. Analyze sample traffic")
    print("2. Show model accuracy")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        print("\nAnalyzing sample traffic...\n")

        sample = X_test.sample(1)
        prediction = model.predict(sample)[0]

        if prediction == 1:
            print("⚠️ WARNING: DDoS ATTACK DETECTED")
        else:
            print("✅ Traffic is BENIGN (Safe)")

    elif choice == "2":
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\n📊 Model Accuracy: {acc:.2f}")

    elif choice == "3":
        print("\nExiting system. Stay safe! 👋")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")