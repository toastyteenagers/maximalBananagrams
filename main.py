from BananagramsController import BanagramsController

if __name__ == '__main__':
    width = 7
    height = 7
    bc = BanagramsController(width, height)
    while True:
        bc.get_maximal_bananagrams()
