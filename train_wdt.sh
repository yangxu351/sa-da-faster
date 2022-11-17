# dataseed -1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python -W ignore tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc.yaml 

# dataseed -1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=2 python -W ignore tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_v2.yaml 

# dataseed 1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1 python tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd1.yaml 

# dataseed 2
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1 python tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd2.yaml 

# dataseed 1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1 python tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_WDT_voc_sd0.yaml 

''' with mask attention '''
## dataseed -1
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=2 python tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_RPNMask_WDT_voc_sd-1.yaml 

## dataseed 1
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python tools/train_net.py --config-file configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_RPNMask_WDT_voc_sd1.yaml 