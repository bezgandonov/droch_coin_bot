import sqlite3 as sq

def create_db():
    con = sq.connect('drochcoin.db')
    cur = con.cursor()

    command = '''
        CREATE TABLE IF NOT EXISTS wallets (
        user_id INT,
        balance INT
        )'''
    cur.execute(command)

    con.commit()
    con.close()


def add_user(user_id):
    con = sq.connect('drochcoin.db')
    cur = con.cursor()

    command = f'INSERT INTO wallets (user_id, balance) VALUES ({user_id}, 0)'
    cur.execute(command)

    con.commit()
    con.close()


def manipulate_wallet(user_id, count, add_or_nah):
    con = sq.connect('drochcoin.db')
    cur = con.cursor()

    command = f'SELECT balance FROM wallets WHERE user_id={user_id}'
    cur.execute(command)

    balance = cur.fetchone()

    if balance == None: 
        add_user(user_id)
        balance = (0, )

    if add_or_nah:
        new_balance = balance[0] + int(count)
    else:
        new_balance = balance[0] - int(count)

    command = f'UPDATE wallets SET balance = {new_balance} WHERE user_id = {user_id}'
    cur.execute(command)

    con.commit()
    con.close()
