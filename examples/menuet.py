from melopy import Melopy
import os

def main():
    m = Melopy('menuet')
    d = os.path.dirname(__file__)
    if len(d):
        m.parsefile(d + '/scores/menuet.mlp')
    else:
        m.parsefile('scores/menuet.mlp')
    m.render()

if __name__ == '__main__':
    main()
