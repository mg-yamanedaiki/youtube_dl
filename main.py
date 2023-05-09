from yt_dlp import YoutubeDL
#オプションを指定（最高音質の音声をmp3形式でダウンロードする）
option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp4',  #変換したい形式を指定
            'preferredquality': '192' #ビットレートを指定
        }]
    }
ydl = YoutubeDL({})
result = ydl.download('https://www.youtube.com/watch?v=kwfPxOM415o&ab_channel=ChilliBeans.')
print(result)