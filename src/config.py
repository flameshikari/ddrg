def init():

    from argparse import ArgumentParser
    from types import SimpleNamespace as ns
    from os.path import abspath, dirname, join

    root = dirname(abspath(__file__))

    parser = ArgumentParser()

    parser.add_argument('-d', '--distros',
        default=[], action='append', metavar='NAME', nargs='+',
        help='define distros to scrape')

    parser.add_argument('-e', '--exclude',
        default=[], action='append', metavar='NAME', nargs='+',
        help='exclude distros')

    parser.add_argument('-H', '--html',
        default=False, action='store_true',
        help='generate html')

    parser.add_argument('-f', '--fallback',
        default=False, action='store_true',
        help='gather urls from predefined json for failed distros')

    parser.add_argument('-l', '--list',
        default=False, action='store_true',
        help='show available distros')

    parser.add_argument('-i', '--input',
        default=join(root, 'distros'), type=str,
        help='the dir with distros for parsing')

    parser.add_argument('-o', '--output',
        default=join(root, '../repo'), type=str,
        help='the dir for saving builded repo')

    parser.add_argument('-v', '--verbose',
        default=False, action='store_true',
        help='show more info when scraping distros')

    args = parser.parse_args()

    return ns(
        args=args,
        paths=ns(
            root=root,
            input=abspath(args.input),
            output=abspath(args.output),
        ),
    )

config = init()
