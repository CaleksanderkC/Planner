import csv
import datetime

class Model:
    '''
        Class Model odpowiada za dane o wydarzeniach,
        ich przechowywanie  i odczyt/zapis z pliku csv
    '''
    def __init__(self):
        self.file_name = 'wydarzenia.csv'
        self.event_data = []
        self.read()

    def check_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return False
        return True

    def check_time(self, time):
        try:
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            return False
        return True

    def check_name(self, name):
        return name != ''

    def add(self, date, time, name, desc):

        self.event_data.append({
            'date': date,
            'time': time,
            'name': name,
            'desc': desc,
        })

        with open(self.file_name, 'a', newline='') as csv_file:
            try:
                csv.writer(csv_file).writerow((date, time, name, desc))
            except:
                pass

    def save(self):
        with open(self.file_name, 'w', newline='') as csv_file:
            for event in self.event_data:
                try:
                    csv.writer(csv_file).writerow((event['date'], event['time'], event['name'], event['desc']))
                except:
                    pass

    def read(self):
        try:
            with open(self.file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    self.event_data.append({
                        'date': row[0],
                        'time': row[1],
                        'name': row[2],
                        'desc': row[3],
                    })
        except:
            pass

    def delete(self, _id):
        if _id >= 0:
            self.event_data.pop(_id)
            self.save()

    def data(self):
        return self.event_data
