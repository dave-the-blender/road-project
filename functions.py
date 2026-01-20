import bpy
from pathlib import Path

MAPPING_SINGLE_POST = {'type_1': 'Socket_2', 'radius_1': 'Socket_3', 'speed_1': 'Socket_4', 'speed_2': 'Socket_32', 'sign_type_11': 'Socket_5', 'sign_type_12': 'Socket_6', 'shape_type_1': 'Socket_7','shape_type_2': 'Socket_25', 'shape_scale_1': 'Socket_8', 'shape_offset_x_1': 'Socket_9', 'shape_offset_y_1': 'Socket_10','shape_scale_2': 'Socket_26', 'shape_offset_x_2': 'Socket_27', 'shape_offset_y_2': 'Socket_28', 'rotation_1': 'Socket_11', 'rotation_2': 'Socket_29', 'thickness': 'Socket_12', 'border_length': 'Socket_13', 'post': 'Socket_46', 'post_width': 'Socket_47', 'post_depth': 'Socket_48', 'post_height': 'Socket_49', 'gap': 'Socket_50', 'second_sign': 'Socket_19', 'type_2': 'Socket_21', 'radius_2': 'Socket_22', 'sign_type_21': 'Socket_23', 'sign_type_22': 'Socket_24', 'text_sign': 'Socket_20', 'text': 'Socket_33', 'sign_width': 'Socket_34', 'sign_height': 'Socket_35', 'text_scale': 'Socket_36', 'text_offset_x': 'Socket_37', 'text_offset_y': 'Socket_38', 'frame': 'Socket_39', 'base_material': 'Socket_14', 'white_material': 'Socket_15', 'red_material': 'Socket_16', 'black_material': 'Socket_17', 'blue_material': 'Socket_18'}
MAPPING_DOUBLE_POST = {'text': 'Socket_2', 'text_scale': 'Socket_11', 'text_offset_x': 'Socket_12', 'text_offset_y': 'Socket_13', 'width': 'Socket_3', 'height': 'Socket_4', 'thickness': 'Socket_5', 'border_lenght': 'Socket_6', 'frame': 'Socket_7', 'arrow': 'Socket_8', 'direction': 'Socket_9', 'strikethrough': 'Socket_10', 'exit': 'Socket_14', 'shape_scale': 'Socket_15', 'shape_offset': 'Socket_16', 'post': 'Socket_21', 'post_width': 'Socket_17', 'post_depth': 'Socket_18', 'post_height': 'Socket_20', 'post_position': 'Socket_19', 'base_material': 'Socket_22', 'background_material': 'Socket_23', 'frame_material': 'Socket_24', 'strikethrough_material': 'Socket_25', 'text_material': 'Socket_26'}

def import_assets():
    """Import all assets from the .blend file"""
    REQUIRED_GEO_NODES = [
        "DoublePostSign",
        "SinglePostSign",
        "GeneralSign",
        "TextSign",
        "Shapes",
        "Sign",
        "SignEngine",
        "Apothem"
    ]
    REQUIRED_MATERIALS = [
        "RoadRedMaterial",
        "RoadWhiteMaterial",
        "RoadBlackMaterial",
        "RoadBlueMaterial",
        "RoadMetalicMaterial",
        "RoadYellowMaterial"
    ]

    REQUIRED_FONTS = [
        "CCRIGE Regular"
    ]

    current_gn = [ng.name for ng in bpy.data.node_groups]
    missing_gn = [name for name in REQUIRED_GEO_NODES if name not in current_gn]

    current_mat = [mat.name for mat in bpy.data.materials]
    missing_mat = [name for name in REQUIRED_MATERIALS if name not in current_mat]

    current_fon = [fon.name for fon in bpy.data.fonts]
    missing_fon = [name for name in REQUIRED_FONTS if name not in current_fon]
    
    blender_file_path = str(Path(__file__).resolve().parent / "assets" / "road.blend")
    print(f"Importing assets from {blender_file_path}")

    with bpy.data.libraries.load(blender_file_path, link=False) as (data_from, data_to):
        available_gn = set(data_from.node_groups)
        gn_to_load = [n for n in missing_gn if n in available_gn]
        data_to.node_groups = gn_to_load

        available_mat = set(data_from.materials)
        mat_to_load = [n for n in missing_mat if n in available_mat]
        data_to.materials = mat_to_load

        available_fon = set(data_from.fonts)
        fon_to_load = [n for n in missing_fon if n in available_fon]
        data_to.fonts = fon_to_load

    for name in REQUIRED_GEO_NODES:
        ng = bpy.data.node_groups.get(name)
        if ng:
            ng.use_fake_user = True
    
    for name in REQUIRED_MATERIALS:
        mat = bpy.data.materials.get(name)
        if mat:
            mat.use_fake_user = True

    for name in REQUIRED_FONTS:
        fon = bpy.data.fonts.get(name)
        if fon:
            fon.use_fake_user = True

def _schedule_import():
    if not getattr(_schedule_import, "_queued", False):
        _schedule_import._queued = True

        def _run():
            _schedule_import._queued = False
            import_assets()
            return None

        bpy.app.timers.register(_run, first_interval=0.1)
        
def sync_gn_to_pg(context):
    """Syncs the values of the GN modifier with the Property Group, using the mapping
    Called when we change the selected object 
    """
    global MAPPING_SINGLE_POST, MAPPING_DOUBLE_POST

    obj = context.active_object
    mod = next(m for m in obj.modifiers if m.type == "NODES")

    # This fields are int in the modifier, but str in the property group. It is needed a type change
    enum_fields = [
        "type_1", "radius_1", "sign_type_11", "sign_type_12", "shape_type_1", "type_2", "radius_2", "sign_type_21", "sign_type_22", "shape_type_2",
        "direction"
        ]

    if obj["type"] == "single_post_sign":
        pg = context.window_manager.road_sp_sign_settings
        mapping = MAPPING_SINGLE_POST
    elif obj["type"] == "double_post_sign":
        pg = context.window_manager.road_dp_sign_settings
        mapping = MAPPING_DOUBLE_POST

    # Modifier properties
    for prop_name, socket_id in mapping.items():
        try:
            value = mod[socket_id]
            if prop_name in enum_fields:
                value = str(value)
            setattr(pg, prop_name, value)
        except Exception as e:
            print(f"Not possible to assign {prop_name} <- {socket_id}: {e}")



def update_properties(context, value, field):
        """
        Syncs the value in the PG with the Geometry Nodes Modifier. Called when we changes values in UI
        Called by the update in each property
        - context
        - value: from the changed porperty in the property group
        - field: string of the property. Used in the mapping to obtain the GN socket
        """
        global MAPPING_SINGLE_POST, MAPPING_DOUBLE_POST
        
        obj = context.active_object
        if obj["type"] == "single_post_sign":
            mapping = MAPPING_SINGLE_POST
        elif obj["type"] == "double_post_sign":
            mapping = MAPPING_DOUBLE_POST
        gn_socket = mapping[field]

        print_value = f"{value:.3f}" if type(value) == float else value
        print(f"Update called with value {print_value}\tto {gn_socket}\t({field})")

        mod = next(m for m in obj.modifiers if m.type == "NODES")
        mod[gn_socket] = value
        obj.update_tag()

