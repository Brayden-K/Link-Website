import pymysql.cursors

class MySQL:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def query(self, query, querytype='select', fetchall=True):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if querytype == 'select':
                    if fetchall == True:
                        result = cursor.fetchall()
                    else:
                        result = cursor.fetchone()
                    return result
            connection.commit()

    def CheckRegistered(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
                result = cursor.fetchone()
                connection.commit()
            if result == None:
                return False
            else:
                return result

    def Register(self, username, email, twitchid, profile_image_url, broadcaster_type, twitch_created_at, created_at):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO users (username, email, twitchid, profile_image_url, broadcaster_type, twitch_created_at, created_at) VALUES ('{username}', '{email}', '{twitchid}', '{profile_image_url}', '{broadcaster_type}', '{twitch_created_at}', '{created_at}')")
                result = cursor.fetchone()
                connection.commit()

    def GetUserByUsername(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
                result = cursor.fetchone()
                connection.commit()
            return result

    def UpdateAccount(self, username, highlight):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE users SET highlight='{highlight}' WHERE username='{username}'")
                result = cursor.fetchone()
                connection.commit()

    def UpdateLinkSettings(self, username, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE linksettings SET backgroundcolor1='{backgroundcolor1}', backgroundcolor2='{backgroundcolor2}', bgradius='{bgradius}', buttonbackgroundcolor='{buttonbackgroundcolor}', buttontextcolor='{buttontextcolor}', buttonbordercolor='{buttonbordercolor}', buttonradius='{buttonradius}', buttonwidth='{buttonwidth}' WHERE owner='{username}'")
                connection.commit()

    def SetDefaultLinkSettings(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO linksettings (owner, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth) VALUES ('{username}', '#1095C1', '#10BBB3', '180', '#1095C1', '#FFFFFF', '#FFFFFF', '10', '40')")
                connection.commit()
        return self.GetLinkSettings(username)

    def GetLinksByUsername(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM links WHERE owner='{username}' AND publish='True'")
                result = cursor.fetchall()
                connection.commit()
            return result

    def GetLinkSettings(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM linksettings WHERE owner='{username}'")
                result = cursor.fetchone()
                connection.commit()
            return result