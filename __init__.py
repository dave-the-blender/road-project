bl_info = {
    "name" : "The Road Project",
    "author" : "Dave the Blender",
    "description" : "",
    "blender" : (4, 5, 5),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

from . import panels, handlers, operators, properties

def register():
    properties.register()
    panels.register()
    handlers.register()
    operators.register()
    

def unregister():
    panels.unregister()
    handlers.unregister()
    operators.unregister()
    properties.unregister()



