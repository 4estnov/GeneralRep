import telebot
TOKEN = '5085685205:AAHTVwNAEmx2f2WcAT9gtfXhhX09skeTNgk'
def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            telinput = m.text
            def base():
                import sqlite3
                while True:
                    connection = sqlite3.connect('telbase.db')
                    cursor = connection.cursor()
                    cursor.execute('SELECT surname FROM telbase')
                    surname_colum = cursor.fetchall()
                    surname_list = [item[0] for item in surname_colum]
                    incoming_surname = telinput
                    if incoming_surname in surname_list:
                        cursor.execute("SELECT name, surname, subdivision, tel FROM telbase WHERE surname like '%'||?||'%'", (incoming_surname,))
                        array = cursor.fetchall()
                        outbase = ''
                        for name, surname, subdivision, tel in array:
                            outbase += f"\n{name} {surname} {subdivision} {tel}"
                        return outbase
                        connection.commit()
                        connection.close()
                    else:
                        return 'Введите фамилию с большой буквы'
        output = base()
        tb.send_message(chatid, output)
tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener)
tb.polling()
tb.polling(none_stop=True)
tb.polling(interval=3)
while True:
    pass

