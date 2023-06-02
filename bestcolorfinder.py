import colorthief
import matplotlib.pyplot as plt

inp = input('Enter image name:')
c = colorthief.ColorThief(inp)
gc = c.get_palette(quality=1)

plt.imshow([gc])
plt.show()

