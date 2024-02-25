import numpy as np
import matplotlib.pyplot as plt

# Label für die y-Achse vergeben:
plt.ylabel('Energie')
plt.xlabel('Zucker')

#Datenpunkte Empfehlenswert
name_1=input("Gib den Namen eines empfehelenswerten Lebensmittel ein ")
x_1=int(input("Gib den Zuckergehalt von "+ name_1 + " an "))
y_1=int(input("Gib den Energiegehalt von "+ name_1 + " an "))
name_2=input("Gib den Namen eines empfehelenswerten Lebensmittel ein ")
x_2=int(input("Gib den Zuckergehalt von "+ name_2 + " an "))
y_2=int(input("Gib den Energiegehalt von "+ name_2 + " an "))
name_3=input("Gib den Namen eines empfehelenswerten Lebensmittel ein ")
x_3=int(input("Gib den Zuckergehalt von "+ name_3 + " an "))
y_3=int(input("Gib den Energiegehalt von "+ name_3 + " an "))
name_4=input("Gib den Namen eines empfehelenswerten Lebensmittel ein ")
x_4=int(input("Gib den Zuckergehalt von "+ name_4 + " an "))
y_4=int(input("Gib den Energiegehalt von "+ name_4 + " an "))
name_5=input("Gib den Namen eines empfehelenswerten Lebensmittel ein ")
x_5=int(input("Gib den Zuckergehalt von "+ name_5 + " an "))
y_5=int(input("Gib den Energiegehalt von "+ name_5 + " an "))

#Datenpunkte Nicht Empfehlenswert
name_a=input("Gib den Namen eines nicht empfehelenswerten Lebensmittel ein ")
x_a=int(input("Gib den Zuckergehalt von "+ name_a + " an "))
y_a=int(input("Gib den Energiegehalt von "+ name_a + " an "))
name_b=input("Gib den Namen eines nicht empfehelenswerten Lebensmittel ein ")
x_b=int(input("Gib den Zuckergehalt von "+ name_b + " an "))
y_b=int(input("Gib den Energiegehalt von "+ name_b + " an "))
name_c=input("Gib den Namen eines nicht empfehelenswerten Lebensmittel ein ")
x_c=int(input("Gib den Zuckergehalt von "+ name_c + " an "))
y_c=int(input("Gib den Energiegehalt von "+ name_c + " an "))
name_d=input("Gib den Namen eines nicht empfehelenswerten Lebensmittel ein ")
x_d=int(input("Gib den Zuckergehalt von "+ name_d + " an "))
y_d=int(input("Gib den Energiegehalt von "+ name_d + " an "))
name_e=input("Gib den Namen eines nicht empfehelenswerten Lebensmittel ein ")
x_e=int(input("Gib den Zuckergehalt von "+ name_e + " an "))
y_e=int(input("Gib den Energiegehalt von "+ name_e + " an "))

plt.plot([x_1,x_2,x_3,x_4,x_5],[y_1,y_2,y_3,y_4,y_5],'go')
plt.plot([x_a,x_b,x_c,x_d,x_e],[y_a,y_b,y_c,y_d,y_e],'ro')
# Achsen-Bereiche manuell festlegen
# Syntax: plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0, 80, 0, 700])

# Ein gepunktetes Diagramm-Gitter einblenden:
plt.grid(True)

# Diagramm anzeigen:
plt.show()

