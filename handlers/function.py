from misc import cursor,conn


def new_payment(telegram_id, comment, payment_sum):
    cursor.execute(f'UPDATE users SET comment = ? WHERE telegram_id = ?;', (comment, telegram_id))
    cursor.execute(f'UPDATE users SET payment_sum = ? WHERE telegram_id = ?;', (payment_sum, telegram_id))
    conn.commit()


def new_user(telegram_id):
    query = f"""SELECT * from users WHERE telegram_id={telegram_id}"""
    cursor.execute(query)
    check = cursor.fetchall()
    if check:
        pass
    else:
        cursor.execute("""INSERT INTO users
                    VALUES (?,?,?,?,?,?,?)""", (telegram_id, "1", 1000, 0, 0, telegram_id, 1)
                       )
        conn.commit()
        return 'new user'


def add_sub(telegram_id):
    cursor.execute(f'UPDATE users SET sub = ? WHERE telegram_id = ?;', (1, telegram_id))
    conn.commit()


def check_sub(telegram_id):
    for row in cursor.execute("SELECT telegram_id , sub FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            sub = row[1]
            return sub


def add_promo(telegram_id, promo):
    for row in cursor.execute("SELECT telegram_id,promo,referal_code FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            user_promo = row[1]
            referal_code = row[2]
            if int(user_promo) == 1 and int(referal_code) != int(user_promo):
                cursor.execute(f'UPDATE users SET promo = ? WHERE telegram_id = ?;', (promo, telegram_id))
                conn.commit()


def get_referals(telegram_id, promo):
    referals = 0
    for row in cursor.execute("SELECT telegram_id,promo FROM users"):
        ref_promo = row[1]
        if ref_promo == promo:
            referals += 1
    if referals != None:
        return referals
    elif referals == None:
        return 0


def get_balance(telegram_id):
    for row in cursor.execute("SELECT telegram_id,balance FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            balance = row[1]
            return balance


def checkbalance(telegram_id):
    for row in cursor.execute("SELECT telegram_id,balance FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            balance = row[1]
            if balance >= 1000:
                balance = int(balance - 1000)
                cursor.execute(f'UPDATE users SET balance = ? WHERE telegram_id = ?;', (balance, telegram_id))
                cursor.execute(f'UPDATE users SET sub = ? WHERE telegram_id = ?;', (1, telegram_id))
                conn.commit()
                return True
            elif balance < 1000:
                return False


def referal_pay(telegram_id):
    """
    Система которая добавляет 10%
    человеку процент от реферальный системы
    """
    for row in cursor.execute("SELECT telegram_id,promo FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            promo = row[1]
            if promo != 1:
                ref_balance = amount / 10
                cursor.execute(f'UPDATE users SET balance = ? WHERE telegram_id = ?;', (ref_balance, promo))
                conn.commit()
                return promo


def get_comment(telegram_id):
    for row in cursor.execute("SELECT telegram_id,comment FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            comment = row[1]
            return comment


def edit_balance(telegram_id):
    cursor.execute(f'UPDATE users SET balance = ? WHERE telegram_id = ?;', (0, telegram_id))
    conn.commit()