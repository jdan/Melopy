from melopy import Melopy
import os

def main():
    m = Melopy('entertainer')
    m.tempo = 140
    m.parsefile(os.path.dirname(__file__) + '/meeps/entertainer.mp')
    m.render()
    
if __name__ == '__main__':
    main()