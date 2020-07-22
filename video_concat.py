import glob
import natsort
import sys
import subprocess

def main(video_dir, output):
    video_list = natsort.natsorted(glob.glob("{}/*".format(video_dir)))
    print("target folder :{}".format(video_dir))
    with open("concat.txt", "w") as f :
        for _, path in enumerate(video_list):
            line = "file {}\n".format(path)
            print(line)
            f.write(line)
    print("convert start")

    cmd ="sh ffmpeg_concat.sh {}".format(output)
    subprocess.run(cmd.split())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])