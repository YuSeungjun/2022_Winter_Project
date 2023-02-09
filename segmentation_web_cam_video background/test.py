import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()

# 실제 이미지
imgBg = cv2.imread('C:/cv2_back/te.jpg')
imgBg = cv2.resize(imgBg, (1280, 720))

cap = cv2.VideoCapture(0)
capVideo = cv2.VideoCapture("C:/cv2_back/bts.mp4")

while True:
    # 실제 이미지
    ret, img = cap.read()

    # 실제 영상 프레임
    ret, videoFrame = capVideo.read()    
    if not ret:
        break


    # 해상도 수정 320 x 240 -> 1280, 720으로 변경
    img = cv2.resize(img, (1280, 720))
    videoFrame = cv2.resize(videoFrame, (1280, 720))

    imgBgVideo = segmentor.removeBG(img, videoFrame , threshold=0.50)

    # 완성본 열기
    # cv2.imshow('사진만',img)
    # cv2.imshow('내 얼굴',videoFrame)
    cv2.imshow('방탄소년단 영상',imgBgVideo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 끝
cap.release()
cv2.destroyAllWindows()