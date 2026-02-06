from collections import namedtuple


air_1 = ('Airbus', 'A320', 180, 2021, 'ER5533')
air_2 = ('Boeing', '737', 160, 2019, 'BA1234')
air_3 = ('Embraer', 'E195', 120, 2020, 'EM5678')
air_4 = ('Cessna', '172', 4, 2018, 'CE9101')

airplanes = [air_1, air_2, air_3, air_4]

for airplane in airplanes:
    if airplane[3] > 150:
        print(f"{airplane[0]} {airplane[-1]} can carry more than 150 passengers.")

print("-" * 50)

Airplane = namedtuple('Airplane', ['fabric', 'model', 'capacity', 'year', 'registration'])
airplane_1 = Airplane('Airbus', 'A320', 180, 2021, 'ER5533')
airplane_2 = Airplane('Boeing', '737', 160, 2019, 'BA1234')
airplane_3 = Airplane('Embraer', 'E195', 120, 2020, 'EM5678')
airplane_4 = Airplane('Cessna', '172', 4, 2018, 'CE9101')

airplanes_2 = [airplane_1, airplane_2, airplane_3, airplane_4]

for airplane in airplanes_2:
    if airplane.capacity > 150:
        print(f"{airplane.fabric} {airplane.registration} can carry more than 150 passengers.")
