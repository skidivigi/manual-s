import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successful connect")

    try:
        cursor = connection.cursor()

        # #Create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `games`(id int AUTO_INCREMENT," \
        #                          " name varchar(32), password varchar(32)," \
        #                          " email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")
        #
        # #insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (name, password, email) VALUES ('Kevin', 'qwerty', '@mail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (name, password, email) VALUES ('Lony', '123456', '@mail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (name, password, email) VALUES ('Yany', '123456', '@mail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # #update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `games` SET password = 'xxxXXX' WHERE name = 'Oleg';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `games` WHERE id = 2;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # #delete(drop) table
        # with connection.cursor() as cursor:
        #     delete_table_full = "DROP TABLE `games`;"
        #     cursor.execute(delete_table_full)

        # select all data from table
        # with connection.cursor() as cursor:
        #     all_rows = "SELECT * FROM `games`"
        #     cursor.execute(all_rows)
        #     # cursor.execute("SELECT * FROM `games`")
        #     rows = cursor.fetchall()
        #     for each in rows:
        #         print(each)
        #     print('yep yep')

    finally:
        connection.close()

except Exception as ex:
    print("Not connect")
    print(ex)
