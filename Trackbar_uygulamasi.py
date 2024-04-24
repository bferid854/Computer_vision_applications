import cv2
import numpy as np

def nothing():
	pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("R","image",0,255,nothing) # (kızağın adı, pencerenin adı,
cv2.createTrackbar("G","image",0,255,nothing) # başlangıç değer,bitiş değer,fonksiyon)
cv2.createTrackbar("B","image",0,255,nothing)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch,"image",0,1,nothing)

while True:  # sürekli yenilensin diye while döngüsüne alıyoruz.
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # q ye basıldığında çıksın (1 millisaniyede yenilensin)
        break
    # (trackbar position fonksiyonuyla görevlendirme diye biliriz)
    r = cv2.getTrackbarPos("R", "image")  # ("Trackbar Adı", "Trackbar Penceresi")
    g = cv2.getTrackbarPos("G", "image")  # ("Trackbar Adı", "Trackbar Penceresi")
    b = cv2.getTrackbarPos("B", "image")  # ("Trackbar Adı", "Trackbar Penceresi")
    s = cv2.getTrackbarPos(switch, "image")  # ("Trackbar Adı", "Trackbar Penceresi")

    if s == 0:  # eğer switch 0 ise ekran değişmesin (beyaz kalsın)
        img[:] = [0, 0, 0]
        if s == 1:  # eğer switch 1 ise ekran trackbarda belirtilen renkleri alsın
    img[:] = [b, g, r]

cv2.destroyAllWindows()