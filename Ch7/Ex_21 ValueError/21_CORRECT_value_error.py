try:
    birthmo = int(input('what month were you born?'))
    monthstogo = 12 - birthmo
    print(monthstogo, "months until your birthday")
except ValueError:
    print('enter a number, no letters')
