# 📄 PDF 合併工具 / PDF Merge Tool

此工具用於自動遍歷指定資料夾及其子資料夾，合併所有以 `CN).pdf` 或 `EN).pdf` 結尾的中文／英文 PDF 文件，並輸出至 `handled_pdf` 資料夾中。合併後的檔案將以資料夾名稱作為檔名的一部分。

This tool automatically scans through a root folder and its subfolders, merging all PDF files ending with `CN).pdf` or `EN).pdf`. The merged files will be saved in a new folder named `handled_pdf`, with filenames based on their original subfolder names.

---

## 🛠 使用方式 / How to Use

### 1. 安裝依賴套件 / Install Dependencies

請確保你已安裝 `PyPDF2` 套件：  
Make sure you have installed `PyPDF2`:

```bash
pip install PyPDF2
```

### 2. 執行腳本 / Run the Script

將以下程式碼儲存為 `merge_pdfs.py`，並在終端機中執行：  
Save the code as `merge_pdfs.py`, then run:

```bash
python merge_pdfs.py
```

### 3. 操作流程 / Process

系統會提示你輸入要處理的根資料夾路徑（例如：`C:\User\Desktop\YourFolder`），工具將：

The script will prompt you to enter the root folder path (e.g., `C:\User\Desktop\YourFolder`), then it will:

- 🔍 搜尋所有以 `CN).pdf` 與 `EN).pdf` 結尾的檔案  
  Search all files ending with `CN).pdf` and `EN).pdf`

- 📄 分別合併成 `{資料夾名稱}_CN.pdf` 與 `{資料夾名稱}_EN.pdf`  
  Merge them into `{folder_name}_CN.pdf` and `{folder_name}_EN.pdf`

- 💾 輸出至 `handled_pdf` 資料夾中  
  Save to the `handled_pdf` folder

- 🔄 第二次掃描合併處理後的 `CN.pdf` 與 `EN.pdf` 版本（可用於多層次合併）  
  Optionally re-merge the already processed PDFs for nested folder structures

---

## 📌 注意事項 / Notes

### 檔案命名規則 / File Naming Rules
- ✅ 原始 PDF 檔案名稱需正確以 `CN).pdf` 或 `EN).pdf` 結尾  
  Original PDFs must end with `CN).pdf` or `EN).pdf`

### 資料夾結構 / Folder Structure
- 📁 若資料夾層數較多，此工具會正確地以資料夾路徑組成命名（如 `U1L3_Handout_CN.pdf`）  
  For deep folder structures, the tool uses folder paths joined with `_` to name merged files

### 合併順序 / Merge Order
- 🔤 若檔案順序有要求，請確保 PDF 檔名可依字母排序後符合你預期的順序  
  If merge order matters, name the files accordingly so they sort correctly alphabetically

---

## 📁 輸出結構範例 / Output Structure Example

```
原始資料夾 / Original Folder:
├── Unit1/
│   ├── Lesson1/
│   │   ├── handout1_CN).pdf
│   │   ├── handout2_CN).pdf
│   │   └── exercise_EN).pdf
│   └── Lesson2/
│       ├── material_CN).pdf
│       └── quiz_EN).pdf
└── handled_pdf/
    ├── Unit1_Lesson1_CN.pdf  (合併所有 CN 檔案)
    ├── Unit1_Lesson1_EN.pdf  (合併所有 EN 檔案)
    ├── Unit1_Lesson2_CN.pdf
    └── Unit1_Lesson2_EN.pdf
```

---

## 🚀 進階功能 / Advanced Features

### 多層次合併 / Multi-level Merging
工具支援對已處理的 PDF 進行二次合併，適用於複雜的資料夾結構。

The tool supports re-merging already processed PDFs, suitable for complex folder structures.

### 自動建立輸出資料夾 / Auto-create Output Folder
如果 `handled_pdf` 資料夾不存在，工具會自動建立。

If the `handled_pdf` folder doesn't exist, the tool will create it automatically.

---

## 🔧 客製化建議 / Customization Suggestions

### 擴展檔案類型 / Extend File Types
可修改程式碼以支援其他檔案結尾模式：

You can modify the code to support other file ending patterns:

```python
# 例如支援 _TC.pdf 和 _SC.pdf
# For example, support _TC.pdf and _SC.pdf
file_patterns = ['_TC.pdf', '_SC.pdf']
```

### GUI 版本 / GUI Version
考慮使用 `tkinter` 建立圖形化介面，提供更友善的使用體驗。

Consider using `tkinter` to create a graphical interface for better user experience.

---

## 🧠 開發者備註 / Developer Notes

歡迎改寫、優化此腳本！如有任何建議或需求，請隨時提出。

Feel free to customize or improve this script for your own use! Any suggestions or requirements are welcome.

### 可能的改進方向 / Potential Improvements
- 📊 加入進度條顯示
- 🎨 建立 GUI 介面
- 📸 製作操作教學 GIF
- ⚡ 提升大檔案處理效能
- 🔐 加入錯誤處理機制

---

## 📋 系統需求 / System Requirements

- Python 3.6+
- PyPDF2 套件
- 足夠的磁碟空間用於輸出檔案

---

## 📞 支援 / Support

如遇到問題或需要協助，請檢查：
- 檔案路徑是否正確
- PDF 檔案是否可正常開啟
- 磁碟空間是否充足

If you encounter issues or need help, please check:
- File paths are correct
- PDF files can be opened normally  
- Sufficient disk space available
