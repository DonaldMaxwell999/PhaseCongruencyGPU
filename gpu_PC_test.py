from phasecong_gpu import phasecongruency as PC
import cv2 as cv
import time

t_start = time.perf_counter()
im_path = 'test.jpg'
im = cv.imread(im_path, 0)
for i in range(100):
    pc = PC(im)
t_end = time.perf_counter()

print('100幅影像的GPU相位一致性运行时间为：' + str(t_end-t_start))
t = 0