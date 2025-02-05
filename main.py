import json
from datetime import datetime

filePath = './studyTime.json'

# CREATING FUNCTIONALITIES

def loadData(filePath):
    try:
        with open(filePath, 'r') as file: 
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def saveData(data):
    try:
        with open(filePath, 'w') as file:
            json.dump(data, file, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def addStudyTime(date, hours, minutes):
    data = loadData(filePath)

    data.append({'date': date, 'hours': hours, 'minutes': minutes})
    saveData(data)
    print('Sucesfully registered the study time!!g =D')

def showRecords():
    data = loadData(filePath)
    if not data:
        print('YOU DONT HAVE ANY TIME STUDIED :(')

    print('##########################################')
    print('STUDY TRACKER:')
    for index, record in enumerate(data):
        print(f"{index + 1}. DATE: {record['date']} | TIME STUDIED: {record['hours']}h:{record['minutes']}m")

def editRecord():
    data = loadData(filePath)
    if not data:
        return

    try:
        index = int(input("TYPE THE NUMBER OF RECORD YOU WANT TO EDIT: ")) - 1
        if 0 <= index < len(data):
            new_hours = int(input("TYPE THE NEW AMOUNT OF HOURS STUDIED: "))
            new_minutes = int(input("TYPE THE NEW AMOUNT OF MINUTES STUDIED: "))
            data[index]["hours"] = new_hours
            data[index]['minutes'] = new_minutes
            saveData(data)
            print("Registro editado com sucesso!\n")
        else:
            print("Índice inválido!\n")
    except ValueError:
        print("Entrada inválida!\n")

def removeRecord():
    data = loadData()
    showRecords()
    if not data:
        return
    try:
        index = int(input("Digite o número do registro que deseja remover: ")) - 1
        if 0 <= index < len(data):
            del data[index]
            saveData(data)
            print("Registro removido com sucesso!\n")
        else:
            print("Índice inválido!\n")
    except ValueError:
        print("Entrada inválida!\n")

# MAIN CODE

def main():
    while True:
        print('##########################################')
        print("1. ADD STUDY TIME")
        print("2. SHOW STUDY TIME")
        print("3. EDIT RECORD")
        print("4. REMOVE RECORD")
        print("5. LEAVE :(")
        print('##########################################')
        choice = input("CHOOSE A OPTION: ")
        
        if choice == "1":
            date = input("TYPE THE DATE (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")  # Valida a data
                hours = int(input("TYPE THE AMOUNT OF HOURS: "))
                minutes = int(input('TYPE THE AMOUNT OF MINUTES: '))
                addStudyTime(date, hours, minutes)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar a data e as horas corretamente.\n")
        elif choice == "2":
            showRecords()
        elif choice == "3":
            editRecord()
        elif choice == "4":
            removeRecord()
        elif choice == '5':
            print('LEAVING... =(')
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()