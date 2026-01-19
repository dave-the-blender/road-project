import bpy
from .functions import import_assets, sync_gn_to_pg
from bpy.app.handlers import persistent #type: ignore

@persistent
def on_load_post(_):
    import_assets()

_LAST_ACTIVE_NAME = None

def depsgraph_handler(_depsgraph):
    global _LAST_ACTIVE_NAME
    context = bpy.context
    obj = context.view_layer.objects.active

    if obj and obj.get("type") and obj.name != _LAST_ACTIVE_NAME:
        _LAST_ACTIVE_NAME = obj.name
        sync_gn_to_pg(context)


def register():
    if on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(on_load_post)
    
    if depsgraph_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(depsgraph_handler)

def unregister():
    if on_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(on_load_post)

    if depsgraph_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(depsgraph_handler)
        
