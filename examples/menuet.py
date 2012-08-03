from melopy import Melopy
import os

def main():
    m = Melopy('menuet')
    m.parsefile(os.path.dirname(__file__) + '/scores/menuet.mlp')
    m.render()

if __name__ == '__main__':
    main()
