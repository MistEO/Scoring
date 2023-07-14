import sys
import os
import typing
import pathlib

def file_score(filename) -> typing.Optional[typing.Tuple[int, int, int]]:
    """Return the score of a file based on its length and number of used characters."""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.isascii():
        return None

    # Score based on length
    score_len = len(content)

    # Score based on number of used characters
    score_cate = len(set(content))

    return score_len, score_cate, score_len * score_cate

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage:\n    python scoring.py <file>\n or\n    python scoring.py <directory>')
        exit()

    arg = sys.argv[1]
    if os.path.isfile(arg):
        path = pathlib.Path(arg)
        scores = file_score(path)
        if not scores:
            print(f'File: {path.absolute()} is not ASCII.')
        else:
            print(f'File: {path.absolute()}, Length: {scores[0]}, Category: {scores[1]}, Score: {scores[2]}')
    elif os.path.isdir(arg):
        min_scores = (0, 0, 0)
        min_path = pathlib.Path()
        for path in pathlib.Path(arg).glob('**/*'):
            scores = file_score(path)
            if not scores:
                print(f'File: {path.absolute()} is not ASCII.')
                continue
            print(f'File: {path.absolute()}, Length: {scores[0]}, Category: {scores[1]}, Score: {scores[2]}')
            if scores[2] < min_scores[2] or min_scores[2] == 0:
                min_scores = scores
                min_path = path
            
        if min_scores[2] == 0:
            print(f'\nNo ASCII file in {arg}.')
        else:
            print(f'\nBest file: {min_path.absolute()}, Length: {min_scores[0]}, Category: {min_scores[1]}, Score: {min_scores[2]}')