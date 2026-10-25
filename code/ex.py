def make_matrix(key):
    char=[]
    key = key.upper().replace("J","I")
    
    for ch in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch in key and ch not in char:
            char.append(ch)
    return(char[i :i+5] for i in range(0,25,5) )

def pos(matrix ,ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i,j
            
            
def prepare_text(text):
    
    text = text.upper().repace("J","I")
    text = "". join(c for c in text if c.isalpha())
    res = ""
    i=0
    
    while i < len(text):
        a = text[i]
        
        if i+1 == len(text):
            res += a +"X"
            break 
        
        b = text[i+1]
        
        if a == b:
            res += a+"X"
            i += 1
        else:
            res += a+b
            i +=2
    return res



def enc(text, matrix):
    res =""
    
    for i in range(0,len(text),2):
        a , b =text[i] , text[i+1]
        
        r1,c1 = pos(matrix,a)
        r2,c2 = pos(matrix,b) 
        
        if r1 == r2:
            res += matrix[r1][(c1+1)%5]
            res += matrix[r2][(c2+1)%5]        
        elif c1==c2:
            res += matrix[(r1 +1)%5][c1]
            res += matrix[(r2 +1)%5][c2]
        else:
            res +=matrix[r1][c2]
            res +=matrix[r2][c1]
    
    
    
            
