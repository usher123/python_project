

def cherk():
    a=input('input a string:')
    c=[]
    b=''
    d=''
    for int in range(len(a)):
        if a[int]!=' ':
            c.append(a[int])
            d=d+a[int]
      


    c.reverse()
    for int in range(len(c)):
        b=b+c[int ]

     
    print('this string is reverse num: ')

    if d==b:
        print (1==1)
    else: 
        print (1!=1)

if __name__=="__main__":
    cherk()

