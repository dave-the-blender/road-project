import bpy


class ROAD_PT_main(bpy.types.Panel):
    bl_label = "Road"
    bl_idname = "ROAD_PT_Main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Road Assets"

    def draw(self, context):
        layout = self.layout

        # if context.active_object:
        #     layout.operator("dave.mapping")


class ROAD_PT_sign(bpy.types.Panel):
    bl_label = "Signs"
    bl_idname = "ROAD_PT_Sign"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Road Assets"
    bl_parent_id = "ROAD_PT_Main"

    def draw(self, context):
        layout = self.layout

        settings = context.window_manager.road_settings
        sp_sign_settings = context.window_manager.road_sp_sign_settings
        dp_sign_settings = context.window_manager.road_dp_sign_settings

        layout.operator("road.create_sign")
        layout.prop(settings, "sign_type")

        obj = context.active_object

        layout.separator()
        layout.separator()

        if obj is not None and obj.get("type") is not None:
            if obj["type"] == "single_post_sign":
                layout.label(text="Single Post Sign")
                box = layout.box()
                box.prop(sp_sign_settings, "type_1")
                box.prop(sp_sign_settings, "radius_1")
                if sp_sign_settings.type_1 in ["0", "1"]:
                    box.prop(sp_sign_settings, "speed_1")
                if sp_sign_settings.type_1 == "1":
                    box.prop(sp_sign_settings, "sign_type_11")
                if sp_sign_settings.type_1 == "5":
                    box.prop(sp_sign_settings, "shape_type_1")
                    box.prop(sp_sign_settings, "shape_scale_1")
                    box.prop(sp_sign_settings, "shape_offset_x_1")
                    box.prop(sp_sign_settings, "shape_offset_y_1")
                if sp_sign_settings.type_1 == "6":
                    box.prop(sp_sign_settings, "sign_type_12")
                    if sp_sign_settings.sign_type_12 == "0":
                        box.prop(sp_sign_settings, "rotation_1")  
                layout.separator()
                
                layout.label(text="Details")
                box = layout.box()
                box.prop(sp_sign_settings, "thickness")
                box.prop(sp_sign_settings, "border_length")
                if sp_sign_settings.post and (sp_sign_settings.second_sign or sp_sign_settings.text_sign):
                    box.prop(sp_sign_settings, "gap")
                layout.separator()

                layout.prop(sp_sign_settings, "post")
                if sp_sign_settings.post:
                    box = layout.box()
                    box.prop(sp_sign_settings, "post_height")
                    box.prop(sp_sign_settings, "post_width")
                    box.prop(sp_sign_settings, "post_depth")
                layout.separator()

                layout.prop(sp_sign_settings, "second_sign")
                if sp_sign_settings.second_sign:
                    box = layout.box()
                    if not sp_sign_settings.post:
                        box.label(text="Activate the Post to display a second sign")
                    else:
                        box.prop(sp_sign_settings, "type_2")
                        box.prop(sp_sign_settings, "radius_2")
                        if sp_sign_settings.type_2 in ["0", "1"]:
                            box.prop(sp_sign_settings, "speed_2")
                        if sp_sign_settings.type_2 == "1":
                            box.prop(sp_sign_settings, "sign_type_21")
                        if sp_sign_settings.type_2 == "5":
                            box.prop(sp_sign_settings, "shape_type_2")
                            box.prop(sp_sign_settings, "shape_scale_2")
                            box.prop(sp_sign_settings, "shape_offset_x_2")
                            box.prop(sp_sign_settings, "shape_offset_y_2")
                        if sp_sign_settings.type_2 == "6":
                            box.prop(sp_sign_settings, "sign_type_22")
                            if sp_sign_settings.sign_type_22 == "0":
                                box.prop(sp_sign_settings, "rotation_1")  
                layout.separator()
                
                layout.prop(sp_sign_settings, "text_sign")
                if sp_sign_settings.text_sign:
                    box = layout.box()
                    if not sp_sign_settings.post:
                        box.label(text="Activate the Post to display the text sign")
                    else:
                        box.prop(sp_sign_settings, "text")
                        box.prop(sp_sign_settings, "sign_width")
                        box.prop(sp_sign_settings, "sign_height")
                        box.prop(sp_sign_settings, "text_scale")
                        box.prop(sp_sign_settings, "text_offset_x")
                        box.prop(sp_sign_settings, "text_offset_y")
                        box.prop(sp_sign_settings, "frame")
                layout.separator()

                layout.label(text="Materials")
                box = layout.box()
                box.prop(sp_sign_settings, "base_material")
                box.prop(sp_sign_settings, "white_material")
                box.prop(sp_sign_settings, "red_material")
                box.prop(sp_sign_settings, "black_material")
                box.prop(sp_sign_settings, "blue_material")

 
            
            elif obj["type"] == "double_post_sign":
                layout.label(text="Double Post Sign")
                box = layout.box()
                box.prop(dp_sign_settings, "text")
                box.prop(dp_sign_settings, "text_scale")
                box.prop(dp_sign_settings, "text_offset_x")
                box.prop(dp_sign_settings, "text_offset_y")
                box.separator(type="LINE")
                box.prop(dp_sign_settings, "width")
                box.prop(dp_sign_settings, "height")
                box.prop(dp_sign_settings, "frame")
                layout.separator()

                layout.label(text="Details")
                box = layout.box()
                box.prop(dp_sign_settings, "thickness")
                box.prop(dp_sign_settings, "border_lenght")
                layout.separator()

                layout.prop(dp_sign_settings, "post")
                if dp_sign_settings.post:
                    box = layout.box()
                    box.prop(dp_sign_settings, "post_height")
                    box.prop(dp_sign_settings, "post_width")
                    box.prop(dp_sign_settings, "post_depth")
                    box.prop(dp_sign_settings, "post_position")
                layout.separator()

                layout.prop(dp_sign_settings, "strikethrough")
                layout.separator()

                layout.prop(dp_sign_settings, "arrow")
                if dp_sign_settings.arrow:
                    box = layout.box()
                    box.prop(dp_sign_settings, "direction")
                    box.prop(dp_sign_settings, "exit")
                    if dp_sign_settings.exit:
                        box.prop(dp_sign_settings, "shape_scale")
                        box.prop(dp_sign_settings, "shape_offset")
                layout.separator()

                layout.label(text="Materials")
                box = layout.box()
                box.prop(dp_sign_settings, "base_material")
                box.prop(dp_sign_settings, "background_material")
                box.prop(dp_sign_settings, "frame_material")
                box.prop(dp_sign_settings, "strikethrough_material")
                box.prop(dp_sign_settings, "text_material")


                

         


            

def register():
    bpy.utils.register_class(ROAD_PT_main)
    bpy.utils.register_class(ROAD_PT_sign)


def unregister():
    bpy.utils.unregister_class(ROAD_PT_main)
    bpy.utils.unregister_class(ROAD_PT_sign)
