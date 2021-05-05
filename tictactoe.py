import pytest

def winner(board):
    """ Given a board, returns either:
        'x': if x wins
        'o': if o wins
        'tie': in case of a tie
        None: if the match haven't finished yet
    """
    raise NotImplementedError()


def print_board(board):
    print(" {} | {} | {} ".format(*tuple(board[0][x] for x in range(0,3))))
    print("---+---+---")
    print(" {} | {} | {} ".format(*tuple(board[1][x] for x in range(0,3))))
    print("---+---+---")
    print(" {} | {} | {} ".format(*tuple(board[2][x] for x in range(0,3))))

TEST_CASES = [
    {  # 1
        "board": [
            ['o','o','o'],
            [' ','x','o'],
            ['o','x',' '],
        ],
        "winner": 'o'
    },

    {  # 2
        "board": [
            ['o','x','o'],
            [' ','x','o'],
            ['o','x',' '],
        ],
        "winner": 'x'
    },

    {  # 3
        "board": [
            ['o',' ','x'],
            [' ','o','x'],
            ['x',' ','o'],
        ],
        "winner": 'o'
    },

    {  # 4
        "board": [
            [' ','o','x'],
            [' ','x',' '],
            ['x',' ','o'],
        ],
        "winner": 'x'
    },

    {  # 5
        "board": [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' '],
        ],
        "winner": None
    },

    {  # 6
        "board": [
            [' ',' ',' '],
            [' ','x',' '],
            [' ','o',' '],
        ],
        "winner": None
    },

    {  # 6
        "board": [
            ['o','o','x'],
            ['x','x','o'],
            ['o','o','x'],
        ],
        "winner": 'tie'
    },
]


@pytest.mark.parametrize('board,expected_winner', tuple((x['board'], x['winner']) for x in TEST_CASES))
def test_tic_tac_toe(board, expected_winner):
    print_board(board)
    assert winner(board) == expected_winner
