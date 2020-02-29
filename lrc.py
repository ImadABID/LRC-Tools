Balises=[]#[ [[min,seconde],lyrics],...]

def cut(T,D):
    global Balises
    for i in range(len(Balises)):
        if SupOrEq(Balises[i][0],T):
            Balises[i][0]=soustraire(Balises[i][0], D)

def extract_data(lrcfile_path):
    global Balises
    lrc_file=open(lrcfile_path,"r")
    txt=lrc_file.read()
    i=3
    while i < len(txt):
        si=sperator_index(txt,'\n',i)
        Balises+=[[[int(txt[i+1:i+3]),int(txt[i+4:i+6])],txt[i+10:si]]]
        i=si+1
    return Balises

    lrc_file.close()

def exportdata(lrcfile_path):
    txt=''
    for b in Balises:
        mn=b[0][0]
        s=b[0][1]
        lyrcs=b[1]
        if mn>=0 and s>=0 and len(lyrcs)!=0 :
            txt+='['+add_zeros(2,str(mn))+':'+add_zeros(2,str(s))+'.00]'+lyrcs+'\n'

    lrc_file=open(lrcfile_path,"w")
    lrc_file.write(txt[:len(txt)-1])
    lrc_file.close()

def soustraire(T, D):
    s=T[0]*60+T[1]-(D[0]*60+D[1])
    mn=0
    while(s>=60):
        mn+=1
        s-=60
    return [mn,s]

def SupOrEq(T1,T2):
    if T1[0]==T2[0] :
        return T1[1]>=T2[1]
    return T1[0]>T2[0]

def sperator_index(txt,sperator,start_search_from_index):
    for i in range(start_search_from_index,len(txt)):
        if txt[i]==sperator:
            return i
    return None

def add_zeros(nbr_chiffre,txt):
    while(len(txt)<nbr_chiffre):
        txt='0'+txt
    return txt