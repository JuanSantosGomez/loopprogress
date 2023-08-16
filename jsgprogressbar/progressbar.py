from sys import stdout

class bcolors:
    WARNING = '\033[93m'
    GRAY = '\033[0;90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'



def progressbar(it, prefix="", size=60, out=stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}{}{} {}{}{}{}{} {} {}/{}".format(bcolors.BOLD,prefix,bcolors.ENDC,bcolors.WARNING, "━"*x,bcolors.ENDC, bcolors.GRAY+"━"*(size-x)+bcolors.ENDC,bcolors.WARNING,bcolors.ENDC, j, count), 
                end='\r', file=out, flush=True)
        
        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)
