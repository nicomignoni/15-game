import random as r
import igraph as ig
from copy import deepcopy

starting_positions = {3: ([[0, 1, 2], [3, 4, 5], [6, 7, 8]]),
                      4: ([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
                      }

winning_positions = {'0xbc614e', '0x75bcd0c',
                     '0x6b14e9f95da1aff57', '0x42ed123bda850df966'}

directions = ('w', 'a', 's', 'd')
shuffle = 80
size = 3

class Game:
    def __init__(self, table):
        if table == 'initial':
            self.table = deepcopy(starting_positions[size])
            random_directions = r.choices(directions, k=shuffle)
            for direction in random_directions:
                self.move(direction=direction)
        else:
            self.table = table

    def move(self, direction, other_table=None):
        if other_table is None:
            table = self.table
        else:
            table = other_table
        if (0 in table[0] and direction == 's' or
                0 in [table[i][0] for i in range(size)] and direction == 'd' or
                0 in table[size - 1] and direction == 'w' or
                0 in [table[i][size - 1] for i in range(size)] and direction == 'a'):
            return None
        else:
            n = [item for sublist in table for item in sublist].index(0)
            zero_index = (int(n / size), n % size)
            if direction == 'w':
                table[zero_index[0] + 1][zero_index[1]], table[zero_index[0]][zero_index[1]] = \
                    table[zero_index[0]][zero_index[1]], table[zero_index[0] + 1][zero_index[1]]
                if other_table is None:
                    return
                else:
                    return other_table
            elif direction == 's':
                table[zero_index[0] - 1][zero_index[1]], table[zero_index[0]][zero_index[1]] = \
                    table[zero_index[0]][zero_index[1]], table[zero_index[0] - 1][zero_index[1]]
                if other_table is None:
                    return
                else:
                    return other_table
            elif direction == 'a':
                table[zero_index[0]][zero_index[1] + 1], table[zero_index[0]][zero_index[1]] = \
                    table[zero_index[0]][zero_index[1]], table[zero_index[0]][zero_index[1] + 1]
                if other_table is None:
                    return
                else:
                    return other_table
            elif direction == 'd':
                table[zero_index[0]][zero_index[1] - 1], table[zero_index[0]][zero_index[1]] = \
                    table[zero_index[0]][zero_index[1]], table[zero_index[0]][zero_index[1] - 1]
                if other_table is None:
                    return
                else:
                    return other_table

    def solver(self):
        def tree_update():
            g.add_vertices(len(tables_to_add))
            g.vs[g.vcount() - len(tables_to_add):]['table'] = tables_to_add
            g.vs[g.vcount() - len(tables_to_add):]['move'] = move_to_add
            g.vs[g.vcount() - len(tables_to_add):]['depth'] = depth
            g.vs[g.vcount() - len(tables_to_add):]['value'] = value_to_add
            g.vs[g.vcount() - len(tables_to_add):]['degree'] = degree_to_add
            g.vs[g.vcount() - len(tables_to_add):]['sterile'] = False

        def encoder(table):
            flatted = [item for sublist in table for item in sublist]
            return hex(int(''.join([str(i) for i in flatted])))

        def attributes_update():
            tables_to_add.append(new_move)
            edges_to_add.append((node.index, g.vcount() + len(tables_to_add) - 1))
            move_to_add.append(direction)
            value_to_add.append(manhattan(new_move))
            memory.add(encoder(new_move))
            degree_to_add.append(1)

        def manhattan(table):
            distance = 0
            for i in range(size):
                for j in range(size):
                    distance += abs(int(table[i][j]/size) - i) + abs(table[i][j] % size - j)
            return distance

        if encoder(self.table) in winning_positions:
            return

        g = ig.Graph()
        g.add_vertex()
        depth = 0
        g.vs['table'] = [deepcopy(self.table)]
        g.vs['depth'] = [depth]
        g.vs['move'] = [None]
        g.vs['value'] = [manhattan(self.table)]
        g.vs['degree'] = [0]
        g.vs['sterile'] = [False]
        memory = {encoder(self.table)}
        while True:
            tables_to_add = []
            degree_to_add = []
            edges_to_add = []
            value_to_add = []
            move_to_add = []
            deepest_values = g.vs(degree_le=1, sterile_eq=False)['value']
            if deepest_values:
                nodes = g.vs(degree_le=1, value_eq=min(deepest_values))
            else:
                nodes = g.vs(degree_le=1, sterile_eq=False)
            for node in nodes:
                for direction in directions:
                    new_move = self.move(other_table=deepcopy(node['table']), direction=direction)
                    if new_move is not None and encoder(new_move) in winning_positions:
                        attributes_update()
                        tree_update()
                        g.add_edges(edges_to_add)
                        index = g.vcount() - 1
                        history = []
                        while index != 0:
                            history.append(g.vs[index]['move'])
                            index = min(g.neighbors(g.vs[index]))
                        history.reverse()
                        print(history)
                        return history
                    elif new_move is not None and encoder(new_move) not in memory:
                        node['degree'] += 1
                        attributes_update()
                if node['degree'] == 1:
                    node['sterile'] = True
            depth += 1
            tree_update()
            g.add_edges(edges_to_add)
            print(g.vcount())
            # ig.plot(g, bbox=(1200, 1200), vertex_label=(g.vs['value']))


test = Game(table='initial')
print(test.table)
#test.solver()

