import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    from views import app
    app.run()
