import cv2

video = "192357-892475199_small.mp4"
output_folder = "output"
def main():
    videoCapture = cv2.VideoCapture(video)

    fps = videoCapture.get(cv2.CAP_PROP_FPS)

    print(fps)
    width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))



    print(width, height)
'''
def get_frames(video, output_folder):
    videoCapture = cv2.VideoCapture(video)

    fpP = int(videoCapture.get(cv2.CAP_PROP_FRAME_COUNT))

    print(fpP)

    width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(width, height)

    counter = 0
    success=True
    while success:
        success, frame = videoCapture.read()
        if success:
           cv2.imwrite("{}/frame{:d}.jpg".format(output_folder, counter), frame)  # save frame as JPEG"output_folder + "/" + str(counter) + ".jpg", frame)
           counter = counter + 1


get_frames(video, output_folder)
'''
output_video="output.mp4"
videoCapture = cv2.VideoCapture(video)
fps = videoCapture.get(cv2.CAP_PROP_FPS)
width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_video_path = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:
    ret, frame = videoCapture.read()
    if ret:
        break
    output_video_path.write(frame)

videoCapture.release()
output_video_path.release()

main()


