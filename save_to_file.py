import abc
import pandas as pd
import json


class SaveToFile(abc.ABC):
    def __init__(self, name, number):
        self.name = name
        self.number = number
    @abc.abstractmethod
    def save_to_file(self):
        pass
class SaveToExcel(SaveToFile):
    def save_to_file(self):
        df = pd.DataFrame({'name': [self.name], 'number': [self.number]})
        df.to_excel('data.xlsx')
class SaveToCsv(SaveToFile):
    def save_to_file(self):
        df = pd.DataFrame({'name': [self.name], 'number': [self.number]})
        df.to_csv('data.csv')
class SaveToTxt(SaveToFile):
    def save_to_file(self):
        with open("data.txt", 'w') as file:
            file.write(f'name: {self.name}\nnumber: {self.number}')
class SaveToJson(SaveToFile):
    def save_to_file(self):
        data = {'name': self.name, 'number': self.number}
        with open("data.json", 'w') as file:
            json.dump(data, file, indent=4)
ivan1 = SaveToExcel('Ivan', '89234629828')
ivan2 = SaveToCsv('Ivan', '89234629828')
ivan3 = SaveToTxt('Ivan', '89234629828')
ivan4 = SaveToJson('Ivan', '89234629828')
for ivan in (ivan1, ivan2, ivan3, ivan4):
    ivan.save_to_file()
