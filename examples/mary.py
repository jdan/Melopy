from melopy import Melopy
import os

def main():
    m = Melopy('mary')
    m.parse(os.path.dirname(__file__) + '/mary.mp')
    m.render()
    
if __name__ == '__main__':
    main()