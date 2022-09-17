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

    def UpdateLinkSettings(self, username, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth, buttonbackgroundhovercolor, namecolor, backgroundimage):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE linksettings SET backgroundcolor1='{backgroundcolor1}', backgroundcolor2='{backgroundcolor2}', bgradius='{bgradius}', buttonbackgroundcolor='{buttonbackgroundcolor}', buttontextcolor='{buttontextcolor}', buttonbordercolor='{buttonbordercolor}', buttonradius='{buttonradius}', buttonwidth='{buttonwidth}', buttonbackgroundhovercolor='{buttonbackgroundhovercolor}', namecolor='{namecolor}', backgroundimage='{backgroundimage}' WHERE owner='{username}'")
                connection.commit()

    def ResetDefaultLinkSettings(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE linksettings SET backgroundcolor1='#1095C1', backgroundcolor2='#10BBB3', bgradius='180', buttonbackgroundcolor='#1095C1', buttontextcolor='#FFFFFF', buttonbordercolor='#FFFFFF', buttonradius='10', buttonwidth='40', buttonbackgroundhovercolor='#15E5E9', namecolor='#dedede', backgroundimage='' WHERE owner='{username}'")
                connection.commit()

    def SetDefaultLinkSettings(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO linksettings (owner, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth, buttonbackgroundhovercolor) VALUES ('{username}', '#1095C1', '#10BBB3', '180', '#1095C1', '#FFFFFF', '#FFFFFF', '10', '40', '#000000')")
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

    def GetAllLinksByUsername(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM links WHERE owner='{username}'")
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

    def CreateLink(self, owner, link, icon, nsfw, publish, label):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f'INSERT INTO `links` (owner, link, icon, nsfw, publish, label) VALUES ("{owner}", "{link}", "{icon}", "{nsfw}", "{publish}", "{label}")')
                connection.commit()

    def DeleteLink(self, id):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f'DELETE FROM links WHERE id={id}')
                connection.commit()

    def UpdateLink(self, id, label, link, icon, nsfw, publish, highlight, effect, highlightname, effectname):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f'UPDATE links SET label="{label}", link="{link}", icon="{icon}", nsfw="{nsfw}", publish="{publish}", highlight="{highlight}", effect="{effect}", highlightname="{highlightname}", effectname="{effectname}" WHERE id={id}')
                connection.commit()

    def GetOptions(self, type):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM options WHERE type='{type}'")
                result = cursor.fetchall()
                connection.commit()
            return result