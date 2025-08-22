```markdown
# 🎬 VideoCompressor

**VideoCompressor** 是一款基於 **FFmpeg** 的輕量級影片壓縮工具，提供 **簡單直覺的圖形化介面 (GUI)**，讓使用者快速壓縮影片、減少空間佔用，同時維持良好畫質與相容性。  
適合需要快速分享影片、釋放儲存空間，或壓縮影片上傳社群平台的使用者。

---

## ✨ 功能特色
- **多格式支援**：輸入 MP4 / AVI / MOV / MKV / WMV / FLV / WebM  
- **輸出格式**：MP4 (H.264 / AAC)  
- **壓縮品質選項（CRF 對應）**  
  - `high` → CRF 18（畫質佳、檔案較大）  
  - `medium` → CRF 23（預設，品質與大小平衡）  
  - `low` → CRF 28（壓縮比高）  
  - `ultra_low` → CRF 35（檔案最小）  
- **解析度調整**：`原始` / `1080p` / `720p` / `480p`  
- **直覺化 GUI**：檔案選擇、進度條、狀態訊息  
- **結果回饋**：顯示原始/壓縮後大小與節省比例 (%)  
- **自動尋找 FFmpeg**：  
  - `專案目錄/ffmpeg/ffmpeg.exe`  
  - 腳本目錄中的 `ffmpeg/ffmpeg.exe`  
  - 系統 PATH

---

## 📂 專案結構
```

VideoCompressor/
├── VideoCompressor.py     # 主程式 (Python)
├── README.md              # 本說明文件
└── 下載FFmpeg說明.txt      # FFmpeg 下載/擺放指南

````

---

## 🖥️ 系統需求與相容性
- **作業系統**：Windows 10/11（可於其他平台以 Python 執行）  
- **Python**：3.8 以上  
- **額外相依**：FFmpeg（需自行下載，專案不內含）

> 本工具使用 Python 標準函式庫（`tkinter`, `subprocess`, `threading`, `pathlib` 等），**無需額外 pip 套件**。

---

## 🚀 安裝與執行

### 1) 取得 FFmpeg
- 依 `下載FFmpeg說明.txt` 指南下載對應版本（建議 Windows 下載 BtbN Builds），將以下檔案放入專案的 `ffmpeg/` 資料夾或加入系統 PATH：  
  - `ffmpeg.exe`（必要）  
  - `ffprobe.exe`（必要）  
  - `ffplay.exe`（可選）

### 2) 執行程式
```bash
python VideoCompressor.py
````

或使用你打包出的 `影片壓縮工具.exe`（Windows，若有提供）。

---

## 🧭 使用教學（GUI）

1. **選擇輸入影片**：挑選欲壓縮的檔案
2. **設定輸出位置**：預設自動產生 `*_compressed.mp4`
3. **選擇壓縮品質**：`high` / `medium` / `low` / `ultra_low`
4. **選擇解析度**：保留 `原始` 或轉為 `1080p / 720p / 480p`
5. **開始壓縮**：按下按鈕後，進度條與訊息區會即時更新
6. **查看結果**：完成後會顯示原始/壓縮後大小與節省比例

---

## 💡 建議（Best Practices）

* **起手式**：先用 `medium` + `原始解析度` 測試，檢查品質是否可接受，再視需求調整至 `high`（畫質佳）或 `low/ultra_low`（更小）。
* **高動態/細節影片**（運動、特效、噪點多）：建議 `high` 或 `medium`，避免過度壓縮造成方塊或塗抹感。
* **要上傳社群平台**：多半接受 H.264/AAC MP4；若平台再轉檔，建議別把檔案壓太死（`medium` 或 `high`）。
* **音訊**：預設 `AAC 128k` 已符合多數需求；若是音樂或人聲要求較高，可後續擴充為 192k。
* **相容性**：H.264 + AAC 在各平台/裝置相容性最佳；若未來有特別需求（如 HEVC、VP9、AV1），可在 Roadmap 擴充。

---

## 📊 範例效果

| 原始大小   | 壓縮後大小  | 節省比例 |
| ------ | ------ | ---- |
| 120 MB | 42 MB  | 65%  |
| 480 MB | 150 MB | 68%  |
| 1.2 GB | 430 MB | 64%  |

> 實際數字依素材內容、畫面動態、噪點多寡與選擇的品質/解析度而異。

---

## 🛠️ 常見問題（Troubleshooting）

* **啟動時跳出「FFmpeg 未找到」**

  * 確認 `ffmpeg/` 資料夾中有 `ffmpeg.exe` / `ffprobe.exe`；或已正確加入系統 PATH。
* **壓縮失敗/沒有輸出檔**

  * 檢查輸入檔是否存在與可讀、輸出目錄是否有寫入權限、磁碟空間是否足夠。
* **壓縮後畫質不佳**

  * 調高品質（如 `low` → `medium` 或 `high`），或保留原始解析度。
* **速度太慢**

  * 目前預設 `-preset medium`；未來可加入 `NVENC/QSV` 等硬體加速（Roadmap）。

---

## ✅ 優點

* **零門檻**：圖形化介面、無需記憶命令列
* **即插即用**：只需擺放 FFmpeg 可執行檔即可使用
* **實用預設**：H.264 + AAC，高相容性
* **回饋明確**：顯示原/後大小與節省比例，便於比較

---

## ⚠️ 限制

* **輸出格式固定**：目前僅輸出 MP4（H.264/AAC）
* **未含 FFmpeg**：需自行下載擺放或設定 PATH
* **單檔處理**：尚未支援批次壓縮
* **無硬體加速**：尚未整合 NVENC、QSV、AMF

---

## 🗺️ Roadmap（可選）

* 批次壓縮與資料夾遞迴處理
* 自訂 FFmpeg 參數（進階模式）
* 一鍵硬體加速（NVENC/QSV/AMF）
* 多語系介面與日誌輸出

---

## 📜 授權

* **程式碼授權**：本專案採用 **MIT License**。
* **第三方授權**：本專案使用 **FFmpeg**（GPL/LGPL）；**不包含**其二進位檔，使用者需自行下載並遵循其授權條款。
* 若你以可執行檔形式發佈本工具且**將 FFmpeg 一併打包**，請務必同時附上 FFmpeg 的授權與原始碼取得方式，或改為提供「下載與擺放教學」以避免授權爭議。

---

## 🤝 貢獻

歡迎提交 Issue / PR 提出功能建議、錯誤回報或改進想法。

---

## 🙏 致謝

* [FFmpeg](https://ffmpeg.org/) — 強大的開放原始碼影音處理框架

```

<!-- Sources: :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} -->
```