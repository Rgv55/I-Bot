import cv2
file = "R:\PROJECTS\I -Bot\All Facial expressions\Smile face.mp4"
video = cv2.VideoCapture(file)
while True:
    ret, frame = video.read()  # Read a frame
    if not ret:
        break  # Exit the loop if we reached the end of the video
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
