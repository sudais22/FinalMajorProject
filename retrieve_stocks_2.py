import psycopg2 as p

def getStockData_2(id):
    connection = 0
    try:
        connection = p.connect(user="postgres",
                               password="postgres",
                               host="172.17.0.2",
                               port="5432",
                               database="postgres")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Connection established to: ", record,"\n")
    except (Exception, p.Error) as error:
        print("Error while connecting to PostgreSQL: ", error, "\n")
    finally:
        if(connection):
            result = 0
            print(id)
            if id == 3 or id == 4 or id == 6 or id == 7 or id == 8:
                result = "{\"info\": \"none\"}"
            else:
                print(id)
                if id == 1:
                    retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_3 order by day ASC) d ) as info) t "
                elif id == 2:
                    retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_5 order by day ASC) d ) as info) t "
                elif id == 5:
                    retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_9 order by day ASC) d ) as info) t "
                else:
                    retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_3 order by day ASC) d ) as info) t "
                cursor.execute(retrieveStocks)
                result = cursor.fetchall()
            return result
        else:
            return 0
        cursor.close()
        connection.close()
        print("Disconnected from postgreSQL")




