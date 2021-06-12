import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id integer PRIMARY KEY,part text,customer text,retailer text,price text)")
        pass
    
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self,part,customer,retailer,price):
        self.cur.execute("INSERT INTO parts VALUES (NULL,?,?,?,?)",(part,customer,retailer,price))
        self.conn.commit()
        
    def remove(self,id):
        self.cur.execute("DELETE FROM parts WHERE id=?",(id,))
        self.conn.commit()
        
    def update(self,id,part,customer,retailer,price):
        self.cur.execute("UPDATE parts SET part=?,customer=?,retailer=?,price=? WHERE id=?",(part,customer,retailer,price,id))
        self.conn.commit()
    
    def __del(self):
        self.conn.close()
    
#db = Database('store.db')
#db.insert("4GB DDR4 RAM","Azlan","Pasar","160")
#db.insert("8GB DDR4 RAM","Azlan","Pasar","260")
#db.insert("16GB DDR4 RAM","Azlan","Pasar","60")
#db.insert("27 inch Samsung Monitor","Azlan","Pasar","100")
#db.insert("600w Corsair PSU","Azlan","Pasar","1260")
#db.insert("NVidia matrox","Azlan","Pasar","360")
#db.insert("Asus Radeon","Azlan","Glory","460")
#db.insert("500w PSU","Azlan","Jannah Store","150")
#db.insert("Asus Mobo","Azlan","Everwin","120")
#db.insert("Logitech Mouse","Karen","Gafu","10")
    