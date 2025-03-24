# Импортируем необходимые библиотеки
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Загрузите ваш датасет (замените на свой путь)
df = pd.read_csv('education_career_success.csv')

# Обработка категориальных переменных с использованием one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Разделяем на признаки (X) и целевой признак (y)
X = df.drop(columns=['Entrepreneurship_Yes'])  # Замените на нужный целевой признак
y = df['Entrepreneurship_Yes']  # Целевой признак

# Разделяем данные на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Применяем SMOTE для балансировки классов
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Масштабируем данные (это важный шаг для XGBoost)
scaler = StandardScaler()
X_train_res_scaled = scaler.fit_transform(X_train_res)
X_test_scaled = scaler.transform(X_test)

# Создаем модель XGBoost
xgb_model = xgb.XGBClassifier(scale_pos_weight=10, random_state=42, use_label_encoder=False)

# Обучаем модель
xgb_model.fit(X_train_res_scaled, y_train_res)

# Прогнозируем на тестовой выборке
y_pred = xgb_model.predict(X_test_scaled)

# Оценка модели
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, xgb_model.predict_proba(X_test_scaled)[:, 1])

# Вывод результатов
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"ROC AUC: {roc_auc}")
input()