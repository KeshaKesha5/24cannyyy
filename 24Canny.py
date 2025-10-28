import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Face.png", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7)  
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=7)   
sobel_combined = cv2.magnitude(sobelx, sobely)

canny_edges = cv2.Canny(img, 205, 280)

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Исходное изображение")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(sobel_combined, cmap='gray')
plt.title("Границы (Sobel ksize=7)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(canny_edges, cmap='gray')
plt.title("Границы (Canny 205,280)")
plt.axis("off")

plt.tight_layout()
plt.show()
