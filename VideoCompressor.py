import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import threading
import os
import sys
from pathlib import Path

class VideoCompressor:
    def __init__(self, root):
        self.root = root
        self.root.title("影片壓縮工具 (獨立版)")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 變數
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.quality = tk.StringVar(value="medium")
        self.resolution = tk.StringVar(value="original")
        self.is_compressing = False
        
        # 設定 FFmpeg 路徑
        self.ffmpeg_path = self.get_ffmpeg_path()
        
        self.create_widgets()
        self.check_ffmpeg()
    
    def get_ffmpeg_path(self):
        """自動尋找 FFmpeg 執行檔"""
        possible_paths = [
            # 檢查是否在程式同目錄的 ffmpeg 資料夾
            Path(sys.executable).parent / "ffmpeg" / "ffmpeg.exe",  # 打包後
            Path(__file__).parent / "ffmpeg" / "ffmpeg.exe",        # 開發時
            # 檢查系統 PATH
            "ffmpeg"  # 系統安裝的版本
        ]
        
        for path in possible_paths:
            if isinstance(path, Path):
                if path.exists():
                    return str(path)
            else:
                # 檢查系統 PATH 中的 ffmpeg
                try:
                    subprocess.run([path, '-version'], capture_output=True, check=True)
                    return path
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
        
        return None
    
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 輸入檔案選擇
        ttk.Label(main_frame, text="選擇輸入影片:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.input_file, width=50).grid(row=1, column=0, pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="瀏覽", command=self.select_input_file).grid(row=1, column=1, pady=5)
        
        # 輸出檔案選擇
        ttk.Label(main_frame, text="選擇輸出位置:").grid(row=2, column=0, sticky=tk.W, pady=(20, 5))
        ttk.Entry(main_frame, textvariable=self.output_file, width=50).grid(row=3, column=0, pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="瀏覽", command=self.select_output_file).grid(row=3, column=1, pady=5)
        
        # 壓縮品質設定
        quality_frame = ttk.LabelFrame(main_frame, text="壓縮設定", padding="10")
        quality_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 10))
        
        ttk.Label(quality_frame, text="壓縮品質:").grid(row=0, column=0, sticky=tk.W)
        quality_combo = ttk.Combobox(quality_frame, textvariable=self.quality, state="readonly", width=15)
        quality_combo['values'] = ('high', 'medium', 'low', 'ultra_low')
        quality_combo.grid(row=0, column=1, padx=(10, 20))
        
        ttk.Label(quality_frame, text="解析度:").grid(row=0, column=2, sticky=tk.W)
        resolution_combo = ttk.Combobox(quality_frame, textvariable=self.resolution, state="readonly", width=15)
        resolution_combo['values'] = ('original', '1080p', '720p', '480p')
        resolution_combo.grid(row=0, column=3, padx=(10, 0))
        
        # 進度條
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 10))
        
        # 狀態標籤
        self.status_label = ttk.Label(main_frame, text="準備就緒")
        self.status_label.grid(row=6, column=0, columnspan=2, pady=5)
        
        # 壓縮按鈕
        self.compress_button = ttk.Button(main_frame, text="開始壓縮", command=self.start_compression)
        self.compress_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))
        
        # 輸出訊息區域
        output_frame = ttk.LabelFrame(main_frame, text="輸出訊息", padding="5")
        output_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))
        
        self.output_text = tk.Text(output_frame, height=8, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 設定權重讓界面可以調整大小
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(8, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
    
    def check_ffmpeg(self):
        """檢查 FFmpeg 是否可用"""
        if self.ffmpeg_path:
            try:
                subprocess.run([self.ffmpeg_path, '-version'], capture_output=True, check=True)
                self.log_output(f"✅ FFmpeg 已就緒: {self.ffmpeg_path}")
                return
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        
        # FFmpeg 不可用，顯示詳細說明
        error_message = """🚫 未找到 FFmpeg！

📁 解決方法：

方法 1 - 便攜版設定（推薦）：
1. 在程式所在資料夾建立 'ffmpeg' 資料夾
2. 下載 FFmpeg：https://github.com/BtbN/FFmpeg-Builds/releases
3. 將 ffmpeg.exe 放入 'ffmpeg' 資料夾
4. 重新啟動程式

方法 2 - 系統安裝：
1. 下載 FFmpeg：https://ffmpeg.org/download.html
2. 解壓並將 bin 資料夾加入系統 PATH
3. 重新啟動程式

📂 目前程式路徑：""" + str(Path(sys.executable).parent if hasattr(sys, 'frozen') else Path(__file__).parent)
        
        messagebox.showerror("FFmpeg 未找到", error_message)
        self.compress_button.configure(state='disabled')
        self.log_output("❌ FFmpeg 未找到，請按照說明安裝")
    
    def select_input_file(self):
        filename = filedialog.askopenfilename(
            title="選擇輸入影片",
            filetypes=[
                ("影片檔案", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm"),
                ("所有檔案", "*.*")
            ]
        )
        if filename:
            self.input_file.set(filename)
            # 自動設定輸出檔名
            base_name = os.path.splitext(filename)[0]
            self.output_file.set(f"{base_name}_compressed.mp4")
    
    def select_output_file(self):
        filename = filedialog.asksaveasfilename(
            title="選擇輸出位置",
            defaultextension=".mp4",
            filetypes=[
                ("MP4 檔案", "*.mp4"),
                ("所有檔案", "*.*")
            ]
        )
        if filename:
            self.output_file.set(filename)
    
    def get_ffmpeg_params(self):
        """根據設定獲取 ffmpeg 參數"""
        params = [self.ffmpeg_path, '-i', self.input_file.get(), '-y']  # -y 覆蓋輸出檔案
        
        # 品質設定 (CRF值越小品質越好)
        quality_map = {
            'high': '18',
            'medium': '23',
            'low': '28',
            'ultra_low': '35'
        }
        params.extend(['-crf', quality_map[self.quality.get()]])
        
        # 解析度設定
        if self.resolution.get() != 'original':
            resolution_map = {
                '1080p': '1920:1080',
                '720p': '1280:720',
                '480p': '854:480'
            }
            params.extend(['-vf', f'scale={resolution_map[self.resolution.get()]}'])
        
        # 編碼設定
        params.extend([
            '-c:v', 'libx264',      # 使用 H.264 編碼
            '-preset', 'medium',     # 編碼速度與品質的平衡
            '-c:a', 'aac',          # 音訊編碼
            '-b:a', '128k',         # 音訊位元率
        ])
        
        params.append(self.output_file.get())
        return params
    
    def log_output(self, message):
        """在輸出區域添加訊息"""
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.root.update()
    
    def start_compression(self):
        if not self.input_file.get() or not self.output_file.get():
            messagebox.showerror("錯誤", "請選擇輸入和輸出檔案")
            return
        
        if not os.path.exists(self.input_file.get()):
            messagebox.showerror("錯誤", "輸入檔案不存在")
            return
        
        if not self.ffmpeg_path:
            messagebox.showerror("錯誤", "FFmpeg 未找到，請先安裝 FFmpeg")
            return
        
        # 在新執行緒中執行壓縮
        thread = threading.Thread(target=self.compress_video)
        thread.daemon = True
        thread.start()
    
    def compress_video(self):
        self.is_compressing = True
        self.compress_button.configure(state='disabled')
        self.progress.start()
        self.status_label.configure(text="壓縮中...")
        
        try:
            params = self.get_ffmpeg_params()
            self.log_output(f"🎬 開始壓縮: {os.path.basename(self.input_file.get())}")
            self.log_output(f"📁 輸出至: {os.path.basename(self.output_file.get())}")
            self.log_output(f"⚙️ 品質: {self.quality.get()}, 解析度: {self.resolution.get()}")
            self.log_output(f"🔧 使用 FFmpeg: {self.ffmpeg_path}")
            self.log_output("-" * 50)
            
            # 執行 ffmpeg
            process = subprocess.Popen(
                params,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            # 讀取輸出
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                self.log_output("✅ 壓縮完成！")
                self.status_label.configure(text="壓縮完成")
                
                # 顯示檔案大小比較
                if os.path.exists(self.output_file.get()):
                    original_size = os.path.getsize(self.input_file.get())
                    compressed_size = os.path.getsize(self.output_file.get())
                    reduction = (1 - compressed_size / original_size) * 100
                    
                    self.log_output(f"📊 原始檔案: {original_size / 1024 / 1024:.1f} MB")
                    self.log_output(f"📊 壓縮後: {compressed_size / 1024 / 1024:.1f} MB")
                    self.log_output(f"📊 減少: {reduction:.1f}%")
                
                messagebox.showinfo("完成", "影片壓縮完成！")
            else:
                self.log_output("❌ 壓縮失敗")
                self.log_output(stderr)
                self.status_label.configure(text="壓縮失敗")
                messagebox.showerror("錯誤", f"壓縮失敗:\n{stderr}")
                
        except Exception as e:
            self.log_output(f"❌ 錯誤: {str(e)}")
            self.status_label.configure(text="發生錯誤")
            messagebox.showerror("錯誤", f"發生錯誤: {str(e)}")
        
        finally:
            self.is_compressing = False
            self.progress.stop()
            self.compress_button.configure(state='normal')

def main():
    root = tk.Tk()
    app = VideoCompressor(root)
    root.mainloop()

if __name__ == "__main__":
    main()