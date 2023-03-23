import logging
import logging.config

'''
WARNING: LOG DON'T WORKING IF YOU CALL activate_logging() FROM settings DIRECTORY

If you want test logging from settings dir, you should in dictionary below at handlers -> file -> filename change 
'settings\\logs.log' to 'logs.log'
'''

LOGGING_CONFIG = {
    'version': 1,
    # 'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            # preview: INFO[2023-03-22 16:15:36,714] - This is information log (__main__)
            'format': '%(levelname)s[%(asctime)s] - %(message)s (%(name)s)'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },

        # This variant just write log in logs.log file. WARNING: every time when program start this file rewriting
        'file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'settings\\logs.log',
        },

        # This variant create new file every midnight
        # Be careful: this variant don't work correctly: every time when program start will be rewrite file logs.log
        # 'file': {
        #     'level': 'INFO',
        #     'formatter': 'standard',
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'filename': 'settings\\logs\\logs.log',
        #     'when': 'midnight',
        #     'interval': 1,
        # },
    },

    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
}


async def activate_logging():
    """
    This function return logging entity, so it's using like: logger = await activate_logging() in main() func.
    WARNING: recommended to create logger object on start program.

    :return:
    """

    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger(__name__)
