
from logging import *

basicConfig(filename='logfile.log',level=DEBUG,filemode='w',format='%(asctime)s -- %(message)s' )  # those error will be saved in that file at that location itself
#  By default it is in append mode , we can change it


info("This is info")
debug("This is debug")   # this will not be visible in the terminal
warning("This is warning")  # this will be visible and anything above it in the label would also be visible
error("This is error")
critical("This is critical")