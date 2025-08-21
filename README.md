<<<<<<< HEAD
# 便攜版影片壓縮工具使用說明

## 📁 資料夾結構
```
便攜版影片壓縮工具/
├── 影片壓縮工具.exe      # 主程式
├── ffmpeg/              # FFmpeg 執行檔資料夾
│   ├── ffmpeg.exe       # 請下載並放入
│   ├── ffprobe.exe      # 請下載並放入
│   └── ffplay.exe       # 請下載並放入
├── README.md            # 本說明檔案
└── 下載FFmpeg說明.txt    # FFmpeg 下載指南
```

## 🔧 首次使用設定

### 步驟 1：下載 FFmpeg
1. 前往：https://github.com/BtbN/FFmpeg-Builds/releases
2. 下載最新的 `ffmpeg-master-latest-win64-gpl.zip`
3. 解壓後，將 `bin` 資料夾內的以下檔案複製到 `ffmpeg` 資料夾：
   - ffmpeg.exe
   - ffprobe.exe
   - ffplay.exe

### 步驟 2：執行程式
- 雙擊 `影片壓縮工具.exe` 即可開始使用

## ✨ 使用說明
1. 選擇要壓縮的影片檔案
2. 設定輸出位置和壓縮參數
3. 點擊「開始壓縮」
4. 等待處理完成

## 🎯 支援格式
- 輸入：MP4, AVI, MOV, MKV, WMV, FLV, WebM
- 輸出：MP4 (H.264)

## 📞 技術支援
如有問題，請確認：
1. ffmpeg 資料夾內有必要的執行檔
2. 輸入的影片檔案格式正確
3. 有足夠的磁碟空間儲存輸出檔案
