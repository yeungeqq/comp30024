# COMP30024 Artificial Intelligence, Semester 1 2024
# Project Part A: Single Player Tetress

from .core import PlayerColor, Coord, PlaceAction, BOARD_N
from .utils import render_board


def search(
    board: dict[Coord, PlayerColor], 
    target: Coord
) -> list[PlaceAction] | None:
    """
    This is the entry point for your submission. You should modify this
    function to solve the search problem discussed in the Part A specification.
    See `core.py` for information on the types being used here.

    Parameters:
        `board`: a dictionary representing the initial board state, mapping
            coordinates to "player colours". The keys are `Coord` instances,
            and the values are `PlayerColor` instances.  
        `target`: the target BLUE coordinate to remove from the board.
    
    Returns:
        A list of "place actions" as PlaceAction instances, or `None` if no
        solution is possible.
    """

    # The render_board() function is handy for debugging. It will print out a
    # board state in a human-readable format. If your terminal supports ANSI
    # codes, set the `ansi` flag to True to print a colour-coded version!
    print(render_board(board, target, ansi=False))

    # Do some impressive AI stuff here to find the solution...
    # separate red and blue into two lists
    red = []
    blue = []
    for coordination in board:
        if board[coordination] is PlayerColor.RED:
            red.append(coordination)
        else:
            blue.append(coordination)

    # find out the goal state - all coords that need to be filled to eliminate target
    goal_state_row = []
    goal_state_column = []
    for i in range(BOARD_N):
        goal_row_coord = Coord(target.r, i)
        goal_column_coord = Coord(i, target.c)
        if goal_row_coord not in blue:
            goal_state_row.append(goal_row_coord)
        if goal_column_coord not in blue:
            goal_state_column.append(goal_column_coord)
        i+=1

    # find out all possible PlaceActions to fulfill the goal state from the target
    # start from the top or from the left, calculate the mt distance between possible expansions and next empty block        
    # choose the expansion with closest mt distance, until all empty blocks is filled
    # if mt distance is indifferent, choose in the order of Up -> Down -> Left -> Right
    # if all empty blocks are filled and still need to expand remaining required blocks, choose the one with closest mt distance with the initial block
            
    # connect lines to the starting red points if there are paths to all lines
    # calculate the mt distance of possible expansions can choose the closest one
    # every four expansions will be grouped into one PlaceAction
    # if all options have same mt distance, choose the one with lowest r and c sum
    # if no possible expansion for a expanded block, undo the expansion and put that coord into the black list
    # if the expansion is adjacent to the initial red block but not the forth expansion of a PlaceAction, choose the one with lowest r and c sum

    # convert the PlaceAction backward

    # Here we're returning "hardcoded" actions as an example of the expected
    # output format. Of course, you should instead return the result of your
    # search algorithm. Remember: if no solution is possible for a given input,
    # return `None` instead of a list.
    return [
        PlaceAction(Coord(2, 5), Coord(2, 6), Coord(3, 6), Coord(3, 7)),
        PlaceAction(Coord(1, 8), Coord(2, 8), Coord(3, 8), Coord(4, 8)),
        PlaceAction(Coord(5, 8), Coord(6, 8), Coord(7, 8), Coord(8, 8)),
    ]

