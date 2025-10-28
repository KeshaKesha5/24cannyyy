import cv2
import numpy as np

image = cv2.imread('image.jpg')
if image is None:
    raise FileNotFoundError("Файл 'image.jpg' не найден. Убедись, что он в той же папке.")

scale = 1.3
resized_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

angle = 50
(h, w) = resized_image.shape[:2]
center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (w, h))

cv2.imshow("Original", image)
cv2.imshow("Resized", resized_image)
cv2.imshow("Rotated", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
