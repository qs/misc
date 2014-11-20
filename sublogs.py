import logging
import multiprocessing
import os
import sys


def add_handler_once(LOG, handler):
    if handler.__class__ not in [h.__class__ for h in LOG.handlers]:
        LOG.addHandler(handler)
    if handler.__class__.__name__ == 'FileHandler':  # updates file for logging
        file_handlers = [h for h in LOG.handlers
                         if h.__class__.__name__ == 'FileHandler' and h.baseFilename != handler.baseFilename]
        if file_handlers:
            file_handlers[0].baseFilename = handler.baseFilename

def get_logger(logfile, quiet=True, level=logging.DEBUG, auto_log_base='./'):
    LOG = logging.getLogger('root')

    formatter = logging.Formatter()
    LOG.setLevel(level)
    logpath = os.path.join(auto_log_base, logfile + '.log')
    print logpath
    if sys.argv[0].endswith('nosetests'):
        quiet = False
    if quiet:
        add_handler_once(LOG, logging.NullHandler())
    else:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        add_handler_once(LOG, stream_handler)

    file_handler = logging.FileHandler(logpath)
    file_handler.setFormatter(formatter)
    add_handler_once(LOG, file_handler)

    LOG.info('writing to file {0}'.format(logpath))
    return LOG


LOG = get_logger('ololo')
LOG.debug("message")

