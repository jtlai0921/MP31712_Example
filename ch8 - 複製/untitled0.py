# E_8_8: Raise 引發異常
try: 
    num=100+'50'
    raise TypeError 
except TypeError as e: 
    print('資料型別錯誤，字串不能算術運算: ' + str(e))  