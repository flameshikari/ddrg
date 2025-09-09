def init():
    try:
        from termcolor import colored
    
    except ImportError:
        colored = lambda *args: args[0]
    
    return colored

color = init()

def init():
    import logging as log

    from config import config

    log.getLogger('urllib3').setLevel(log.ERROR)

    log.addLevelName(log.DEBUG, color('verb', 'magenta'))
    log.addLevelName(log.INFO, color('info', 'blue'))
    log.addLevelName(log.WARNING, color('warn', 'yellow'))
    log.addLevelName(log.ERROR, color('fail', 'red'))
    log.addLevelName(log.CRITICAL, color('crit', 'red'))

    log.basicConfig(
        level=log.DEBUG if config.args.verbose else log.INFO,
        datefmt='%H:%M:%S',
        format=f'{color("%(asctime)s", 'dark_grey')} [%(levelname)s] %(message)s',
    )

    def log_url(url, size, status = True):
        if config.args.verbose:
            status = color('+', 'green') if status else color('-', 'red') 
            prefix = color('0'*(11 - len(str(size))), 'dark_grey') + color(str(size), 'blue')
            log.debug(f"{status} {prefix} {color(url, 'dark_grey')}")

    log.url = log_url

    return log

log = init()