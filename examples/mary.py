from melopy import Melopy
import os

def main():
    m = Melopy('mary')
    m.parsefile(os.path.dirname(__file__) + '/meeps/mary.mp')
    m.render()
    
if __name__ == '__main__':
    main()