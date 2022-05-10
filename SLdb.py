
import sqlite3
import random

class C_Game:
      Fishki = []
      Level = 1
      

      def __init__ (self, Level):
            self.Level = Level
      

      def set (self):
            #print(f'level = {self.Level}')
            k =  4 + self.Level
            Digt = [0,1,2,3,4,5,6,7,8,9]
            self.Fishki = random.sample(Digt, k)
            return self.Fishki 

class gamers:
      name = 'Vasya'

      def __init__(self):
           pass




def proverka (variant, otvet):

      rez = []
      
      for i in range(len(otvet)):
            if variant[i] == otvet[i]:
                  rez.append(2)
                  otvet.pop(i)
                  otvet.insert(0, "x")
                  variant.pop(i)
                  variant.insert(0, "x")
      
                  #print (otvet, variant)

      for i in range(len(otvet)):
            
            if (variant[i] in otvet) and (variant[i] != "x"):
                  rez.append(1)
                  otvet.remove(variant[i])
                  otvet.insert(0, "x")
                  variant.pop(i)
                  variant.insert(0, "x")
                 # print ('-',  variant, otvet)
      return rez


def strlist (otvet):

      otv = []
      

      for i in range(len(otvet)):
            otv.append(int(otvet[i]))

      return (otv)


def provres (res, lvl):
      lvl=lvl+4
     # print (res.count(2), lvl )
      if res.count(2) == lvl :
            return True
      else:
            return False
      


class DB:
    def __init__(self, db_file):
        self.db_file = db_file
    

    
    def con(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self.conn, self.cursor         


    def view_my_game(self, Id: int):

        sqconn , mycursor = self.con()

        z='       Ваши лучшие игры :\n\n'
        mst = 1
        sql = f'select  Game_L, Nim_N, G_T from yourgames WHERE Id = {Id} Limit 10'
        
        mycursor.execute(sql)
        myresult = mycursor.fetchall()


        if myresult != []:
            for x in myresult:
                okn = 'ов'
                if int(x[2]) in [2,3,4]: okn = 'а'
                if int(x[2]) in [1]: okn = ''
                mins=x[2]//60
                secc=x[2]%60
                mesto = str(mst)
                z=z+mesto+' уровень-'+str(x[0])+' за '+str(x[1])+f' ход{okn} - '+ str(mins)+'мин. '+str(secc)+'с.\n\n'
                mst+=1            
        else: z='No'

        mycursor.close()
        sqconn.close()

        return z


    def read_klava_variant(self, Id: int):
        sqconn , mycursor = self.con()

        sql = "SELECT Klava_Var FROM klava WHERE id = "+str(Id)
    
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult != []: 
            for x in myresult: z=x[0]
        else: z='No'

        mycursor.close()
        sqconn.close()
        return str(z)  


    # def write_klava_variant(self, Id: int, Klava_Var: str):
    #     ids = str(Id)
    #     KV = Klava_Var
    #     sqconn , mycursor = self.con()

    #     if self.read_klava_variant(Id) == 'No':
    #         sql = f"INSERT INTO klava (id, Klava_Var) VALUES ({ids}, {KV})"

    #         mycursor.execute(sql)
    #         sqconn.commit()

    #     else:

    #         sql = f"UPDATE klava SET Klava_Var = {KV} WHERE id = {ids}" 
            
        
    #         mycursor.execute(sql)
    #         sqconn.commit()

    #     mycursor.close()
    #     sqconn.close()

    def pole_from_b (self, base:str, pole:str , gde:str):

        sqconn , mycursor = self.con()

        sql = f"SELECT {pole} FROM {base} WHERE ChatId = {gde}"
        
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult != []: 
            for x in myresult: z=x[0]
        else: z='XPEH'
        
        mycursor.close()
        sqconn.close()
        return str(z) 



    def pole_from_b1 (self, base:str, pole:str ,pgde:str, gde:str):
        
        sqconn , mycursor = self.con()
        try:
            sql = f"SELECT {pole} FROM {base} WHERE {pgde} = {gde}"
        
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if myresult != []: 
                for x in myresult: z=x[0]
            else: z='XPEH'
        except:
            z = 'errSQL'

        mycursor.close()
        sqconn.close()    
        return str(z)


    
    def new_game (self, chatid: int, data:int, level: int):
        
        mydb , mycursor = self.con()
        
        gam = C_Game(level)
        gam.set()
                
        ids = str(chatid)
        dats = str(data)
        les = str(level)

                
        sql = f"INSERT INTO games (Gamer_ID, Start_Date_Time, Game_Level) VALUES ({ids}, {dats}, {les})"
        #print(sql)
        mycursor.execute(sql)
        mydb.commit()
        Id = mycursor.lastrowid
        
        Ids = str(Id)
        N='1'

        Varik=''
        for i in gam.Fishki: Varik += str(i)
      
        ##################
      
                
        if self.pole_from_b ('game', 'Now_Game', str(chatid)) == 'XPEH':
        
            sql = f"INSERT INTO game (id, ChatId, Now_Game, Variant, Level, hod) VALUES ({Ids}, {ids}, {N}, '{Varik}', {les}, 0)"
            mycursor.execute(sql)
            mydb.commit()
            
            
        else:
            sql = f"UPDATE game SET id = {Ids}, Now_Game = {N}, Variant = '{Varik}', Level = {les}, hod = 0  WHERE ChatId = {ids}"  
            mycursor.execute(sql)
            mydb.commit()


        mycursor.close()
        mydb.close()


            
        
    def updbvictory(self, chatid: int, data:int):     

        mydb , mycursor = self.con()

        ids = str(chatid)
        das = str(data)

        Ids = self.pole_from_b ('game', 'id' , ids)
        
        z = self.pole_from_b1 ('games', 'Start_Date_Time' ,'Game_Id', Ids)
        
        hod = self.pole_from_b ('game', 'hod' , ids)

        
        sql = f"UPDATE game SET Now_Game = 0, hod = 0  WHERE ChatId = {ids}" 
            
    
        mycursor.execute(sql)
        mydb.commit()

        GTS=str(data-int(z))  
        
        sql = f"UPDATE games SET End_Data_Time = {das}, Game_Time = {GTS}, Nimber_Hod = {hod} WHERE Game_Id = {Ids}"
    
        mycursor.execute(sql)
        mydb.commit()

        ret = [hod, GTS]

        mycursor.close()
        mydb.close()

        return ret
            


    def updbplayer(self, chatid: int, Name:str, f_name:str, l_name:str, tit:str, lng_code:str ):

        mydb , mycursor = self.con()
        ids = str(chatid)
        pn = self.pole_from_b1 ('player', 'Player_Id' ,'Player_Id', ids)
        if pn == 'XPEH' :
            sql = f'INSERT INTO player (Player_Id, Player_Name, first_name, last_name, title, language_code ) \
    VALUES ({ids}, "{Name}", "{f_name}", "{l_name}", "{tit}", "{lng_code}")'
        else:
            sql = f'UPDATE player SET Player_Name = "{Name}", \
    first_name = "{f_name}", \
    last_name = "{l_name}", \
    title = "{tit}", \
    language_code = "{lng_code}" \
    WHERE Player_Id = {ids}' 
        #print(sql)    
    
        mycursor.execute(sql)
        mydb.commit()

        mycursor.close()
        mydb.close()

        


    def updatehod(self, chatid: int):
        mydb , mycursor = self.con()

        z = self.pole_from_b ('game', 'hod' , str(chatid))
        k = int(z)+1
        hod = str(k)
        ids = str(chatid)
        
        sql = f"UPDATE game SET hod = {hod} WHERE ChatId = {ids}" 
            
    
        mycursor.execute(sql)
        mydb.commit()

        mycursor.close()
        mydb.close()


    def otsenka (self, chatid: int, inp: str):
        mydb , mycursor = self.con()
        Vk=''
        implist = strlist (inp)
        
        sql = "SELECT Variant, Level FROM game WHERE ChatId = "+str(chatid)
    
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            z = x[0]
            lvl = x[1]
        
        if len(inp)==len(z):
            tempA = list (strlist (z))
            tempB = list (implist)
            #print (tempB, tempA)
            res = proverka (tempB, tempA)
            if res == []: Vk = 'No'
            else:
                if provres(res, lvl):
                    res = 'Victory !!!'
                for i in res:
                    Vk += str(i)    
            self.updatehod(chatid)     
        else: Vk ='err01'
        
        mycursor.close()
        mydb.close()
        return Vk


    def seechamp(self):   
        mydb , mycursor = self.con()
        sql = "SELECT * FROM champs"
    
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult 
        


if __name__=="__main__" :
     ww = C_Game(1)
     w2 = C_Game(2)
     w3 = C_Game(3)

     for i in range(5): print(ww.set())
     for i in range(5): print(w2.set())
     for i in range(5): print(w3.set())