# DDoS Attack Detection System

## Overview

This project demonstrates a simple **Machine Learning–based DDoS attack detection system**.
The system trains a model on network traffic data and allows a user to analyze traffic samples to determine whether they are **benign** or **malicious**.

The goal of this project is to provide a **beginner-friendly, command-line interface** that allows even non-technical users to run a basic traffic analysis without needing deep knowledge of machine learning.

The model used is a **Random Forest classifier** trained on labeled network traffic data.

---

# Project Structure

```
cyber_ml_project
│
├── data/
│   └── traffic.csv      # Dataset (NOT included in the repository)
│
├── src/
│   └── ddos_interface.py
│
└── README.md
```

⚠️ **Note:**
The dataset file `traffic.csv` is not included in the repository because of file size limitations and dataset licensing restrictions.

---

# Dataset Instructions

This project requires a network traffic dataset to train the machine learning model.

You can use datasets such as:

* **CICIDS2017 Dataset**
* **CIC-DDoS2019 Dataset**
* Any labeled network traffic dataset containing benign and attack flows.

Example source:

CICIDS2017 dataset:
https://www.unb.ca/cic/datasets/ids-2017.html

---

# Preparing the Dataset

After downloading a dataset:

1. Extract the CSV file containing the network traffic features.
2. Rename the file to:

```
traffic.csv
```

3. Place the file inside the `data` folder:

```
cyber_ml_project/data/traffic.csv
```

Your project directory should look like this:

```
cyber_ml_project
│
├── data
│   └── traffic.csv
│
├── src
│   └── ddos_interface.py
```

---

# Installation

Make sure Python 3.9+ is installed.

Install the required libraries:

```
pip install pandas numpy scikit-learn
```

---

# Running the Program

Run the program from the project root directory:

```
python src/ddos_interface.py
```

You will see the following interface:

```
========================================
 DDoS ATTACK DETECTION SYSTEM
========================================
1. Analyze sample traffic
2. Show model accuracy
3. Exit
```

---

# Program Features

### 1. Analyze Sample Traffic

The system randomly selects a traffic sample from the dataset and predicts whether it represents:

* **Benign traffic**
* **Potential DDoS attack**

### 2. Show Model Accuracy

Displays the trained model's accuracy on the test dataset.

### 3. Exit

Closes the program.

---

# Machine Learning Model

The system uses a **Random Forest Classifier**, which is well-suited for network intrusion detection due to its ability to handle high-dimensional datasets and nonlinear relationships.

Model workflow:

1. Load network traffic dataset
2. Clean invalid values
3. Convert labels to binary
4. Split data into training and test sets
5. Train Random Forest model
6. Evaluate accuracy
7. Provide interactive interface for predictions

---

# Important Notes

* This project is intended for **educational and demonstration purposes**.
* The model is trained on a **sample dataset**, and accuracy will depend heavily on the dataset quality.
* Real-world DDoS detection systems require significantly more complex pipelines and real-time traffic analysis.

---

# Future Improvements

Possible enhancements include:

* Real-time packet capture
* Web-based dashboard
* Feature importance visualization
* Support for multiple datasets
* Model persistence and loading

---

# Author

Created as a demonstration project for experimenting with **machine learning–based cybersecurity systems**.
