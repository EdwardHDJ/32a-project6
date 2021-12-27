def change_number_to_color(number:int)->str:
    if number == 0:
        return 'R'
    elif number == 1:
        return 'O'
    elif number == 2:
        return 'Y'
    elif number == 3:
        return 'G'
    elif number == 4:
        return 'B'
    elif number == 5:
        return 'P'
    elif number == 6:
        return 'D'

class GameState:
    def __init__(self):
        self._board = []

    def initiate_game_board_to_empty(self,row:int,col:int)->None:
        board = []

        if row < 4 or col < 3:
            raise InvalidSizeError
        
        for col_number in range(0,col):
            board_sublist = []
            for row_number in range(0,row):
                board_sublist.append(None)
            board.append(board_sublist)

        self._board = board


    def check_if_faller_is_freezed(game_faller:'Faller')->'Faller':
        if game_faller == None:
            return False
        
        for jewel in game_faller.get_jewel_in_faller():
            if jewel.get_status() != 'freeze':
                return False
            
        return True


    def create_random_faller(game_state:'GameState')->'Faller':
        random_number_for_col = random.randint(0,5)
        count = 0
        
        while True:
            if game_state.get_board()[random_number_for_col][12] != None:
                random_number_for_col = random.randint(0,5)
                count += 1

            elif game_state.get_board()[random_number_for_col][12] == None:
                break
            
            if count == 20:
                print('game_over')
                return
            
        jewel1_color = change_number_to_color(random.randint(0,6))
        jewel2_color = change_number_to_color(random.randint(0,6))
        jewel3_color = change_number_to_color(random.randint(0,6))
        
        game_faller = set_up_faller(game_state,random_number_for_col,jewel1_color,jewel2_color,jewel3_color)

        return game_faller

    def change_jewel_list_status(jewel_list:['Jewel'],status:str)->None:
        for jewel in jewel_list:
            jewel.change_status(status)
            

class Jewel:
    def __init__(self,row_position:int,col_position:int,color_information:str,
                 status:str):
        self._col_position = col_position
        self._row_position = row_position
        self._color_information = color_information
        self._status = status


class Faller:
    def __init__(self,jewel1,jewel2,jewel3):
        self._jewel_in_faller = [jewel1,jewel2,jewel3]
