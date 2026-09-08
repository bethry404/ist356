import mycode as mc
# import pandas it finds the site packages folder and runs the init.py from the packages folder

print(mc.person)

mc.say_hi("Rylee")


# You can also import specific functions from the module == cherry picking
# cherry picking saves on resources if theres tons of lines in the module
from mycode import say_hi

say_hi("Riska")

# can rename imports as aliases if theres multiple module w same name
