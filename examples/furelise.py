from melopy import Melopy
import os

def main():
    m = Melopy('furelise')
    m.parsefile(os.path.dirname(__file__) + '/meeps/furelise.mp')
    m.parsefile(os.path.dirname(__file__) + '/meeps/furelise_left.mp', 0)
    m.render()
    
if __name__ == '__main__':
    main()