import argparse
from yt_dlp import YoutubeDL

def get_args():
    psr  = argparse.ArgumentParser(
    prog='youtube_dl',
    usage='python main.py url [--type]',
    description='youtubeの動画ダウンロード'
    )
    # add_argumentメソッドを使って、コマンドラインから引数を受け取る処理を作成する
    psr.add_argument('url', help='youtube url')
    psr.add_argument('-t', '--type', help='拡張子')
    return psr.parse_args()


def main():
    args = get_args()
    option = {}
    if args.type:
        option = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  
                'preferredcodec': args.type,  #変換したい形式を指定
                'preferredquality': '192' #ビットレートを指定
            }]
        }
    ydl = YoutubeDL(option)
    result = ydl.download(args.url)
    print(result)

if __name__ == '__main__':
    main()