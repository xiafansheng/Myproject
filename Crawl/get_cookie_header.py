def get_headers(textpath):
    text = open(textpath,'r',encoding='utf-8').readlines()
    headerlist = [i.split(':') for i in text if i]
    headers = {i[0].strip(' '):''.join(i[1:]).strip(' ').strip('\n') for i in headerlist}
    return headers

