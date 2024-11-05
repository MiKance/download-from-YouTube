from pytube import YouTube

while True:
    url = input("Enter url: ")
    try:
        yt = YouTube(url)
        break
    except:
        print('\nError\n')

print('\nAuthor: ', yt.author)
print('Title: ', yt.title)
print('Views: ', yt.views)
print('Url channel: ', yt.channel_url)
print('Length: ', yt.length//60, 'min', yt.length%60, 'sec')


yd = yt.streams.get_highest_resolution()
size = yd.filesize
print('File size:', (size//1024)+1, 'KB')
yd.download('/home/mikance/Загрузки')
print('Download is complete')
