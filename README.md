# JSGprogressbar: Dynamic Progress Bar Module for Python

JSGprogressbar is a lightweight Python module that provides an elegant solution for incorporating dynamic progress bars into your loops. Say goodbye to the days of tedious guesswork during lengthy operations – with JSGprogressbar, you can effortlessly keep track of your loop's advancement in real-time, all while maintaining focus on your core logic.

## Features

- **Easy Integration**: Seamlessly integrate a progress bar into your loops with minimal code adjustments.
- **Real-time Updates**: Monitor the progress of your loop in real-time, eliminating uncertainty and improving user experience.
- **Customization Options**: Customize the appearance of the progress bar to match your application's aesthetics.
- **Completion Statistics**: Gain valuable insights into execution time and overall progress upon loop completion.
- **User-Friendly**: JSGprogressbar is designed with simplicity in mind, catering to programmers of all skill levels.
- **Versatile Compatibility**: Compatible with a wide range of Python projects, from data processing and analysis to simulations and batch operations.

## Usage

Simply import the `JSGprogressbar` class and create an instance, passing the required arguments:

```python
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
```

Then, simply utilize the `progressbar` generator function within your loop to integrate the progress bar. Here's an example:

```python
from jsgprogressbar.progressbar import progressbar

def main():
    total_items = 1000
    items_processed = 0

    for item in progressbar(range(total_items), prefix='Processing', size=50):
        # Your processing logic here
        items_processed += 1

if __name__ == "__main__":
    main()
```

## Installation

JSGprogressbar can be easily installed using pip:

```bash
pip install jsgprogressbar
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, open issues, and provide feedback! Happy coding with JSGprogressbar! 🚀