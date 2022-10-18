import cv2

img_basic = cv2.imread('pd.JPG',cv2.IMREAD_COLOR)
cv2.imshow('Image Basic',img_basic)
cv2.waitKey(0)