import bpy
from bpy.types import Operator #type: ignore


class ROAD_OT_create_sign(Operator):
    bl_idname = "road.create_sign"
    bl_label = "Create New"
    bl_description = "Create new sign"
    bl_options = {'UNDO'}

    def execute(self, context):

        settings = context.window_manager.road_settings
        sign_type = settings.sign_type

        #self.report({'INFO'}, f"Selected value: {sign_type}")
        bpy.ops.mesh.primitive_plane_add(size=1,location=(0.0, 0.0, 0.0))
        obj = context.active_object
        obj.name = "Sign"

        obt_attr = {
            "A": "single_post_sign",
            "B": "double_post_sign"
        }
        obj_node_group = {
            "A": "SinglePostSign",
            "B": "DoublePostSign"
        }

        obj["type"] = obt_attr[sign_type]

        ng = bpy.data.node_groups.get(obj_node_group[sign_type])
        mod = obj.modifiers.new(name="Sign_GeoNodes", type= "NODES")
        mod.node_group = ng

        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(ROAD_OT_create_sign)

def unregister():
    bpy.utils.unregister_class(ROAD_OT_create_sign)
