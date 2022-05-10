from aiogram import types


def MainKlava():

    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Ввести комбинацию", callback_data="first")
    keyboardmain.add(first_button)
    return (keyboardmain)


def KlavaMulti(ivi: int, bk: int):

    k1='🔴' 
    k2='🟠'
    k3='🟡'
    k4='🟢'
    k5='🔵'  
    k6='🟣'
    k7='⚫'
    k8='⚪'
    k9='🟤'

    god='👍'
    notgod='👎'

    keyboard = types.InlineKeyboardMarkup()
    rele1 = types.InlineKeyboardButton(text='[ '+k1+' ]',  callback_data="1")
    rele2 = types.InlineKeyboardButton(text='[ '+k2+' ]',  callback_data="2")
    rele3 = types.InlineKeyboardButton(text='[ '+k3+' ]',  callback_data="3")
    rele4 = types.InlineKeyboardButton(text='[ '+k4+' ]',  callback_data="4")
    rele5 = types.InlineKeyboardButton(text='[ '+k5+' ]',  callback_data="5")
    rele6 = types.InlineKeyboardButton(text='[ '+k6+' ]',  callback_data="6")
    rele7 = types.InlineKeyboardButton(text='[ '+k7+' ]',  callback_data="7")
    rele8 = types.InlineKeyboardButton(text='[ '+k8+' ]',  callback_data="8")
    rele9 = types.InlineKeyboardButton(text='[ '+k9+' ]',  callback_data="9")
    bkbut = types.InlineKeyboardButton(text="🔙", callback_data="back")
    if ivi == 1 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, bkbut)
    if ivi == 1 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4)
    if ivi == 2 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, rele5, bkbut)
    if ivi == 2 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4, rele5)
    if ivi == 3 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, bkbut)
    if ivi == 3 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6)
    if ivi == 4 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7, bkbut)
    if ivi == 4 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7)
    if ivi == 5 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7, rele8, bkbut)
    if ivi == 5 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7, rele8)
    if ivi == 6 and bk == 1: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7, rele8, rele9, bkbut)
    if ivi == 6 and bk == 0: keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, rele7, rele8, rele9)
    return (keyboard)


def KlavaLevel():

    keyboard = types.InlineKeyboardMarkup()
    rele1 = types.InlineKeyboardButton(text='Уровень 1',  callback_data="lev1")
    rele2 = types.InlineKeyboardButton(text='Уровень 2',  callback_data="lev2")
    rele3 = types.InlineKeyboardButton(text='Уровень 3',  callback_data="lev3")
    rele4 = types.InlineKeyboardButton(text='Уровень 4',  callback_data="lev4")
    rele5 = types.InlineKeyboardButton(text='Уровень 5',  callback_data="lev5")
    rele6 = types.InlineKeyboardButton(text='Уровень 6',  callback_data="lev6")
    bkbut = types.InlineKeyboardButton(text="🔙", callback_data="backlvl")
    keyboard.add(rele1, rele2, rele3, rele4, rele5, rele6, bkbut)
    return (keyboard)


def KlavaEnter():
    god='👍'
    notgod='👎'
    keyboard = types.InlineKeyboardMarkup()
    rele1 = types.InlineKeyboardButton(text='Готово! '+god, callback_data="enter")
    rele2 = types.InlineKeyboardButton(text='Назад'+notgod, callback_data="back")
    keyboard.add(rele1, rele2)
    return (keyboard)


def SIntInShar (s: str):

    k1='🔴'
    k2='🟠'
    k3='🟡'
    k4='🟢'
    k5='🔵'
    k6='🟣'
    k7='⚫'
    k8='⚪'
    k9='🟤'
    dw=k1+k2+k3+k4+k5+k6+k7+k8+k9
    N=len(s)
    nws =''
    if N>9: otv = 'err01'
    else:
        for i in range(N):
            if s[i] in ['1','2','3','4','5','6','7','8','9']:
                k=int(s[i])-1
                nws = nws + dw[k]    
        otv=nws
    if len(otv)!=len(s): otv='err02'    
    return otv




def SharInSInt (s: str):
    
    k1='🔴'
    k2='🟠'
    k3='🟡'
    k4='🟢'
    k5='🔵'
    k6='🟣'
    k7='⚫'
    k8='⚪'
    k9='🟤'
    dw=k1+k2+k3+k4+k5+k6+k7+k8+k9
    N=len(s)
    res = ''
    for i in range(N):
        if s[i] in dw:
            for j in range(9):
                if dw[j] == s[i]: res += str(j+1)
                
    return res            
      

def ResInShar (s: str):
    
    c='⚫'
    b='⚪'
    
    N=len(s)
    res = ''

    for i in range(N):
        if s[i]=='1': res += b
        if s[i]=='2': res += c
    return res    
    
