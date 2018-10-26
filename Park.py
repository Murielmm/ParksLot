# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import io
import json
import math


def myFunc(e):
    return e['ParkSpace']['Id']


class park:

    def getParkData(self):
        with io.open('ParkData.json', 'r', encoding='utf8') as json_file:
            return json.load(json_file)

    def truncateData(self, park_data):
        park_data['Park'].sort(key=myFunc)
        with io.open('ParkData.json', 'w', encoding='utf8') as json_file:
            json.dump(park_data, json_file, ensure_ascii=False)
            json_file.close()

    def getParkCapacity(self, park_data):
        sum_value = 0

        for park_line in park_data['Park']:
            if park_line['ParkSpace']['VehicleType'] == 'M':
                value = 0.5
            else:
                value = 1

            value = len(park_line['ParkSpace']['Vehicles']) * value
            sum_value += value

        return sum_value

    def validParkCapacity(self, vehicle_type):
        park_data = self.getParkData()
        sum_value = self.getParkCapacity(park_data)

        dif_value = park_data['MaxParking'] - sum_value

        if (sum_value == park_data['MaxParking']) or (vehicle_type == 'M' and dif_value < 0.5) or \
           (vehicle_type == 'A' and dif_value < 1):
            print('\nERRO! Estacionamento cheio!')
            return False

        return True

    def addNewSpace(self, park_data, vehicle):
        park_space = {'ParkSpace': {
            "Id": self.getNewSpaceId(park_data),
            "VehicleType": vehicle['Type'],
            "Vehicles": []
        }}

        self.addNewVehicle(park_space, vehicle)

        park_data['Park'].append(park_space)

    def addNewVehicle(self, park_space, vehicle):
        park_space['ParkSpace']['Vehicles'].append({
            "Plate": vehicle['Plate'],
            "Cpf": vehicle['Cpf'],
            "Name": vehicle['Name'],
            "Phone": vehicle['Phone'],
            "Time": vehicle['Time']
        })

    def getNewSpaceId(self, park_data):
        id_spaces = []
        id_space = 0
        id_aux = 0

        for park_line in park_data['Park']:
            id_spaces.append(park_line['ParkSpace']['Id'])

        while id_space == 0:
            id_aux += 1
            if id_spaces.count(id_aux) == 0:
                id_space = id_aux

        return id_space

    def calculateValueToPay(self, vehicle_type, entrance_hour):
        value = 2.00
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        now = str(datetime.now())
        diff = datetime.strptime(now, fmt) - datetime.strptime(entrance_hour, fmt)

        if diff.days > 0 or diff.seconds > 3600:
            diff = diff - timedelta(hours=1)
            seconds = diff.seconds

            for _ in range(diff.days):
                seconds += 86400

            hours = math.ceil((seconds / 60) / 60)

            if vehicle_type == 'A':
                value += hours * 2.50

            elif vehicle_type == 'M':
                value += hours * 1.50

        print("\nSaldo devedor:", 'R${:,.2f}'.format(value))

    def checkOut(self, plate):
        data_removed = False
        park_data = self.getParkData()

        for park_line in park_data['Park']:
            for vehicle in park_line['ParkSpace']['Vehicles']:
                if vehicle['Plate'] == plate:
                    data_removed = True
                    self.calculateValueToPay(park_line['ParkSpace']['VehicleType'], vehicle['Time'])
                    park_line['ParkSpace']['Vehicles'].remove(vehicle)
                    break

            if len(park_line['ParkSpace']['Vehicles']) == 0:
                park_data['Park'].remove(park_line)

        if data_removed is True:
            self.truncateData(park_data)
            print("\nSUCESSO!")
        else:
            print("\nERRO! Placa não encontrada!")

    def checkIn(self, vehicle):
        new_space = True
        park_data = self.getParkData()

        if vehicle['Type'] == 'M':
            for park_line in park_data['Park']:
                if park_line['ParkSpace']['VehicleType'] == 'M' and len(park_line['ParkSpace']['Vehicles']) == 1:
                    new_space = False
                    self.addNewVehicle(park_line, vehicle)
                    break

        if new_space is True:
            self.addNewSpace(park_data, vehicle)

        self.truncateData(park_data)
        print("\nSUCESSO!")

    def listAllSpaces(self):
        park_data = self.getParkData()

        for park_line in park_data['Park']:
            print('\nVaga', park_line['ParkSpace']['Id'])
            print('Tipo Veículo(s) na vaga:', 'Motocicleta' if park_line['ParkSpace']['VehicleType'] == 'M' else 'Automóvel')

            for vehicle in park_line['ParkSpace']['Vehicles']:
                print('Placa:', vehicle['Plate'], '| CPF:', vehicle['Cpf'], '| Nome:', vehicle['Name'],
                      '| Telefone:', vehicle['Phone'], '| Hora Entrada:', vehicle['Time'][0:5])
        print("\n")
