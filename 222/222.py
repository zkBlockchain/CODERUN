def process(main_g, nodes):
    node_store, main_teams = [], []
    while nodes:
        first_run = True
        current_team, team_backup, wrong = set(), set(), set()
        start_node = next(iter(nodes))
        node_store.append(start_node)
        nodes.discard(start_node)

        current_edges = main_g[node_store[-1]]
        while node_store:
            finale = False
            wrong_vertice = False

            team_backup.add(node_store[-1])
            if first_run:
                common_edges = current_edges.intersection(nodes)
                first_run = False

            if current_edges:
                finale = True
                contain_item = False
                for next_node in current_edges:
                    if next_node in nodes:
                        if not all(item in main_g[next_node] for item in team_backup):
                            continue
                        if next_node not in common_edges:
                            wrong.add(next_node)
                            continue
                        node_store.append(next_node)
                        nodes.discard(next_node)
                        vertice = next_node
                        contain_item = True
                        break
                if contain_item:
                    finale = False
                    current_edges = main_g[vertice]
                    common_edges.discard(vertice)
                    if common_edges:
                        copy = common_edges.intersection(current_edges)
                        if not copy:
                            wrong_vertice = True
                            finale = True
                        else:
                            common_edges = copy
            else:
                finale = True
            if finale:
                if wrong_vertice:
                    nodes.add(node_store[-1])
                    team_backup.discard(node_store[-1])
                    node_store.pop()
                    current_edges = main_g[node_store[-1]]
                else:
                    current_team.add(node_store.pop())
        main_teams.append(current_team)

    if len(main_teams) != 2:
        return False
    print(len(main_teams[0]))
    for teammate in main_teams:
        print(' '.join(map(str, teammate)))
    return True


def main():
    num_nodes, num_edges = map(int, input().split())

    if num_nodes * (num_nodes - 1) // 2 == num_edges:
        print('1\n1\n' + ' '.join(map(str, range(2, num_nodes + 1))))
        return

    nodes = set(range(1, num_nodes + 1))
    main_g = {i: set() for i in range(1, num_nodes + 1)}
    for _ in range(num_edges):
        first_node, second_node = map(int, input().split())
        main_g[first_node].add(second_node)
        main_g[second_node].add(first_node)

    if (num_edges == 0 and num_nodes != 2) or not process(main_g, nodes):
        print(-1)


if __name__ == "__main__":
    main()