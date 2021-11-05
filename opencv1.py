import cv2
#importing opencv-python

img = cv2.imread('assets/image 1.jpg', 1)
img = cv2.resize(img, (150, 130), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#loading some images
cv2.imwrite('new_img.jpg', img)

#writing to new file
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
