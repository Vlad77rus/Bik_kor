from aiogram import types


def MainKlava():

    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Ввести комбинацию", callback_data="first")
    keyboardmain.add(first_button)
    return (keyboardmain)





def SharInSInt (s: str):

    dw = ["0","1","2","3","4","5","6","7","8","9"]
    
    res = ''
    
    for i in range(len(s)):
        if s[i] in dw: res += s[i]

    return res            
      

def ResInShar (s: str):
    
    c='🐃'
    b='🐄'
    
    N=len(s)
    res = ''

    for i in range(N):
        if s[i]=='1': res += b
        if s[i]=='2': res += c
    return res    
    
