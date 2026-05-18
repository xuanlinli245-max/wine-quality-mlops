import os

def find_file(filename, search_path):
    """在指定路径下搜索文件"""
    print(f"正在搜索: {filename}")
    print(f"搜索范围: {search_path}")
    print("-" * 50)
    
    found_files = []
    
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            found_files.append(full_path)
            print(f"✅ 找到: {full_path}")
    
    return found_files

# 搜索整个 C 盘（如果C盘太大，可以只搜桌面）
# 方法1：搜索整个 C 盘（耗时较长）
# search_path = "C:\\"

# 方法2：只搜索桌面（推荐，更快）
desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
search_path = desktop_path

print(f"搜索路径: {search_path}\n")

# 搜索 CSV 文件
results = find_file("winequality-red.csv", search_path)

# 搜索 model.pkl
print("\n" + "-" * 50)
results_pkl = find_file("model.pkl", search_path)

if not results and not results_pkl:
    print("\n❌ 没有找到文件！")
    print("可能的原因：")
    print("1. 文件还没下载")
    print("2. 文件在其他盘（D盘、E盘等）")
    print("3. 文件名不一样")