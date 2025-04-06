import os
import PyPDF2

def merge_pdfs_in_folder(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        pdf_cn = [f for f in filenames if f.endswith("CN).pdf")]
        pdf_en = [f for f in filenames if f.endswith("EN).pdf")]
        
        if not pdf_cn and not pdf_en:
            continue
        
        # 提取子子資料夾名稱作為文件名
        relative_path = os.path.relpath(dirpath, root_folder)
        folder_name = relative_path.replace(os.sep, "_")
        
        handled_folder = os.path.join(root_folder, "handled_pdf")
        os.makedirs(handled_folder, exist_ok=True)
        
        if pdf_cn:
            merge_pdfs(dirpath, pdf_cn, os.path.join(handled_folder, f"{folder_name}_CN.pdf"))
        if pdf_en:
            merge_pdfs(dirpath, pdf_en, os.path.join(handled_folder, f"{folder_name}_EN.pdf"))
    return folder_name, handled_folder

def merge_pdfs_in_folder2(root_folder, folder_name):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        pdf_cn = [f for f in filenames if f.endswith("CN.pdf")]
        pdf_en = [f for f in filenames if f.endswith("EN.pdf")]
        
        if not pdf_cn and not pdf_en:
            continue
        
        # 提取子子資料夾名稱作為文件名
        relative_path = os.path.relpath(dirpath, root_folder)
        folder_name = relative_path.replace(os.sep, "_")
        
        handled_folder = os.path.join(root_folder, "handled_pdf")
        os.makedirs(handled_folder, exist_ok=True)
        
        if pdf_cn:
            merge_pdfs(dirpath, pdf_cn, os.path.join(handled_folder, f"{folder_name}_CN.pdf"))
        if pdf_en:
            merge_pdfs(dirpath, pdf_en, os.path.join(handled_folder, f"{folder_name}_EN.pdf"))

def merge_pdfs(dirpath, pdf_files, output_filename):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_files.sort()
    
    for pdf in pdf_files:
        pdf_merger.append(os.path.join(dirpath, pdf))
    
    with open(output_filename, "wb") as output_pdf:
        pdf_merger.write(output_pdf)
    
    print(f"合併完成，輸出文件: {output_filename}")

if __name__ == "__main__":
    root_folder = input("請輸入要處理的資料夾路徑: ")
    #root_folder=r"C:\Users\chris\OneDrive\Desktop\Merit College Chris folder\Teaching Folder\Art\Photography\Teaching Materials\Unit 1\U1L3\Handout"
    folder_name, handled_folder = merge_pdfs_in_folder(root_folder)
    merge_pdfs_in_folder2(handled_folder, folder_name)