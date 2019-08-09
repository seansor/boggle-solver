def make_grid(width, height):
    """
    Creates grid that will hold all tiles
    fow a boggle game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
    }
    