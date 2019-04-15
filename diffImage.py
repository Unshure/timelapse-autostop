import numpy as np
import cv2

np.set_printoptions(threshold=np.nan)

image1 = cv2.imread('0000.jpeg', 0)

cv2.imshow("image1", image1)
cv2.waitKey(0)

image2 = cv2.imread('0001.jpeg', 0)

cv2.imshow("image2", image2)
cv2.waitKey(0)

difference = cv2.absdiff(image1, image2)

cv2.imshow("Difference", difference)
cv2.waitKey(0)

cv2.destroyAllWindows()


print(np.sum(difference))
