import numpy as np
import matplotlib.pyplot as plt

def heaviside(x):
    if x < 5.3:
        return 0
    elif x == 5.3:
        return 0.5
    else:
        return 1

# Vektorisieren der Funktion, um mit numpy-Arrays zu arbeiten
heaviside_vec = np.vectorize(heaviside)

# Definieren des Bereichs für x-Werte
x_values = np.linspace(-5, 40, 1000)

# Berechnen der y-Werte
y_values = heaviside_vec(x_values)


plt.plot(x_values, y_values, label='Heaviside-Funktion')
plt.title('Heaviside-Funktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

#Datenpunkt
food_1=input("Gib das erste Lebensmittel ein")
x_point_1 = float(input("Geben Sie den x-Wert des Datenpunkts ein: "))
y_point_1 = heaviside(x_point_1)

food_2=input("Gib das erste Lebensmittel ein")
x_point_2 = float(input("Geben Sie den x-Wert des Datenpunkts ein: "))
y_point_2 = heaviside(x_point_2)

food_3=input("Gib das erste Lebensmittel ein")
x_point_3 = float(input("Geben Sie den x-Wert des Datenpunkts ein: "))
y_point_3 = heaviside(x_point_3)

# Anzeigen des Datenpunkts auf dem Graphen
plt.plot(x_point_1, y_point_1, 'ro', label=f'{food_1}')
plt.plot(x_point_2, y_point_2, 'go', label=f'{food_2}')
plt.plot(x_point_3, y_point_3, 'bo', label=f'{food_3}')
plt.legend()

plt.show()
