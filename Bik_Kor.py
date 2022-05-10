from aiogram import types, Bot 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import SLdb, random
from config import STR1, TOKEN, ABOUT, QIWI_PAB_KEY
from keyboards import *
import datetime, time



k1='🔴'
k2='🟠'
k3='🟡'
k4='🟢'
k5='🔵'
k6='🟣'
k7='⚫'
k8='⚪'
k9='🟤'


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

 
@dp.message_handler(content_types=['text'])
async def hueta(message):

        if message.text == '/help':
            ans = STR1
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['/new_game','/champs','/help']])
            await bot.send_message(message.chat.id, ans, reply_markup=keyboard) 

        elif message.text == '/about':

            com = str(message.chat.id)+"-"+str(random.randint(100000, 999999)) 

            url= 'https://oplata.qiwi.com/create?'

            bil= "commonpay"+com    
            silka = f'{url}publicKey={QIWI_PAB_KEY}&billId={bil}&comment={com}'


            keyboard = types.ReplyKeyboardRemove(selective=False) 
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            but1 = types.InlineKeyboardButton(text="📨 Написать разработчику", url="https://t.me/ivldru")
            but2 = types.InlineKeyboardButton(text="💰 Донат", url=silka)
            keyboard.add(but1, but2)
            await bot.send_message(message.chat.id, ABOUT, reply_markup=keyboard)

        elif message.text == '/drop_game':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['/new_game','/champs','/help']])
            await bot.send_message(message.chat.id, f'''Возможно вы выбрали слишком сложный уровень...

🎮  /new_game - новая игра

🏆  /champs - таблица чемпионов

🙂  /my_game - мои лучшие игры

❓  /help - помощь

🔍  /about - о программе ''', reply_markup=keyboard)

        elif message.text == '/new_game':
            db.updbplayer(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, message.chat.title, message.from_user.language_code)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['level_1','level_2','level_3']])
            keyboard.add(*[types.KeyboardButton(name) for name in ['level_4','level_5','level_6']])
            await bot.send_message(message.chat.id, f'''Выберите уровень, где 1 самый легкий, а 6 - сложный. Не переоценивайте свои силы, начните с легкого.

1️⃣  - {k1+k2+k3+k4}

2️⃣  - {k1+k2+k3+k4+k5}

3️⃣  - {k1+k2+k3+k4+k5+k6}

4️⃣  - {k1+k2+k3+k4+k5+k6+k7}

5️⃣  - {k1+k2+k3+k4+k5+k6+k7+k8}

6️⃣  - {k1+k2+k3+k4+k5+k6+k7+k8+k9}

''', reply_markup=keyboard) 
            ans = ''
            
        elif message.text == '/start':
            ans = '''Игра "Логика Цвета" приветствует вас!

❓  /help - как играть?'''        
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['/help']])
            await bot.send_message(message.chat.id, ans, reply_markup=keyboard) 


        elif message.text == '/champs':
            rest = db.seechamp()
            mst = 1
            ans = '....Рейтинг победителей  🏆 \n\n'
            if rest != []: 
                for x in rest:
                    okn = 'ов'
                    if int(x[3]) in [2,3,4]: okn = 'а'
                    if int(x[3]) in [1]: okn = ''
                    mins=x[4]//60
                    secc=x[4]%60
                    mesto = str(mst)
                    if mst==1: mesto ='🥇'
                    if mst==2: mesto ='🥈'
                    if mst==3: mesto ='🥉'
                    ans=ans + mesto+' '+x[0]+' - '+x[1]+'\n    уровень-'+str(x[2])+' за '+str(x[3])+f' ход{okn} - '+ str(mins)+'мин. '+str(secc)+'с.\n\n'
                    mst+=1
                await bot.send_message(message.chat.id, ans)


        elif message.text == '/my_game':
            ans = db.view_my_game(message.chat.id)  
            await bot.send_message(message.chat.id, ans)  
               

        elif message.text in ['level_1','level_2','level_3','level_4','level_5','level_6']:
               
                if message.text == 'level_1': 
                    lvl=1
                    col = k1+k2+k3+k4

                if message.text == 'level_2':
                    lvl=2
                    col = k1+k2+k3+k4+k5

                if message.text == 'level_3':
                    lvl=3
                    col = k1+k2+k3+k4+k5+k6

                if message.text == 'level_4':
                    lvl=4
                    col = k1+k2+k3+k4+k5+k6+k7
                
                if message.text == 'level_5':
                    lvl=5
                    col = k1+k2+k3+k4+k5+k6+k7+k8

                if message.text == 'level_6':
                    lvl=6
                    col = k1+k2+k3+k4+k5+k6+k7+k8+k9

                db.new_game (message.chat.id, int(time.mktime(message.date.timetuple())),lvl)
                keyboard = types.ReplyKeyboardRemove(selective=False)           # убиваем клаву Reply
                await bot.send_message(message.chat.id, f'''Комбинация из цветов-
{col}
успешно загадана.
Для ввода вариата используйте цветные кружочки на закладке "Символы". Если это невозможно воспользуйтесь встроенной клавиатурой. Для ёё активации нажмите

сюда 👉 /Continue

Ваш вариант: ''', reply_markup=keyboard)
#                print(str(lvl))
              
                


        elif db.pole_from_b('game', 'Now_Game' , message.chat.id)=='1' :
                
            lv = int(db.pole_from_b('game', 'Level' , message.chat.id))    

            if message.text == '/Continue':
                db.write_klava_variant(message.chat.id, '0')
                keyboardmain = KlavaMulti(lv, 0)                               # Inline клавиатура back -on 
                await bot.send_message(message.chat.id, 'Ваша Комбинация:', reply_markup=keyboardmain)
            else:
                    mt = SharInSInt (message.text)
                    ans = db.otsenka (message.chat.id, mt)                            
                    
#                    print(ans)
#                    print('======================================')
            
                    if ans == 'Victory !!!':
                        print('ПОБЕДА!')    
                        ret = db.updbvictory(message.chat.id, int(time.mktime(message.date.timetuple())))
                        q= ret[0]
                        w= ret[1]
                
                        okn = 'ов'
                        if int(q[len(q)-1]) in [2,3,4]: okn = 'а'
                        if int(q[len(q)-1]) in [1]: okn = ''
                        okw = ''
                        if int(w[len(w)-1]) in [2,3,4]: okw = 'ы'
                        if int(w[len(w)-1]) in [1]: okw = 'у'
                
                        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        keyboard.add(*[types.KeyboardButton(name) for name in ['/new_game','/champs','/help']])
                        await bot.send_message(message.chat.id, f'''Вы угадали комбинацию за {ret[0]} ход{okn}, затратив на это {ret[1]} секунд{okw}.
Мои поздравления!

🎮  /new_game - новая игра

🏆  /champs - таблица чемпионов

🙂  /my_game - мои лучшие игры

❓  /help - помощь

🔍  /about - о программе ''', reply_markup=keyboard)
                    else:
                        if ans == 'err01': ans = 'неверный ввод'
                        elif ans == 'No': ans = 'Вы не угадали ни одного цвета.'
                        else: ans = ResInShar(ans)    
                        await bot.send_message(message.chat.id, ans)





@dp.callback_query_handler(lambda c: c.data)
async def callback_inline(call):
  
        lvl = int(db.pole_from_b('game', 'Level' , call.message.chat.id))
        st = db.read_klava_variant(call.message.chat.id)         

        if call.data in ['1','2','3','4','5','6','7','8','9'] :
               
            if st == '0':
                print (st, call.data)    
                st=str(call.data)  
            else:
                st += str(call.data)

            db.write_klava_variant(call.message.chat.id, st)                    # запоминаем st в базу

            if len(st) >= (lvl+3):
                st = SIntInShar(st)                                             # st в шарики
                keyboard=KlavaEnter()                                           # Inline клавиатура Enter
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)   

            else:    
                st = SIntInShar(st)                                             # st в шарики
                keyboard=KlavaMulti(lvl, 1)                                     # Inline клавиатура back -on
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)


        elif call.data == "back":
#            print ('xxxxxx-','Klava_Var', st, str(len(st)))    
            if (len(st) == 1) or  (st == '0'):
                    st = 'Ваша Комбинация:'
                    db.write_klava_variant(call.message.chat.id, '0')
                    keyboard=KlavaMulti(lvl, 0)                                 # Inline клавиатура back -off
                    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)
            else :
                    st = st[0:-1]
                    db.write_klava_variant(call.message.chat.id, st)            # запоминаем st в базу
                    st = SIntInShar(st)
                
                    keyboard=KlavaMulti(lvl, 1)                                 # Inline клавиатура back -on
                    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)



        elif call.data == "enter" :

            ans = db.otsenka (call.message.chat.id, st)
                            
#            print(ans)
#            print('======================================')
############            
            if ans == 'Victory !!!':
#                print('ПОБЕДА!')    
                ret = db.updbvictory(call.message.chat.id, int(time.mktime(call.message.date.timetuple())))

                

                st = SIntInShar(st)
                keyboard = types.InlineKeyboardMarkup()
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)
                
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*[types.KeyboardButton(name) for name in ['/new_game','/champs','/help']])

                q= ret[0]
                w= ret[1]
                okn = 'ов'
                if int(q[len(q)-1]) in [2,3,4]: okn = 'а'
                if int(q[len(q)-1]) in [1]: okn = ''
                okw = ''
                if int(w[len(w)-1]) in [2,3,4]: okw = 'ы'
                if int(w[len(w)-1]) in [1]: okw = 'у'



                
                await bot.send_message(call.message.chat.id, f'''Вы угадали комбинацию за {ret[0]} ход{okn}, затратив на это {ret[1]} секунд{okw}.
Мои поздравления!

🎮  /new_game - новая игра

🏆  /champs - таблица чемпионов

🙂  /my_game - мои лучшие игры

❓  /help - помощь

🔍  /about - о программе ''')
############                
            else:
                if ans == 'err01': ans = 'неверный ввод'
                elif ans == 'No': ans = 'Вы не угадали ни одного цвета.'
                else: ans = ResInShar(ans)    
            

                
                st = SIntInShar(st)                                                 # st в шарики    
                keyboard = types.InlineKeyboardMarkup()
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st, reply_markup=keyboard)

                ans=f'''{ans}
/Continue'''

                await bot.send_message(call.message.chat.id, ans)                   # отправляем оценку

   
             

if __name__ == "__main__": 
    db = SLdb.DB('ColorDB.db')
    executor.start_polling(dp)
        

