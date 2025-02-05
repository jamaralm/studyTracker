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
    print('Sucesfully registered the study time! =D')

def showTimeStudied():
    data = loadData(filePath)
    if not data:
        print('YOU DONT HAVE ANY TIME STUDIED :(')

    print('STUDY TRACKER:')
    for record in data:
        print(f"DATE: {record['date']} | TIME STUDIED: {record['hours']}h:{record['minutes']}m")

# MAIN CODE

def main():
    while True:
        print("1. ADD STUDY TIME")
        print("2. SHOW STUDY TIME")
        print("3. LEAVE :(")
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
            showTimeStudied()
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()