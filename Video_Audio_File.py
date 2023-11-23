import cv2
from ffpyplayer.player import MediaPlayer

# Replace this with the path to your video file
file = "R:\PROJECTS\I -Bot\All Facial expressions\Smile face.mp4"

# Create a VideoCapture object to read the video file
video = cv2.VideoCapture(file)

# Check if the video file was opened successfully
if not video.isOpened():
    print("Error: Could not open video file.")
    exit()

# Create a MediaPlayer object to play the audio of the video
player = MediaPlayer(file)

while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Check if the video has reached the end
    if not ret:
        break

    # Get the audio frame and play it
    audio_frame, val = player.get_frame()
    if val != 'eof' and audio_frame is not None:
        # audio_frame contains the audio data; you can play it using an audio library
        pass

    # Display the video frame
    cv2.imshow('Video', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the OpenCV window
video.release()
cv2.destroyAllWindows()
