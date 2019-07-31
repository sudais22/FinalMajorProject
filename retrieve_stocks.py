import psycopg2 as p

def getStockData(id):
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
            if id == 1:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_2 order by day ASC) d ) as info) t "
            elif id == 2:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_4 order by day ASC) d ) as info) t "
            elif id == 3:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_6 order by day ASC) d ) as info) t "
            elif id == 4:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_7 order by day ASC) d ) as info) t "
            elif id == 5:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_8 order by day ASC) d ) as info) t "
            elif id == 6:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_10 order by day ASC) d ) as info) t "
            elif id == 7:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_11 order by day ASC) d ) as info) t "
            elif id == 8:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_12 order by day ASC) d ) as info) t "
            else:
                retrieveStocks = "select row_to_json(t) from ( select (select array_to_json(array_agg(row_to_json(d))) from (select day, closing_price, volume from stocktrade_2 order by day ASC) d ) as info) t "
            cursor.execute(retrieveStocks)
            result = cursor.fetchall()
            return result
        else:
            return 0
        cursor.close()
        connection.close()
        print("Disconnected from postgreSQL")
