import os
import shutil
from dataset.extract_config import ext_cfg

# 1. 获取所有子目录路径
base_path = ext_cfg.init_dir
all_dirs = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

# 记录在 b 中
b = all_dirs

# 检查是否有目录
if not b:
    print("没有找到任何子目录。")
    exit()

for item in b:
    # 目标文件路径
    source_video = os.path.join(item, "source.mp4")

    # 新的名字：使用该路径的最后一层目录名
    new_name = os.path.basename(item) + ".mp4"
    target_path = os.path.join(ext_cfg.source_video_dir, new_name)

    # 创建目标目录（如果不存在）
    os.makedirs(ext_cfg.source_video_dir, exist_ok=True)

    # 拷贝并重命名
    shutil.copy(source_video, target_path)

    print(f"已将 {source_video} 拷贝为 {target_path}")
