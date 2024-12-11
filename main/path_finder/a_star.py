from heapq import heappop, heappush


def get_neighbors(cell, map_instance):
    x, y = cell
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    valid_neighbors = []

    for nx, ny in neighbors:
        if map_instance.check_bounds(nx, ny):
            if map_instance.check_cell(nx, ny):  # Пустая клетка
                valid_neighbors.append(((nx, ny), 1))  # Вес = 1
            elif map_instance.is_grass(nx, ny):  # Клетка с травой
                valid_neighbors.append(((nx, ny), 2))  # Вес = 2 (можно менять)
    return valid_neighbors


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

        for neighbor, weight in get_neighbors(current, map_instance):
            tentative_g_score = g_score[current] + weight

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


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]
