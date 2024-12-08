from heapq import heappop, heappush

def a_star(start, target, map_instance):
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, target)}

    while open_set:
        _, current = heappop(open_set)

        if current == target:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, map_instance):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, target)

                if not any(neighbor == cell for _, cell in open_set):
                    heappush(open_set, (f_score[neighbor], neighbor))

    return []

def heuristic(cell, target):
    x1, y1 = cell
    x2, y2 = target
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(cell, map_instance):
    x, y = cell
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [n for n in neighbors if map_instance.check_bounds(*n) and map_instance.check_cell(*n)]

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]
