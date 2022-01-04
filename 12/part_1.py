import collections
import sys

cave_graph = collections.defaultdict(set)

for line in sys.stdin:
    a, b = line.rstrip().split("-")
    cave_graph[a].add(b)

    if a != "start" and b != "end":
        cave_graph[b].add(a)

exploration_state = [
    {
        "path": ["start", next_cave],
        "small_caves_visited": set(["start", next_cave]) if next_cave.islower() else set(["start"])
    }
    for next_cave in cave_graph["start"]
]

paths = []

while len(exploration_state) > 0:
    record = exploration_state.pop()
    last_cave_visited = record["path"][-1]

    if last_cave_visited == "end":
        paths.append(record["path"])
        continue

    next_caves = [
        next_cave for next_cave in cave_graph[last_cave_visited]
        if not next_cave in record["small_caves_visited"]
    ]

    for next_cave in next_caves:
        small_caves_visited = record["small_caves_visited"].copy()
        if next_cave.islower():
            small_caves_visited.add(next_cave)

        exploration_state.append({
            "path": [*record["path"], next_cave],
            "small_caves_visited": small_caves_visited
        })

print(len(paths))
