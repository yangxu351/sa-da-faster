# 70000 iterations dataseed-1 # train with Maskrcnn-benchmark/maskrcnn_benchmark 
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd-1.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221114_0640_R-50-C4_Weights/modle_final.pth # 0.5175

# 70000 iterations dataseed-1  train with maskrcnn_benchmark 
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd-1.yaml --ckpt /data/users/yang/code/sa_da_faster/output、20221116_0606_R-50-FPN_Config/modle_final.pth # 4199

# 70000 iterations dataseed0
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd0.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221115_2308_R-50-FPN_sd0_Weights/modle_final.pth #  0.3298

# 70000 iterations dataseed0
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd0.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221118_1144_R-50-FPN_sd0_Weights/modle_final.pth # 0.3405

# 70000 iterations dataseed1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd1.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221115_0718_R-50-FPN_sd1_Weights/modle_final.pth # 0.4227 

# 70000 iterations dataseed1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd1.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221115_0718_R-50-FPN_sd1_Weights/modle_final.pth # 0.4295

# 70000 iterations dataseed2
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd2.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221115_1220_R-50-FPN_sd2_Weights/modle_final.pth # 0.3541

# 360000 iterations  dataseed-1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=3 python tools/test_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc.yaml --ckpt /data/users/yang/code/sa_da_faster/output/20221113_1113_R-50-C4_Weights/modle_final.pth # 0.5243