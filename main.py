import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame):
    global grid
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(columns):
            neighbors = count_neighbors(i, j)
            if grid[i, j] == 1:  # Cell is alive
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0  # Cell dies
            else:  # Cell is dead
                if neighbors == 3:
                    new_grid[i, j] = 1  # Cell becomes alive
    grid = new_grid
    img.set_array(grid)
    return img,

def count_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            count += grid[(x + i) % rows, (y + j) % columns]
    count -= grid[x, y]
    return count

# Size of the grid
rows = 100
columns = 100

# Create an empty grid
grid = np.zeros((rows, columns))

# Fill the center area
grid[15:85, 15:85] = 1

# Set up the plot
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation="nearest", cmap="binary")
plt.axis("off")

# Animate the game
ani = animation.FuncAnimation(fig, update, frames=100, interval=200, blit=True)
plt.show()
