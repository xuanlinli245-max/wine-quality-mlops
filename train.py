import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 读取数据
df = pd.read_csv(r'C:\Users\user\Desktop\wine_quality_mlops\winequality-red.csv')
print(f"数据加载成功，共 {len(df)} 行")

# 准备数据
X = df.drop('quality', axis=1)
y = df['quality']

print("x的样子",X)
print("y的样子",y)
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 评估
y_pred = model.predict(X_test)
print(f"模型准确率: {accuracy_score(y_test, y_pred):.4f}")

# 保存模型
joblib.dump(model, 'model.pkl')
print("模型已保存为 model.pkl")