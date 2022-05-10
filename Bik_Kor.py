from aiogram import types, Bot 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import SLdb, random
from config import ABORT, CHANCHLEV, MUADD, STR1, TOKEN, ABOUT, QIWI_PAB_KEY
from keyboards import *
import datetime, time

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
            await bot.send_message(message.chat.id, ABORT, reply_markup=keyboard)
        
        elif message.text == '/new_game':
            db.updbplayer(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, message.chat.title, message.from_user.language_code)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['level_1','level_2','level_3']])
            await bot.send_message(message.chat.id, CHANCHLEV , reply_markup=keyboard) 
            ans = ''


        elif message.text in ['level_1','level_2','level_3']:
               
                if message.text == 'level_1': 
                    lvl=1
                    col = 'пяти'
                if message.text == 'level_2':
                    lvl=2
                    col = 'шести'
                if message.text == 'level_3':
                    lvl=3
                    col = 'семи'
                db.new_game (message.chat.id, int(time.mktime(message.date.timetuple())),lvl)
                keyboard = types.ReplyKeyboardRemove(selective=False)           # убиваем клаву Reply
                await bot.send_message(message.chat.id, f'Комбинация из {col} цифр успешно загадана.', reply_markup=keyboard)
#                print(str(lvl))

        elif message.text == '/new_game':
            lvl=1
            db.updbplayer(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, message.chat.title, message.from_user.language_code)
            db.new_game (message.chat.id, int(time.mktime(message.date.timetuple())),lvl)
            keyboard = types.ReplyKeyboardRemove(selective=False)           # убиваем клаву Reply
            await bot.send_message(message.chat.id, 'Комбинация успешно загадана', reply_markup=keyboard)
            
            
        elif message.text == '/start':
            ans = '''Игра "Быки и Коровы" приветствует вас!

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
               


        elif db.pole_from_b('game', 'Now_Game' , message.chat.id)=='1' :
                
            lv = int(db.pole_from_b('game', 'Level' , message.chat.id))    

            mt = SharInSInt (message.text)
            ans = db.otsenka (message.chat.id, mt)                            
            
    #                    print(ans)
    #                    print('======================================')

            if ans == 'Victory !!!':
               # print('ПОБЕДА!')    
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
 
{MUADD}''', reply_markup=keyboard)
            else:
                if ans == 'err01': ans = 'неверный ввод'
                elif ans == 'No': ans = 'Вы не угадали ни одной цифры.'
                else: ans = ResInShar(ans)    
                await bot.send_message(message.chat.id, ans)


           

if __name__ == "__main__": 
    db = SLdb.DB('bikkor.db')
    executor.start_polling(dp)
        

