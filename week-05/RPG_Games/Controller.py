class Controller():
    def __init__(self):
        self.game_map = "map/game_map.txt"

    def open_map_file(self, file_name):
        try:
            with open(file_name, "r") as file_open:
                lines = file_open.read().splitlines()
                return lines
        except IOError:
            print("File can not open!")

    def move_monsters(self):
        move_matrix = [[]]






