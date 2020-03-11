"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for items in sys.argv:
    print(items)

# Print out the OS platform you're using:
# YOUR CODE HERE
# print("OS Platform you're using:", sys.platform)

if sys.platform.startswith('win32'):
    print("Looks like you're using Windows")
elif sys.platform.startswith('linux'):
    print("Looks like you're using Linux")
elif sys.platform.startswith('cygwin'):
    print("Looks like you're using Windows/Cygwin")
elif sys.platform.startswith('darwin'):
    print("Looks like you're using MacOS")

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python Version:")
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Here's the current process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Here's the current working directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Hello there", os.getlogin())
