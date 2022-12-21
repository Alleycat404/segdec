import glob
import os
import random
import shutil

KSDD = 'KSDD'
root_dir = 'E:/denso/mixed-segdec-net-comind2021-master/results/KSDD/N_33/FOLD_1/test_outputs'
target_dir = 'Data1'
full_sample = os.listdir(root_dir)
for sample in full_sample:
    folder = sample[13:18]
    file = sample[19:28]
    shutil.move(os.path.join(KSDD, folder, file), os.path.join(target_dir, 'Test', folder + '_' + file))


samples = glob.glob(KSDD + '/*/*.jpg')

for sample in samples:
    folder = sample[5:10]
    file = sample[11:21]
    shutil.move(os.path.join(KSDD, folder, file), os.path.join(target_dir, 'Train', folder + '_' + file))
    shutil.move(os.path.join(KSDD, folder, file[0:5] + '_label.bmp'), os.path.join(target_dir, 'Train', folder + '_' + file[0:5] + '_label.bmp'))

errors = glob.glob(KSDD + '/*/*.jpg')

for error in errors:
    print(error)
