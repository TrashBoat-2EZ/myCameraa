import cv2
from datetime import datetime

text = str(datetime.now())

cam = cv2.VideoCapture(0)  # Set cam to cam number
cam.set(cv2.CAP_PROP_FPS, 30)  # Set FPS
cam.set(3, 1280)  # Set x resolution
cam.set(4, 720)  # Set y resolution

font = cv2.FONT_HERSHEY_PLAIN

fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Set Codec ('M', 'J', 'P', 'G') (*'DIVX')
out = cv2.VideoWriter("testVid.avi", fourcc, 17, (1280, 720))
while True:
    re, img = cam.read()  # Set camera read

    img = cv2.flip(img, 1)  # Flip on x axis

    #           Video  Text                                 Position  font  size   colour   Stroke
    cv2.putText(img, "You've Been Spotted", (520, 360), font, 1.5, (0, 0, 255), 1, cv2.LINE_AA)  # Display Text
    cv2.putText(img, text, (1000, 680), font, 1, (20, 200, 0), 1, cv2.LINE_AA)  # Display Date


    cv2.imshow("Mornin'", img)  # title
    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # Press "Esc " to quit
        break

cam.release
cv2.destroyAllWindows()
