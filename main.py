import csv
import sys
import curses
from curses import wrapper
from sentence_annotator import SentenceAnnotator
import pandas as pd


def init_colours():
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)


def open_file(filepath):
    df = pd.read_csv(filepath, delimiter='\t',
                     skiprows=1, header=None,
                     engine='python', quoting=csv.QUOTE_NONE)
    df[4] = df[4].str.split('[', n=1, expand=True)[0]
    df.rename(columns={0: 'file', 2: 'position', 3: 'word', 4: 'post_tag'})
    df['timestamp'] = pd.Series(dtype='datetime64[ns]')
    return df.rename(columns={0: 'file', 2: 'position', 3: 'word', 4: 'post_tag'}).drop(columns=[5, 6, 7, 8, 9, 10, 11])


def main(stdscr):
    init_colours()
    w_b = curses.color_pair(1)

    tags_win = curses.newwin(20, 24)
    tags_win.bkgdset('_', w_b)
    tags_win.refresh()
    tags_win.addstr('This is a string in window for tags')
    tags_win.refresh()

    stdscr.refresh()
    key = stdscr.getkey()

    tags_win.addstr(key)
    tags_win.refresh()
    stdscr.getch()


if __name__ == '__main__':
    wrapper(main)
