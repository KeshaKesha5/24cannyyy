import cv2
import numpy as np

image = cv2.imread('image2.jpg')

if image is None:
    raise Exception("Кескін табылмады. Файл атауын немесе жолын тексеріңіз.")

scale = 0.9
new_width = int(image.shape[1] * scale)
new_height = int(image.shape[0] * scale)
resized_image = cv2.resize(image, (new_width, new_height))

angle = 135
center = (new_width // 2, new_height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (new_width, new_height))

# 4. Нәтижелерді көрсету
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Rotated Image', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()