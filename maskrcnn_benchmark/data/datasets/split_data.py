import os
import random
import argparse
import glob
import sys
sys.path.append('.')
BASE_DIR = '/data/users/yang/data'

def split_syn_real_wdt_by_data_seed(syn=False, data_seed=0):
    if syn:
        files = glob.glob(os.path.join(args.syn_voc_annos_dir, '*.xml'))
    else:
        files = glob.glob(os.path.join(args.real_voc_annos_dir, '*.xml'))

    all_name = 'all.txt'
    trn_name = f"train_seed{data_seed}.txt"
    val_name = f"val_seed{data_seed}.txt"

    files_name = sorted([os.path.basename(f).split(".")[0] for f in files])
    files_num = len(files_name)
    val_index = random.sample(range(0, files_num), k=int(files_num*val_rate))
    train_files = []
    val_files = []
    for index, file_name in enumerate(files_name):
        if index in val_index:
            val_files.append(file_name)
        else:
            train_files.append(file_name)
    print('len val files', len(val_files))
    try:
        all_f = open(os.path.join(args.workdir_main, all_name), "w")
        train_f = open(os.path.join(args.workdir_main, trn_name), "w")
        eval_f = open(os.path.join(args.workdir_main, val_name), "w")
        train_f.write("\n".join(train_files))
        eval_f.write("\n".join(val_files))
        all_f.write("\n".join(train_files+val_files))
    except FileExistsError as e:
        print(e)
        exit(1)

def record_real_val_aug_files(aug=False):  
    ''' 
        keep original val set (val_seed0), 
        copy original val set to val aug val set, 
        then record the val aug+ val original data files
        '''  
    if aug:
        # tag: ori + aug files
        files = glob.glob(os.path.join(args.real_voc_annos_aug_dir, '*.xml'))
        val_name = f"val_aug_seed{data_seed}.txt"
        files_name = sorted([os.path.basename(f).split(".")[0] for f in files])
        val_files = []
        for fn in files_name:
            val_files.append(fn)
        print('len val files', len(val_files))
        try:
            eval_f = open(os.path.join(args.workdir_main, val_name), "w")
            eval_f.write("\n".join(val_files))
        except FileExistsError as e:
            print(e)
            exit(1)
    

def get_arg(cmt='syn_wdt_rnd_sky_rnd_solar_rnd_cam_p3_shdw_step40', syn=True, folder_name='synthetic_data_wdt'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--syn_base_dir", type=str,
                        help="base path of synthetic data",
                        default=f'{BASE_DIR}/data/synthetic_data_wdt')

    parser.add_argument("--syn_data_dir", type=str, default='{}/{}',
                        help="Path to folder containing synthetic images and annos \{syn_base_dir\}/{cmt}")

    parser.add_argument("--syn_data_imgs_dir", type=str, default='{}/{}_images',
                        help="Path to folder containing synthetic images .jpg \{cmt\}/{cmt}_images")   

    parser.add_argument("--syn_data_segs_dir", type=str, default='{}/{}_annos_dilated',
                        help="Path to folder containing synthetic SegmentationClass .jpg \{cmt\}/{cmt}_annos_dilated")  

    parser.add_argument("--syn_voc_annos_dir", type=str, default='{}/{}_xml_annos/minr{}_linkr{}_px{}whr{}_all_xml_annos',
                        help="syn annos in voc format .xml \{syn_base_dir\}/{cmt}_xml_annos/minr{}_linkr{}_px{}whr{}_all_annos_with_bbox")     
    
    parser.add_argument("--real_base_dir", type=str,default=f'{BASE_DIR}/data/wind_turbine', help="base path of synthetic data")
    parser.add_argument("--real_imgs_dir", type=str, default='{}/{}_crop', help="Path to folder containing real images")
    parser.add_argument("--real_yolo_annos_dir", type=str, default='{}/{}_crop_label_xcycwh', help="Path to folder containing real annos of yolo format")
    parser.add_argument("--real_voc_annos_dir", type=str, default='{}/{}_crop_label_xml_annos', help="Path to folder containing real annos of voc .xml")
    # tag: yang adds
    parser.add_argument("--real_imgs_aug_dir", type=str, default='{}/{}_crop_aug', help="Path to folder containing real images")
    parser.add_argument("--real_voc_annos_aug_dir", type=str, default='{}/{}_crop_label_xml_annos_aug', help="Path to folder containing real annos of voc format")

    parser.add_argument("--workdir_data", type=str, default='{}/{}/{}',
                        help="workdir data base synwdt Base_dir/synthetic_data_wdt/\{cmt\}")
    # parser.add_argument("--workdir_imgsets", type=str, default='{}/ImageSets',
    #                     help="ImageSets folder")
    parser.add_argument("--workdir_main", type=str, default='{}/ImageSets/Main',
                        help="\{workdir_data\}/Main ")                
    parser.add_argument("--min_region", type=int, default=10, help="the smallest #pixels (area) to form an object")
    parser.add_argument("--link_r", type=int, default=10,  help="the #pixels between two connected components to be grouped")
    parser.add_argument("--px_thres", type=int, default=12, help="the smallest #pixels to form an edge")
    parser.add_argument("--whr_thres", type=int, default=5, help="ratio threshold of w/h or h/w")                        
    args = parser.parse_args()
    if syn:
        args.syn_data_dir = args.syn_data_dir.format(args.syn_base_dir, cmt)
        args.syn_data_imgs_dir = args.syn_data_imgs_dir.format(args.syn_data_dir, cmt)
        args.syn_data_segs_dir = args.syn_data_segs_dir.format(args.syn_data_dir, cmt)
        args.syn_voc_annos_dir = args.syn_voc_annos_dir.format(args.syn_base_dir, cmt, args.link_r, args.min_region, args.px_thres, args.whr_thres)
        
    else:
        args.real_imgs_dir = args.real_imgs_dir.format(args.real_base_dir, cmt)
        args.real_yolo_annos_dir = args.real_yolo_annos_dir.format(args.real_base_dir, cmt)
        args.real_voc_annos_dir = args.real_voc_annos_dir.format(args.real_base_dir, cmt)
        args.real_imgs_aug_dir = args.real_imgs_aug_dir.format(args.real_base_dir, cmt)
        args.real_voc_annos_aug_dir = args.real_voc_annos_aug_dir.format(args.real_base_dir, cmt)
        
    
    args.workdir_data = args.workdir_data.format(BASE_DIR, folder_name, cmt)
    # args.workdir_imgsets = args.workdir_imgsets.format(args.workdir_data)
    args.workdir_main = args.workdir_main.format(args.workdir_data)

    return args

if __name__ == '__main__':
    data_seed = 0 # default
    # data_seed = 1
    # data_seed = 2
    random.seed(data_seed)  # 设置随机种子，保证随机结果可复现

    ''' Syn wdt '''
    cmt = 'syn_wdt_rnd_sky_rnd_solar_rnd_cam_p3_shdw_step40'
    syn = True
    val_rate = 0.3
    folder_name = 'synthetic_data_wdt'
    args = get_arg(cmt, syn, folder_name)
    # split_syn_real_wdt_by_data_seed(syn, data_seed)
    ### 判断 val.txt and val_seed0.txt 记录是否相同，不考虑顺序
    import pandas as pd
    import numpy as np
    val_file = f'{args.workdir_main}/val.txt'
    val_seed_file = f'{args.workdir_main}/val_seed0.txt'
    df_val = pd.read_csv(val_file, header=None).to_numpy()[:,0]
    df_val_seed = pd.read_csv(val_seed_file, header=None).to_numpy()[:,0]
    val_seed_names = df_val_seed.tolist().sort()
    val_names = df_val.tolist().sort()
    if np.all(val_seed_names == val_names):
        print('YES')
    else:
        print('False')


    ''' Real wdt '''
    # cmt = 'xilin_wdt'
    # syn = False
    # val_rate = 0.3
    # # aug = False
    # aug = True

    # # cmt = 'DJI_wdt'
    # # syn = False
    # # val_rate = 1
    # # aug = False

    # data_folder = 'real_data_wdt'
    # args = get_arg(cmt, syn, data_folder)
    # split_syn_real_wdt_by_data_seed(syn, data_seed)
    # # aug real val set
    # record_real_val_aug_files(aug)

