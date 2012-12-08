from melopy import Melopy
import os

def main():
    m = Melopy('furelise')
    d = os.path.dirname(__file__)
    if len(d):
        m.parsefile(d + '/scores/furelise.mlp')
    else:
        m.parsefile('scores/furelise.mlp')
    m.render()

if __name__ == '__main__':
    main()
