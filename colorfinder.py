import colorthief
import matplotlib.pyplot as plt
c = colorthief.ColorThief('Saf.jpg')
gc = c.get_color()

plt.imshow([gc])
plt.show()

