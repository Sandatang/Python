from mysql.connector import connect
  
db_connection = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "database":"pythondb"
}

#region --Model Components--
class Query():
    def __init__(self, table_name, **kwargs):
        self.db = connect(**db_connection)
        self.table_name = table_name
        self.header_str = ', '.join(kwargs.keys())
        self.values = tuple(kwargs.values())
        if kwargs:
            self.values_update_specific = tuple(kwargs.values())[1:] + (tuple(kwargs.values())[0],)
            self.header_update_specific = tuple(kwargs.keys())[1:]

    def addQuery(self):
        db = self.db
        cursor = db.cursor()
        query = f"insert into {self.table_name} ({self.header_str}) values({','.join(['%s'] * len(self.values))})"
        cursor.execute(query, self.values)
        db.commit()
        self.closeDatabaseConnection(cursor,db)
        return "Student added successfully."
    
    def selectAllQuery(self):
        db = self.db
        cursor = db.cursor()
        cursor.execute(f"select * from {self.table_name}")
        data = cursor.fetchall()
        self.closeDatabaseConnection(cursor,db)
        return data

    def findQuery(self):
        db = self.db
        cursor = db.cursor()
        cursor.execute(f"select * from {self.table_name} where {self.header_str} = %s", self.values)
        data = cursor.fetchall()
        return data
    
    def deleteQuery(self):
        db = self.db
        cursor = db.cursor()
        query = f"delete from {self.table_name} where {self.header_str} = %s"
        cursor.execute(query, self.values)
        db.commit()
        affected = cursor.rowcount
        self.closeDatabaseConnection(cursor,db)
        return affected

    def updateQuery(self):
        db = self.db
        cursor = db.cursor()
        # return self.values_update_specific
        query = f"update {self.table_name} set {', '.join([f'{head} = %s' for head in self.header_update_specific])} where idno = %s"
        cursor.execute(query,self.values_update_specific)
        db.commit()
        affected = cursor.rowcount
        self.closeDatabaseConnection(cursor,db)
        return affected

    def closeDatabaseConnection(self, *args):
        args[0].close()
        args[1].close()
#endregion