import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

DATASET_DIR = "dataset"

# 1. Load dataset
X = []
y = []
labels = os.listdir(DATASET_DIR)

print("Label ditemukan:", labels)

for label in labels:
    folder = os.path.join(DATASET_DIR, label)
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        # load gambar
        img = cv2.imread(path)
        if img is None:
            continue

        img = cv2.resize(img, (128, 128))   # kecilkan biar ringan
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        img = img.flatten()  # ubah ke 1D

        X.append(img)
        y.append(label)

X = np.array(X)
y = np.array(y)

print("Jumlah data:", len(X))

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Training
print("Training model...")
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)

# 4. Evaluasi
acc = model.score(X_test, y_test)
print("Akurasi:", acc)

# 5. Simpan model
joblib.dump(model, "model.pkl")
print("Model berhasil disimpan sebagai model.pkl")
