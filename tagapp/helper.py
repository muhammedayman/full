import datetime;

def write_file(tag,request):
    ct = datetime.datetime.now()
    ts = ct.timestamp()
    content = f'{tag}    {ts}    {request.user.username}'
    file_name = f'data\{tag}.txt'
    f= open(file_name,'w')
    f.write(content)
    f.close()
    url = f'media/{file_name}'
    return content