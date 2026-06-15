# KNN 選股完整流程：讀取 Excel、切分 1997/1998、訓練與預測

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# === Step 1: 讀取資料 ===
file_path = 'top200.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# === 建立明確的 'Year' 欄位 ===
df['Year'] = df['年月'].astype(str).str[:4].astype(int)

# 過濾訓練與測試資料（1997 年為訓練，1998 年為測試）
df_train = df[df['Year'] == 1997].copy()
df_test = df[df['Year'] == 1998].copy()

# === Step 2: 定義特徵與標籤 ===
features = [
    '市值(百萬元)',
    '收盤價(元)_年',
    'Unknown masked parameter',
    '股價淨值比',
    '股價營收比',
    'M淨值報酬率─稅後',
    '資產報酬率ROA',
    '營業利益率OPM',
    '利潤邊際NPM',
    '負債/淨值比',
    'M流動比率',
    'M速動比率',
    'M存貨週轉率 (次)',
    'M應收帳款週轉次',
    'M營業利益成長率',
    'M稅後淨利成長率'
]

label_col = 'ReturnMean_year_Label'
return_col = 'Return'

# === Step 3: 特徵標準化 ===
scaler = StandardScaler()
X_train = scaler.fit_transform(df_train[features])
X_test = scaler.transform(df_test[features])

y_train = df_train[label_col]

# === Step 4: 建立與訓練 KNN 模型 ===
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# === Step 5: 預測測試資料 ===
preds = knn.predict(X_test)
df_test['Pred_Label'] = preds

# === Step 6: 選出預測為 1 的股票，計算實際報酬率 ===
selected = df_test[df_test['Pred_Label'] == 1]
avg_return = selected[return_col].mean()

print(f"K={k}, 使用特徵數={len(features)}，預測為 1 的股票數量={len(selected)}")
print(f"這些股票實際平均報酬率為：{avg_return:.2f}%")
