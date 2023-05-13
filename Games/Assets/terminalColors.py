class TColor:
    '''Constant values to style text in terminal messages'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text):
    text=text.replace('#H', TColor.HEADER)
    text=text.replace('#B', TColor.OKBLUE)
    text=text.replace('#C', TColor.OKCYAN)
    text=text.replace('#G', TColor.OKGREEN)
    text=text.replace('#W', TColor.WARNING)
    text=text.replace('#F', TColor.FAIL)
    text=text.replace('#E', TColor.ENDC)
    text=text.replace('#S', TColor.BOLD)
    text=text.replace('#U', TColor.UNDERLINE)

    return text
