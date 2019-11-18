import json

#============Глобальні змінні
JSON_FILE_NAME = 'result.json'
DIALOG_NAME = 'Рожище'

def read_from_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    line = file.readlines()
    file.close()
    return line


def transfer_to_pair_list(list):
    for iterator in range(len(list)):
        start_index1 = list[iterator].find(')')
        end_index1 = list[iterator].find('-')
        key = list[iterator][start_index1 + 2:end_index1 - 1]
        value = list[iterator][end_index1 + 2:-1]  # Якщо правою гранню зріза встановити -1 то буде братися рядок без \n
        list[iterator] = [key, value]


def writing_to_file(file_name, lines):
    count = 1
    file = open(file_name, 'w', encoding='utf-8')
    for content in lines:
        file.write(str(count) + ') ' + content[0] + ' - ' + content[1] + '\n')
        count += 1
    file.close()


def search_coincidence(list):   #Функція пошуку співпадінь. ЇЇ ще треба доробити
    length = len(list)
    for i,j in enumerate(list):
        for x in range(i+1,length):
            if list[i][0]==list[x][0] or list[i][1]==list[x][1]:
                print('True')
                print(list[i][0],list[x][0])
                print('or')
                print(list[i][1], list[x][1])
        #print(list[i])
        #print(j)



lines = read_from_file('word_list.txt')        # Відкриваю файл зі списком попередніх слів
transfer_to_pair_list(lines)                   # Перетворюю їх в список типу [key:value] для подальшої роботи з ними
#===
word_list_from_JSON = []
file = open(JSON_FILE_NAME, 'r', encoding='utf-8') #Відкриваємо JSON файл щоб отримати з нього список повідомлень
content = json.load(file)
chats_list = content['chats']['list']        #Тут ми отримуємо список всіх чатів
for dialog in chats_list:                    #За допомогою циклу перебираємо список всіх чатів
    if dialog['name']==DIALOG_NAME:             #Якщо ключ 'name' = 'Назва потрібного чату', то продовжуємо працювати з потрібним діалогом
        message_list = dialog['messages']
        for message in message_list:
            if message['id']>=269:           #Передивившись файл вручну знайшов що мені потрібно зберегти всі повідомлення починаючи з 252-го
                text = '0) '+message['text']+'\n'   #Добавляю до строки спереду номер і в кінці перенос на новий рядок щоб використати готову,
                                                    # перевірену функцію 'transfer_to_pair_list()' з файлу Program_to_mention_English_word_console.py
                word_list_from_JSON.append(text)

transfer_to_pair_list(word_list_from_JSON)      #Перетворюю список строк в список типу [key:value] для подальшої роботи з ними
#----Тут має бути функція як перевіряє збіги
lines = lines+word_list_from_JSON               #Об'єдную дві змінні (попередні слова і нові слова)
search_coincidence(lines)
writing_to_file('rezult.txt',lines)             #Записую результат у файл

