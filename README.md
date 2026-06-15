# 📈 金融科技量化交易專題 (FinTech Quantitative Trading & Investment Models)

本專案為**金融科技（AIFT）課程的量化投資專題成果**。專案核心圍繞於建立系統化的投資策略模型，並完全導入**時序驗證（Temporal Validation, TV）**機制進行策略回測（Back-testing），以確保模型在面對金融市場動態特性時的有效性與嚴謹度。

專案主要包含兩大核心模組：**多策略個股回測比較** 與 **統計套利配對交易（Pairs-Trading）**。

---

## 🛠️ 核心技術與量化架構
- **核心語言**: Python
- **資料科學與量化庫**: `pandas`, `numpy`, `scikit-learn`, `yfinance` (或相關財經 API)。
- **驗證框架**: 嚴格採用 **時序驗證（Temporal Validation, TV1~TVn）**，以 In-sample 歷史數據進行模型參數優化，並以 Out-of-sample 數據進行策略績效評估，避免傳統隨機交叉驗證（Cross-Validation）破壞時間序列前後因果關係的問題。

---

## 📂 專案核心模組說明 (Project Modules)

### 📊 模組一：個股投資策略與回測評估 (Investment Strategies & Backtesting)
- **實作邏輯**: 自行精選 5 檔核心股票，設定初始資金 $10,000 / 每檔，設計並實作自訂的技術指標量化策略（如 **移動平均線策略 Moving Average Strategies** ）。
- **績效基準比較**: 策略最終績效皆轉換為**年化報酬率（Annual Rate of Return）**，並與兩大經典被動投資基準進行嚴格對比：
  - **單筆投入法 (Lump-sum Method)**
  - **定期定額法 (DCA - Dollar-Cost Averaging)**
- **核心亮點**: 展現策略在不同市況下是否具備超額報酬（Alpha 獲利能力）。

### ⚖️ 模組二：統計套利配對交易策略 (Pairs-Trading Strategy)
- **實作邏輯**: 利用模組一選出的 5 檔股票，進行資產間的共整合（Cointegration）或相關性分析，尋找具備平穩性（Stationarity）的資產價差組合，實作經典的**配對交易（Pairs-Trading）**統計套利策略。
- **回測優化**: 策略開平倉閾值與價差均線完全基於時序驗證（Temporal Validation）框架進行 rolling 訓練，系統化考察模型在動態金融環境中的穩健度。

