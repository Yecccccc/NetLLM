# 视频偏好模块

## Pipeline设计

输入x维度[bs,seq_len,feature_dim]

### auto_regressive

1. 对每个时间序列的x进行cnn->linear，按照时间维度进行拼接
2. 拼接多模态信息
3. 按照未来窗口长度使用plm进行预测
   1. 得到预测结果
   2. 将预测结果拼接入x继续进行预测

### teaching_force

1. 直接拿到x和ground truth，将x和ground truth进行拼接
2. 和auto_regressive不同的是，一个使用自己预测出来的值拼接到x上，一个使用ground truth拼接到x上

##  video_perferencer训练命令

```sh
python run_plm.py --adapt --his-window 3 --fut-window 3 --plm-type llama --plm-size base --epochs 40 --bs 1 --lr 0.0002 --grad-accum-steps 32 --device cuda:0 --steps-per-valid 5000 --save-checkpoint-per-epoch 1 --rank 32 --scheduled-sampling --video_len 10
```

## VIT多模态特征提取模块

1. tools/get_source_video.py：将数据集里的源视频(10s 1080p30fps)的视频拷贝到指定位置
2. tools/get_video_images.py：使用ffmpeg提取视频的每一帧的图像并且保存
3. dataset/extract_feateure.py：仿照viewpoint_predicition模块，将视频每1秒的30帧提取出来
4. dataset/video_feature：存放20个视频的VIT特征pth文件
