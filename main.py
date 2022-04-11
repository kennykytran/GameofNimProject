from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal=set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        return frozenset(state.symmetric_difference(action))
        # return [{'F', 'G'}]

    def actions(self, state):
        # 1st level
        if state == {'F', 'W', 'G', 'C'}:
            return [{'F', 'G'}]
        # 2nd level
        elif state == {'W', 'C'}:
            return [{'F', 'G'}, {'F'}]
        # 3rd level
        elif state == {'F', 'W', 'C'}:
            return [{'F'}, {'F', 'W'}, {'F', 'C'}]
        # 4th level
        elif state == {'C'}:
            return [{'F', 'W'}, {'F', 'G'}]
        elif state == {'W'}:
            return [{'F', 'G'}, {'F', 'C'}]
        # 5th level
        elif state == {'F', 'G', 'C'}:
            return [{'F', 'C'}, {'F', 'G'}]
        elif state == {'F', 'W', 'G'}:
            return [{'F', 'G'}, {'F', 'W'}]
        # 6th level
        elif state == {'G'}:
            return [{'F', 'C'}, {'F', 'W'}, {'F'}]
        # 7th level
        elif state == {'F', 'G'}:
            return [{'F'}, {'F', 'G'}]
        # 8th level
        elif state == {}:
            return [{'F', 'G'}]


def main():
    wgc = WolfGoatCabbage()

    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

    return


if __name__ == '__main__':
    main()