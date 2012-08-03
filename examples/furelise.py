from melopy import Melopy
import os

def main():
    m = Melopy('furelise')
    m.parsefile(os.path.dirname(__file__) + '/scores/furelise.mlp')
    m.render()

if __name__ == '__main__':
    main()
