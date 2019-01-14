import os


def reset():
    path = 'data'
    files = ['/Session.txt', '/Todo.txt', '/User.txt']
    if not os.path.exists(path):
        os.makedirs(path)
        for f in files:
            fp = open(path + f, 'w')
            fp.write('[]')
            fp.close()


if __name__ == '__main__':
    reset()