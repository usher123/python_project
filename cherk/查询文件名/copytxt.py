##find /media/3933-3635  -regex ".*\.mp3\|.*\.MP3\|.*\.wma\|.*\.ape\|.*\.WAV">~/github/python_project/text/mp3name.txt

def copytxt(file):
    '''(file open fme_to_num[name]  num_to_name[1] = name
        or reading and copy)->dict of {list of str}
    read the file name  and return a dictionary'''

    line = file.readline().split('/')
    name = line[len(line)-1]
    c=name.rfind('.')
    name=name[:c]
    name_to_num = {}
    num_to_name = {}
    n = 1
    while line != ['']:

        if name not in name_to_num :
            name_to_num[name] = [n]
            
        elif name in name_to_num:
            name_to_num[name].append(n)

        
        if n not in num_to_name:
            num_to_name[n] = name
                 
       
        line = file.readline().split('/')
        name = line[len(line)-1]
        c=name.rfind('.')
        name=name[:c]
        n = n+1

    o='4'
    while(o!='3'):
        if o=='1':
            q=input('what\'s name do you check to num:')
            while q != '':
                if q not in name_to_num:
                    print ('not existence')
                else:
                    print (name_to_num[q])
                q=input('what\'s name do you check to num:')

        elif o=='2':
            q=input('what\'s num do you check to name:')
            while q != '':
                if int(q) not in num_to_name:
                    print ('not existence')
                else:
                    print (num_to_name[int(q)])
                q=input('what\'s num do you check to name:')
        o = input('what you want: 1.name_to_num 2.num_to_name 3.exit')

    print('num:',len(num_to_name))
##   return name_to_num
if __name__ == '__main__':
    file = open('/home/zhangpeng/github/python_project/text/mp3name.txt')  
    print(copytxt(file))

