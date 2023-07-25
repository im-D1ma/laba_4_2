import csv


game_type = dict() #запрос юзера
answer = list() #ответ по запросу
with open('steam.csv', mode='r', encoding = 'utf-8-sig') as file:
    for parameter in file.readline().rstrip('\n').split(','): 
        answer.append(parameter)
        game_type[parameter] = input(f'Input "{parameter}": ')
print('===========================')
print('Find:\n', game_type)
print('===========================')

w_flag = False
with open('steam.csv', mode='r', encoding = 'utf-8-sig', newline='') as src_csv_file:
    data_src = csv.DictReader(src_csv_file)
    for row in data_src:
        print(row)
        r_flag = True
        for parameter in game_type.keys():
            print(f'Searching "{game_type[parameter].lower()}" in /{parameter} : "{row[parameter].lower()}"/')
            if (game_type[parameter].lower() in row[parameter].lower()): 
                print('Match!')
            else:
                print(f'MISMATCH, going to next candidate!')
                r_flag = False
                break
        if r_flag:
            print(f'All games cheeked! Wrirting to "result.csv" => game: "{row[answer[1]]}"')
            with open('result.csv', mode='a', encoding = 'utf-8-sig', newline='') as trg_csv_file:
                writer = csv.DictWriter(trg_csv_file, fieldnames=answer)
                if not w_flag: 
                    writer.writeheader()
                writer.writerow(row)
                w_flag = True
        print('-------------------------')  
print('Result saved "result.csv"')
