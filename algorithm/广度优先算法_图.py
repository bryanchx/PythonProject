from collections import deque
graph = {}
graph['you'] = ['bob', 'claire', 'alice']
graph['bob'] = ['anuj','peggy']
graph['claire'] = ['thom','jonny','mangguo']
graph['alice'] = ['peggy']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def search(name):
    search_tu = deque()
    search_tu+=graph[name]
    searched=[]
    while search_tu:
        item =search_tu.popleft()
        if item not in searched:
            if item == 'mangguo':
                return True
            else:
                search_tu+=graph[item]
                searched.append(item)
    return False

if __name__ == '__main__':
    b = search('you')
    print(b)
