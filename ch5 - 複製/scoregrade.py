#score=int(input('請輸入成績0-100分: '))
#if score<60:   #條件1
#    print('戊等')
#elif score <70:  #條件2
#    print('丁等')
#elif score<80: #條件3
#    print('丙等')    
#elif score<90: #條件4
#    print('乙等')
#elif score<100: #條件5
#    print('甲等')
#else:  #條件6
#    print('輸入錯誤')   
#

score=int(input('輸入成績0-100分: '))
grade='輸入'
if score<60:  #條件1
    grade='戊等'
elif score <70:  #條件2
    grade='丁等'
elif score<80:  #條件3
    grade='丙等'    
elif score<90:  #條件4
    grade='乙等'
elif score<100:  #條件5
    grade='甲等'
else:    #條件6
    grade='輸入錯誤'
print (score,grade) 
     
