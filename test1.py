import cv2

image = cv2.imread("track1.png")
for i in range (0,529):
    for j in range(0,419):
        b,g,r =image[i][j]
        if ((b<150) and (g<=150) and (r>=150)):
            image[i][j]=255,255,255


cv2.imshow("fhsda",image)
cv2.waitKey()