import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. 데이터 생성
np.random.seed(42)
X = np.random.randint(50, 100, size=(200, 2))
y_raw = np.random.randint(100, 200, size=200)
y = (y_raw >= 140).astype(int)

# 2. 데이터 분할 (오타 수정: random_state)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2
)

# 3. 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. 예측 및 평가
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"정확도(Accuracy): {accuracy:.4f}")
print("혼동 행렬(Confusion Matrix):\n", cm)