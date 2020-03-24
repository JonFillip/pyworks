# Importing a Single Class
from classes.robo_farms import Robot


bot = Robot("cyclopes", "armstrong", "harvesting")
bot.booting()

# Importing Multiple Classes from a Module
"""
To import multiple classes from a module that stores multiple classes the
general syntax to use is:
    from module_name import class_name, class_name1
"""

# Importing an Entire Module
"""
You can also import an entire module and then access the classes you need using 
the dot notation. The syntax for this procedure is as follows:

import Module_name

# To access the classes in the module

variable = module_name.ClassName
"""

# Importing All Classes from a Module
"""
You can import every class from a module using the following syntax:

from module_name import *
"""

# Importing a Module into a Module
"""
Sometimes you'll want to spread out your classes over several modules to keep 
any one file from growing too large and avoid storing unrelated classes in the
same module. The syntax for this procedure is as follows:  

from module_name import ClassName
from module_name1 import ClassName1

my_variable0 = ClassName(attributes)
my_variable0.class_method()

my_variable1 = ClassName1(attributes)
my_variable1.class_method1()
"""

# Using Aliases
"""
To use an alias to import a class the general syntax for this procedure is as 
follows:

from module_name import ClassName as CN

To access the class and create instances whenever you have an alias the syntax:

my_variable = CN(attributes)
"""
