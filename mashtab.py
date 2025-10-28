import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

ROTATE_ANGLE = 345
SCALE_FACTOR = 1.6
FONT_PATH = "arial.ttf"  

img = cv2.imread('input.jpg')
if img is None:
    print(" Кескін табылмады. 'input.jpg' файлы бір папкада бар екенін тексер.")
    exit()

original_img = img.copy()

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

def scale_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

def draw_buttons_with_unicode(image):
    btn_img = image.copy()

    cv2.rectangle(btn_img, (10, 10), (160, 60), (180, 105, 255), -1)   
    cv2.rectangle(btn_img, (180, 10), (360, 60), (255, 200, 150), -1)  

    pil_img = Image.fromarray(cv2.cvtColor(btn_img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    try:
        font = ImageFont.truetype(FONT_PATH, 24)
    except:
        print(" Шрифт табылмады. Arial.ttf немесе басқа Unicode шрифт жүктеп, файлмен бірге сақта.")
        exit()

    draw.text((25, 18), "Бұру", font=font, fill=(0, 0, 0))           
    draw.text((195, 18), "Масштабтау", font=font, fill=(0, 0, 0))

    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

def on_mouse(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 <= x <= 160 and 10 <= y <= 60:
            img = rotate_image(img, ROTATE_ANGLE)
            img = draw_buttons_with_unicode(img)
            cv2.imshow('Кескін', img)
        elif 180 <= x <= 360 and 10 <= y <= 60:
            img = scale_image(img, SCALE_FACTOR)
            img = draw_buttons_with_unicode(img)
            cv2.imshow('Кескін', img)

img = draw_buttons_with_unicode(img)

cv2.imshow('Кескін', img)
cv2.setMouseCallback('Кескін', on_mouse)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break

cv2.destroyAllWindows()
