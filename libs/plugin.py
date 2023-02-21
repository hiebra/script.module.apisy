def init():
    return sys.argv[0][:-1], int(sys.argv[1]), dict(parse_qsl(sys.argv[2][1:]))
items = []
def append(item):
    if item:
        items.append(item)
base, handle, parameters = init()
