def callfunc(n):
    if n.isdigit():
        number=int(n)        
        print('1累加到n的結果 = ', sumnfunc(number))        
        print('1累乘到n的結果 = ', prodnfunc(number))        
    else:
        print('請輸入數值資料')    
def sumnfunc(n):
    sumn=0
    for i in range(1,n+1):
        sumn=sumn+i
    return(sumn)   
def prodnfunc(n):
    prodn=1
    for i in range(1,n+1):
        prodn=prodn*i
    return(prodn)    
num=input('輸入一個正整數n = ')
callfunc(num)


