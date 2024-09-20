import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('images.png', cv2.IMREAD_COLOR)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

recognizer = pytesseract.image_to_string(grey)
print("recognizer",recognizer)

_, binary_image = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
countour, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_copy = img.copy()
cv2.drawContours(image_copy, countour, -1, (0, 0, 255), 2)
cv2.imshow("image", binary_image)
cv2.imshow("imaga", image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()