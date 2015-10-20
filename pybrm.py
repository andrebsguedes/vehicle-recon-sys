import cv2

imageA = cv2.imread("input/side.png")
imageB = cv2.imread("input/noside.png")
imageC = cv2.absdiff(imageA, imageB)
grayC = cv2.cvtColor(imageC, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(grayC, 70, 255, cv2.THRESH_BINARY)
result = cv2.bitwise_and(imageA, imageA, mask = mask)
cv2.imshow('res',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
