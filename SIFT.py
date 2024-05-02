import cv2 as cv

img = cv.imread('mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp,des=sift.detectAndCo,pute(gray,None)

gray = cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift'. gray)

k=cv.waitKey()
cv.destroyAllWindows()