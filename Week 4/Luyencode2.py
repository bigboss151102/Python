class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        
def read_video():
    title = input("Title video: ")
    link = input("Link video: ")
    video = Video(title, link)
    return video

def print_video(video):
    print("===============")
    print("Title video: ", video.title, end = "")
    print("Link video: ", video.link, end = "")
    
def read_videos():
    videos = []
    total_video = int(input("How many video:"))
    for i in range(total_video):
        print("Video ", i+1)
        video = read_video()
        videos.append(video)
    return videos

def print_videos(videos):
    total = len(videos)
    for i in range(total):
        print_video(videos[i])
        
def write_videos_to_txt(videos):
    total = len(videos)
    with open("data.txt", "w") as file:
        file.write(str(total) + "\n")
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
    write_videos_to_txt(videos)
    videos = read_videos_from_txt()
    print_videos(videos)
    
main()
        
         
        
                  