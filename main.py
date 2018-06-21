import sqlite3
'''
CREATE define, DROP borra,
'''

try:
    connection = sqlite3.connect("Company.db")

    cursor = connection.cursor()

    sql_command = """
    CREATE TABLE IF NOT EXISTS office(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20)
    );"""
    cursor.execute(sql_command)

    sql_command = """
    INSERT INTO office(
        id,
        name
    ) VALUES(
        NULL,
        "MKT"
    );
    """

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        lastname VARCHAR(30),
        gender CHAR(1),
        birth_date DATE,
        officeId INTEGER,
        FOREIGN KEY (officeId) REFERENCES office(id)
    );"""

    cursor.execute(sql_command)


    sql_command = """
    INSERT INTO employee (
        id,
        name,
        lastname,
        gender,
        birth_date,
        officeid
    ) VALUES(
            NULL,
            "PANCHO",
            "VILLA",
            "H",
            "1999-05-21",
            2
        );"""
    cursor.execute(sql_command)
    cursor.execute("SELECT * FROM employee")

    result = cursor.fetchall()
    print(result)

    connection.commit()
    connection.close()

except Exception as identifier :
        print("Something get wrong")
        print(identifier)