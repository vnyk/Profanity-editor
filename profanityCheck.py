import urllib
def reads():
    file=open("G:/desktop/mspic.txt")
    content=file.read()
    #print(content)
    file.close()
    check_profanity(content)

def check_profanity(text):
    f = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text)
    op= f.read()
    print(op)
    f.close()
    if "true" in op:
        print('profanity Alert!!')
    elif "false" in op:
        print('no errors')
    else:
        print()
reads()
    
