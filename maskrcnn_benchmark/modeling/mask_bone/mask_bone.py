import torch 
import torch.nn as nn
from torch.nn import functional as F


class MaskBone(nn.Module):
    def __init__(self, cfg):
        super(MaskBone, self).__init__()
        self.soft_val = cfg.MODEL.SOFT_VAL
        self.layer_levels = cfg.MODEL.LAYER_LEVELS
    
    def forward(self, features, masks=None):
        atten_features = []
        for k, feat in enumerate(features):
            if masks is not None and k in self.layer_levels:
                feat_shape = feat.shape[-2:]
                msk = F.interpolate(masks, size=feat_shape, mode="nearest")
                if self.soft_val == -1:
                    soft_msk = torch.rand_like(msk)
                    soft_msk[msk==1] = 1
                elif self.soft_val == -0.5:
                    soft_msk = torch.rand_like(msk)//2
                    soft_msk[msk==1] = 1
                else:
                    soft_msk = torch.ones_like(msk)*self.soft_val
                    soft_msk[msk==1] = 1
                atten_features.append(feat*soft_msk)
            
        return atten_features