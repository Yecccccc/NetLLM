import os
"""
used to extract features from video frames using a pre-trained ViT model
"""
class Config:
    init_dir =  "/mnt/c/Users/yec/Desktop/video_feature/video"
    base_dir = './dataset'
    source_video_dir = os.path.join(base_dir, 'video/source')
    image_dir = os.path.join(base_dir, 'video/images')
    feature_store_dir = os.path.join(base_dir, 'video_feature')
    store_step = 30  # save features every 30 frames (1s)
ext_cfg = Config()
