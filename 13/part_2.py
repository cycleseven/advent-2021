import sys

# Parses into: coords = [{ "x": 6, "y": 10 }, { "x": 0, "y": 14 }, ...]
lines = sys.stdin.readlines()
coords = []
for line in lines:
    if line.isspace() or line.startswith("fold along"):
        continue

    coords.append(tuple(int(x) for x in line.split(",")))

# Parses into: folds = [{ axis: "y", value: 7 }, ...]
folds = []
for line in [l for l in lines if l.startswith("fold along")]:
    axis, raw_value = line.rstrip().replace("fold along ", "").split("=")
    folds.append({ "axis": axis, "value": int(raw_value) })

def apply_fold(coord, fold):
    folded_coord = { "x": coord[0], "y": coord[1] }

    if fold["axis"] == "y" and coord[1] > fold["value"]:
        folded_coord["y"] = fold["value"] - (coord[1] - fold["value"])

    if fold["axis"] == "x" and coord[0] > fold["value"]:
        folded_coord["x"] = fold["value"] - (coord[0] - fold["value"])

    return (folded_coord["x"], folded_coord["y"])

def visualise_coords(coords):
    max_x = 0
    max_y = 0

    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]

        if coord[1] > max_y:
            max_y = coord[1]

    visualisation = ""
    for _ in range(max_y + 1):
        for _ in range(max_x + 1):
            visualisation += "."
        visualisation += "\n"

    for x, y in coords:
        i = y * (max_x + 2) + x
        visualisation = visualisation[:i] + "#" + visualisation[i + 1:]

    print(visualisation)

folded_coords = set(coords)
for fold in folds:
    folded_coords = set(apply_fold(coord, fold) for coord in folded_coords)

visualise_coords(folded_coords)
