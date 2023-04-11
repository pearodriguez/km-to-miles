kilometers = float(input('Enter kilometers to convert: '))

def km_to_miles (kilometers):
    miles = kilometers * 0.6214
    print(kilometers, 'kilometers is converted to approximately', round(miles, 2), 'miles')

km_to_miles(kilometers)
print()
