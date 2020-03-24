
import builder

builder.make_car("Bugatti", "Black carbon", "beige leather")

# Importing the Entire Module
"""
To start importing functions, we have to first create a module. A file ending in
.py that contains the code of the function you want to import for example:
builder.py which contain the functions make_car(). Then we will have to create a
separate file in our case module1.py.

The first approach to importing, in which you simply write import followed by 
the name of the module, makes every function from the module available in your 
program. If you use this kind of import statement to import an entire module, 
each function in the module is available through the following syntax:
    import module_name

    module_name.function name()
"""
