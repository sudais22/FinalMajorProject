import psycopg2 as p

def authenticateUser(email, password):
    connection = 0
    try:
        connection = p.connect(user="postgres",
                               password="postgres",
                               host="172.17.0.2",
                               port = "5432",
                               database="postgres")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Connection established to: ", record,"\n")
    except (Exception, p.Error) as error:
        print("Error while connecting to PostgreSQL: ", error, "\n")
    finally:
        if(connection):
            checkEmail = "SELECT exists(SELECT * FROM login WHERE email='%s')" % (email)
            cursor.execute(checkEmail)
            result = cursor.fetchone()
            if result[0] is True:
                checkPassword = "SELECT * FROM login WHERE email='%s'" % (email)
                cursor.execute(checkPassword)
                result = cursor.fetchone()
                print(result)
                print(result[0])
                print(result[1])
                print(result[2])
                if result[2] == password:
                    return result[0]
                else:
                    return -1
            else:
                return -1
            cursor.close()
            connection.close()
            print("Disconnected from postgreSQL")
