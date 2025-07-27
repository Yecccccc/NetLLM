import os
import subprocess

# 输入和输出目录
video_dir = "/home/yec/NetLLM/video_preference/dataset/video/source"
output_root = "/home/yec/NetLLM/video_preference/dataset/video/images"

# 遍历每个视频文件
for video_file in os.listdir(video_dir):
    if not video_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        continue  # 忽略非视频文件

    video_path = os.path.join(video_dir, video_file)
    video_name = os.path.splitext(video_file)[0]
    output_dir = os.path.join(output_root, video_name)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 构造 ffmpeg 命令：提取所有帧为 frame_001.png, frame_002.png, ...
    output_pattern = os.path.join(output_dir, "frame_%03d.png")
    cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", "fps=30",  # 保证以30fps提取
        output_pattern
    ]
    
    print(f"正在提取帧: {video_file} 到 {output_dir}")
    subprocess.run(cmd, check=True)

print("所有视频帧提取完成。")
