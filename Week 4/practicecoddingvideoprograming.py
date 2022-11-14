class Video:
    def __init__(self,title, link):
        self.title = title
        self.link = link

def read_video():
        title = input("Enter title: ")
        link = input("Enter link: ")
        video = Video(title, link)
        return video
    

def print_video(video):
        print("===============")
        print("Video title: ",video.title, end="")
        print("Video link: ", video.link, end="")


def read_videos():
    videos = []
    total_video = int(input("Enter how many video: "))    
    for i in range(total_video):
        print("Enter video ", i+1)
        vid = read_video()
        videos.append(vid)
    return videos


def print_videos(videos):
    for i in range(len(videos)):
        print_video(videos[i])
        

def write_to_txt(videos):
    total = len(videos)
    with open("data.txt","w") as file:
        file.write(str(total)+ "\n")
        for i in range(total):
            file.write((videos[i].title) + "\n")
            file.write((videos[i].link) + "\n")
            

def read_videos_from_txt():
    videos = []
    with open("data.txt", "r") as file:
        total = int(file.readline())
        for i in range(total):
            title = file.readline()
            link = file.readline()
            video = Video(title, link)
            videos.append(video)
    return videos

def main():
    videos = read_videos()
    write_to_txt(videos)
    videos = read_videos_from_txt()
    print_videos(videos)

main()        