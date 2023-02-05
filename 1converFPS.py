import cv2
import os

def change_fps(input_folder, output_folder, fps=25):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

    for i, video_file in enumerate(video_files):
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, f"{video_file}")

        cap = cv2.VideoCapture(input_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        print(f"Processing video {i+1} of {len(video_files)}: {input_path}")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            out.write(frame)

        cap.release()
        out.release()
        print(f"Video {i+1} of {len(video_files)} processed, fps changed to {fps}. Output file: {output_path}")

if __name__ == "__main__":
    input_folder = r"/home/chenj0g/2fps25/rgb_flowvideo1"
    output_folder = r"/home/chenj0g/2fps25/fps25_video1"
    fps = 25
    change_fps(input_folder, output_folder, fps)
