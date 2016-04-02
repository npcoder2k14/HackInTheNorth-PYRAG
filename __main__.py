import sys
import textwrap
def main():
    """\
    Usage: sport-api [-h] [-F] [-C] live_score|news|[player_stats name] [-my_fav_team]

    Get latest updates for football and cricket

    Options:

    -h, --help                shows help(this) message

    -F, --football [uefa,
    barclay, fifa]            Get football updates. The tournament for which you
                              want to get updates. One of the argumets from uefa,
                              barclay and fifa is compulsory.

    -C, --cricket             Get cricket updates for international matches.

    [live_score, news,
    player_stats[name]]       Fields to get. `live_scores` to get live socre of
                              on-going matches, `news` to get latest news headlines,
                              `player_stats` to get statistics of player specified.
                              Compulsory argument

    -proxy                    To specify proxy. Defaults to system proxy. Take name of
                              a file.
    """
    useage = textwrap.dedent(main.__doc__)
    args = sys.argv
    if args[1] == '-h':
        print(useage)
        sys.exit(0)
    args = args[1:]
    if args[1] == '-F' or args[1] == '--football':
        if args[2][1].lower() == 'c':
            raise ValueError('Both Football and cricket cannot be specified')
        if args[2] == 'uefa':

        elif args[2] == 'barclay':
            from barclay import Barclay
            if args[3] == ''
        elif args[2] == 'fifa':

        else:
            raise TypeError('None of the uefa, barclay, fifa was specified')


    if args[1]
if __name__ == '__main__':
    main()
