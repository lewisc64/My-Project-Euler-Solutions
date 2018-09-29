
def load_grids(path):
    
    file = open(path, "r")
    content = file.read()
    file.close()

    grids = []
    
    for line in content.split("\n"):
        if line.startswith("Grid"):
            grids.append([])
            continue
        grids[-1].append([int(x) for x in line])
        
    return grids

def draw_grid(grid):
    for i, row in enumerate(grid):
        print("".join([str(x) for x in row]))
        if i % 3 == 0:
            #print()
            pass
    print()

def next_coords(x, y):
    x += 1
    if x >= 9:
        y += 1
        x = 0
    return x, y

def solve(grid, x=0, y=0):
    if y >= 9:
        return True
    if grid[y][x] != 0:
        return solve(grid, *next_coords(x, y))

    for n in range(1, 10):
        if n in grid[y]:
            continue
        elif n in [grid[sy][x] for sy in range(len(grid))]:
            continue
        else:
            valid = True
            for sy in range(y // 3 * 3, y // 3 * 3 + 3):
                for sx in range(x // 3 * 3, x // 3 * 3 + 3):
                    if grid[sy][sx] == n:
                        valid = False
                        break
                else:
                    continue
                break
            if valid:
                grid[y][x] = n
                if solve(grid, *next_coords(x, y)):
                    return True
                grid[y][x] = 0

grids = load_grids("grids.txt")
output = 0
for i, grid in enumerate(grids):
    print(f"solving grid {i+1}...")
    draw_grid(grid)
    solve(grid)
    draw_grid(grid)
    output += int("".join([str(x) for x in grid[0][:3]]))

print(output)
    
