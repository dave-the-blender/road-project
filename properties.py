import bpy
from bpy.types import PropertyGroup
from bpy.props import EnumProperty, PointerProperty
from .functions import update_properties

class ROAD_PG_settings(PropertyGroup):
    sign_type: EnumProperty(
        name="Type",
        items=[
            ('A', "Single Post", "Single Post Sign"),
            ('B', "Double Post", "Double Post Sign"),
        ],
        default='A'
    )# type: ignore


class ROAD_PG_single_post_sign(PropertyGroup):
	def update_type_1(self, context):
		value = int(self.type_1)
		update_properties(context, value, 'type_1')

	def update_radius_1(self, context):
		value = int(self.radius_1)
		update_properties(context, value, 'radius_1')

	def update_speed_1(self, context):
		value = self.speed_1
		update_properties(context, value, 'speed_1')

	def update_sign_type_11(self, context):
		value = int(self.sign_type_11)
		update_properties(context, value, 'sign_type_11')

	def update_sign_type_12(self, context):
		value = int(self.sign_type_12)
		update_properties(context, value, 'sign_type_12')

	def update_shape_type_1(self, context):
		value = int(self.shape_type_1)
		update_properties(context, value, 'shape_type_1')

	def update_shape_scale_1(self, context):
		value = self.shape_scale_1
		update_properties(context, value, 'shape_scale_1')

	def update_shape_offset_x_1(self, context):
		value = self.shape_offset_x_1
		update_properties(context, value, 'shape_offset_x_1')

	def update_shape_offset_y_1(self, context):
		value = self.shape_offset_y_1
		update_properties(context, value, 'shape_offset_y_1')

	def update_rotation_1(self, context):
		value = self.rotation_1
		update_properties(context, value, 'rotation_1')
	
	def update_rotation_2(self, context):
		value = self.rotation_2
		update_properties(context, value, 'rotation_2')

	def update_thickness(self, context):
		value = self.thickness
		update_properties(context, value, 'thickness')

	def update_border_length(self, context):
		value = self.border_length
		update_properties(context, value, 'border_length')

	def update_post(self, context):
		value = self.post
		update_properties(context, value, 'post')

	def update_post_width(self, context):
		value = self.post_width
		update_properties(context, value, 'post_width')

	def update_post_depth(self, context):
		value = self.post_depth
		update_properties(context, value, 'post_depth')

	def update_post_height(self, context):
		value = self.post_height
		update_properties(context, value, 'post_height')

	def update_gap(self, context):
		value = self.gap
		update_properties(context, value, 'gap')

	def update_second_sign(self, context):
		value = self.second_sign
		update_properties(context, value, 'second_sign')

	def update_type_2(self, context):
		value = int(self.type_2)
		update_properties(context, value, 'type_2')

	def update_radius_2(self, context):
		value = int(self.radius_2)
		update_properties(context, value, 'radius_2')

	def update_speed_2(self, context):
		value = self.speed_2
		update_properties(context, value, 'speed_2')

	def update_sign_type_21(self, context):
		value = int(self.sign_type_21)
		update_properties(context, value, 'sign_type_21')

	def update_sign_type_22(self, context):
		value = int(self.sign_type_22)
		update_properties(context, value, 'sign_type_22')

	def update_shape_type_2(self, context):
		value = int(self.shape_type_2)
		update_properties(context, value, 'shape_type_2')
	
	def update_shape_scale_2(self, context):
		value = self.shape_scale_2
		update_properties(context, value, 'shape_scale_2')

	def update_shape_offset_x_2(self, context):
		value = self.shape_offset_x_2
		update_properties(context, value, 'shape_offset_x_2')

	def update_shape_offset_y_2(self, context):
		value = self.shape_offset_y_2
		update_properties(context, value, 'shape_offset_y_2')

	def update_text_sign(self, context):
		value = self.text_sign
		update_properties(context, value, 'text_sign')

	def update_text(self, context):
		value = self.text
		update_properties(context, value, 'text')

	def update_sign_width(self, context):
		value = self.sign_width
		update_properties(context, value, 'sign_width')

	def update_sign_height(self, context):
		value = self.sign_height
		update_properties(context, value, 'sign_height')

	def update_text_scale(self, context):
		value = self.text_scale
		update_properties(context, value, 'text_scale')

	def update_text_offset_x(self, context):
		value = self.text_offset_x
		update_properties(context, value, 'text_offset_x')

	def update_text_offset_y(self, context):
		value = self.text_offset_y
		update_properties(context, value, 'text_offset_y')

	def update_frame(self, context):
		value = self.frame
		update_properties(context, value, 'frame')

	def update_base_material(self, context):
		value = self.base_material
		update_properties(context, value, 'base_material')

	def update_white_material(self, context):
		value = self.white_material
		update_properties(context, value, 'white_material')

	def update_red_material(self, context):
		value = self.red_material
		update_properties(context, value, 'red_material')

	def update_black_material(self, context):
		value = self.black_material
		update_properties(context, value, 'black_material')

	def update_blue_material(self, context):
		value = self.blue_material
		update_properties(context, value, 'blue_material')


	type_1: bpy.props.EnumProperty(
		name='Sign',
		items=[
			('0', 'Speed Limit', ''),
			('1', 'Speed Recommendation', ''),
			('2', 'Stop', ''),
			('3', 'Yield', ''),
			('4', 'No Entry', ''),
			('5', 'Warning', ''),
			('6', 'Direction', '')
		],
		default="0",
		update=update_type_1
	) #type: ignore
	radius_1: bpy.props.EnumProperty(
		name='Size',
		items=[
			('0', 'Small', ''),
			('1', 'Medium', ''),
			('2', 'Big', ''),
		],
		default="0",
		update=update_radius_1
	) #type: ignore
	speed_1: bpy.props.IntProperty(
		name='Speed',
		default=0,
		update=update_speed_1,
		min=10,
		max=130
	) #type: ignore
	sign_type_11: bpy.props.EnumProperty(
		name='Sign Shape',
		items=[
			('0', 'Circle', ''),
			('1', 'Square', '')
		],
		default="0",
		update=update_sign_type_11
	) #type: ignore
	sign_type_12: bpy.props.EnumProperty(
		name='Sign Shape',
		items=[
			('0', 'Circle', ''),
			('1', 'Square', '')
		],
		default="0",
		update=update_sign_type_12
	) #type: ignore
	shape_type_1: bpy.props.EnumProperty(
		name='Warning',
		items=[
			('2', 'Bump', ''),
			('4', 'Snow', '')
		],
		default="2",
		update=update_shape_type_1
	) #type: ignore
	shape_scale_1: bpy.props.FloatProperty(
		name='Shape Scale',
		default=0.0,
		update=update_shape_scale_1,
		min=0.1,
		max=4
	) #type: ignore
	shape_offset_x_1: bpy.props.FloatProperty(
		name='Shape Offset X',
		default=0.0,
		update=update_shape_offset_x_1,
		min=-1.0,
		max=1.0
	) #type: ignore
	shape_offset_y_1: bpy.props.FloatProperty(
		name='Shape Offset Y',
		default=0.0,
		update=update_shape_offset_y_1,
		min=-1.0,
		max=1.0
	) #type: ignore
	rotation_1: bpy.props.FloatProperty(
		name='Rotation',
		default=0.0,
		update=update_rotation_1,
		subtype="ANGLE",
		min=-180.0,
		max=180.0,
		precision=0,
		step=1
	) #type: ignore
	rotation_2: bpy.props.FloatProperty(
		name='Rotation',
		default=0.0,
		update=update_rotation_2,
		subtype="ANGLE",
		min=-180.0,
		max=180.0,
		precision=0,
		step=1
	) #type: ignore
	thickness: bpy.props.FloatProperty(
		name='Thickness',
		default=0.0,
		update=update_thickness,
		min=0.001,
		max=0.005
	) #type: ignore
	border_length: bpy.props.FloatProperty(
		name='Border Length',
		default=0.0,
		update=update_border_length,
		min=0.005,
		max=0.05
	) #type: ignore
	post: bpy.props.BoolProperty(
		name='Post',
		default=True,
		update=update_post
	) #type: ignore
	post_width: bpy.props.FloatProperty(
		name='Post Width',
		default=0.0,
		update=update_post_width,
		min=0.02,
		max=0.1
	) #type: ignore
	post_depth: bpy.props.FloatProperty(
		name='Post Depth',
		default=0.0,
		update=update_post_depth,
		min=0.01,
		max=0.1
	) #type: ignore
	post_height: bpy.props.FloatProperty(
		name='Post Height',
		default=0.0,
		update=update_post_height,
		min=1.0,
		max=5.0
	) #type: ignore
	gap: bpy.props.FloatProperty(
		name='Gap',
		default=0.0,
		update=update_gap,
		min=0.0,
		max=0.1
	) #type: ignore
	second_sign: bpy.props.BoolProperty(
		name='Second Sign',
		default=False,
		update=update_second_sign
	) #type: ignore
	type_2: bpy.props.EnumProperty(
		name='Sign',
		items=[
			('0', 'Speed Limit', ''),
			('1', 'Speed Recommendation', ''),
			('2', 'Stop', ''),
			('3', 'Yield', ''),
			('4', 'No Entry', ''),
			('5', 'Warning', ''),
			('6', 'Direction', '')
		],
		default="0",
		update=update_type_2
	) #type: ignore
	radius_2: bpy.props.EnumProperty(
		name='Size',
		items=[
			('0', 'Small', ''),
			('1', 'Medium', ''),
			('2', 'Big', ''),
		],
		default="0",
		update=update_radius_2
	) #type: ignore
	speed_2: bpy.props.IntProperty(
		name='Speed',
		default=0,
		update=update_speed_2,
		min=10,
		max=130
	) #type: ignore
	sign_type_21: bpy.props.EnumProperty(
		name='Sign Shape',
		items=[
			('0', 'Circle', ''),
			('1', 'Square', '')
		],
		default="0",
		update=update_sign_type_21
	) #type: ignore
	sign_type_22: bpy.props.EnumProperty(
		name='Sign Shape',
		items=[
			('0', 'Circle', ''),
			('1', 'Square', '')
		],
		default="0",
		update=update_sign_type_22
	) #type: ignore
	shape_type_2: bpy.props.EnumProperty(
		name='Warning',
		items=[
			('2', 'Bump', ''),
			('4', 'Snow', '')
		],
		default="2",
		update=update_shape_type_2
	) #type: ignore
	shape_scale_2: bpy.props.FloatProperty(
		name='Shape Scale',
		default=0.0,
		update=update_shape_scale_2,
		min=0.1,
		max=4
	) #type: ignore
	shape_offset_x_2: bpy.props.FloatProperty(
		name='Shape Offset X',
		default=0.0,
		update=update_shape_offset_x_2,
		min=-1.0,
		max=1.0
	) #type: ignore
	shape_offset_y_2: bpy.props.FloatProperty(
		name='Shape Offset Y',
		default=0.0,
		update=update_shape_offset_y_2,
		min=-1.0,
		max=1.0
	) #type: ignore
	text_sign: bpy.props.BoolProperty(
		name='Text Sign',
		default=False,
		update=update_text_sign
	) #type: ignore
	text: bpy.props.StringProperty(
		name='Text',
		default='',
		update=update_text
	) #type: ignore
	sign_width: bpy.props.FloatProperty(
		name='Sign Width',
		default=0.0,
		update=update_sign_width,
		min=0.1,
		max=4.0
	) #type: ignore
	sign_height: bpy.props.FloatProperty(
		name='Sign Height',
		default=0.0,
		update=update_sign_height,
		min=0.1,
		max=4.0
	) #type: ignore
	text_scale: bpy.props.FloatProperty(
		name='Text Scale',
		default=0.0,
		update=update_text_scale,
		min=0.1,
		max=4.0
	) #type: ignore
	text_offset_x: bpy.props.FloatProperty(
		name='Text Offset X',
		default=0.0,
		update=update_text_offset_x,
		min=-5.0,
		max=5.0
	) #type: ignore
	text_offset_y: bpy.props.FloatProperty(
		name='Text Offset Y',
		default=0.0,
		update=update_text_offset_y,
		min=-5.0,
		max=5.0
	) #type: ignore
	frame: bpy.props.FloatProperty(
		name='Frame',
		default=0.0,
		update=update_frame,
		min=0.005,
		max=0.05
	) #type: ignore
	base_material: bpy.props.PointerProperty(
		name='Base Material',
		type=bpy.types.Material,
		update=update_base_material
	) #type: ignore
	white_material: bpy.props.PointerProperty(
		name='White Material',
		type=bpy.types.Material,
		update=update_white_material
	) #type: ignore
	red_material: bpy.props.PointerProperty(
		name='Red Material',
		type=bpy.types.Material,
		update=update_red_material
	) #type: ignore
	black_material: bpy.props.PointerProperty(
		name='Black Material',
		type=bpy.types.Material,
		update=update_black_material
	) #type: ignore
	blue_material: bpy.props.PointerProperty(
		name='Blue Material',
		type=bpy.types.Material,
		update=update_blue_material
	) #type: ignore


class ROAD_PG_double_post_sign(PropertyGroup):
	def update_text(self, context):
		value = self.text
		update_properties(context, value, 'text')

	def update_text_scale(self, context):
		value = self.text_scale
		update_properties(context, value, 'text_scale')

	def update_text_offset_x(self, context):
		value = self.text_offset_x
		update_properties(context, value, 'text_offset_x')

	def update_text_offset_y(self, context):
		value = self.text_offset_y
		update_properties(context, value, 'text_offset_y')

	def update_width(self, context):
		value = self.width
		update_properties(context, value, 'width')

	def update_height(self, context):
		value = self.height
		update_properties(context, value, 'height')

	def update_thickness(self, context):
		value = self.thickness
		update_properties(context, value, 'thickness')

	def update_border_lenght(self, context):
		value = self.border_lenght
		update_properties(context, value, 'border_lenght')

	def update_frame(self, context):
		value = self.frame
		update_properties(context, value, 'frame')

	def update_arrow(self, context):
		value = self.arrow
		update_properties(context, value, 'arrow')

	def update_direction(self, context):
		value = int(self.direction)
		update_properties(context, value, 'direction')

	def update_strikethrough(self, context):
		value = self.strikethrough
		update_properties(context, value, 'strikethrough')

	def update_exit(self, context):
		value = self.exit
		update_properties(context, value, 'exit')

	def update_shape_scale(self, context):
		value = self.shape_scale
		update_properties(context, value, 'shape_scale')

	def update_shape_offset(self, context):
		value = self.shape_offset
		update_properties(context, value, 'shape_offset')

	def update_post(self, context):
		value = self.post
		update_properties(context, value, 'post')

	def update_post_width(self, context):
		value = self.post_width
		update_properties(context, value, 'post_width')

	def update_post_depth(self, context):
		value = self.post_depth
		update_properties(context, value, 'post_depth')

	def update_post_height(self, context):
		value = self.post_height
		update_properties(context, value, 'post_height')

	def update_post_position(self, context):
		value = self.post_position
		update_properties(context, value, 'post_position')

	def update_base_material(self, context):
		value = self.base_material
		update_properties(context, value, 'base_material')

	def update_background_material(self, context):
		value = self.background_material
		update_properties(context, value, 'background_material')

	def update_frame_material(self, context):
		value = self.frame_material
		update_properties(context, value, 'frame_material')

	def update_strikethrough_material(self, context):
		value = self.strikethrough_material
		update_properties(context, value, 'strikethrough_material')

	def update_text_material(self, context):
		value = self.text_material
		update_properties(context, value, 'text_material')


	text: bpy.props.StringProperty(
		name='Text',
		default='',
		update=update_text
	) #type: ignore
	text_scale: bpy.props.FloatProperty(
		name='Text Scale',
		default=0.0,
		update=update_text_scale,
		min=0.0,
		max=3.0
	) #type: ignore
	text_offset_x: bpy.props.FloatProperty(
		name='Text Offset X',
		default=0.0,
		update=update_text_offset_x,
		min=-5.0,
		max=5.0
	) #type: ignore
	text_offset_y: bpy.props.FloatProperty(
		name='Text Offset Y',
		default=0.0,
		update=update_text_offset_y,
		min=-5.0,
		max=5.0
	) #type: ignore
	width: bpy.props.FloatProperty(
		name='Width',
		default=0.0,
		update=update_width,
		min=0.1,
		max=5.0
	) #type: ignore
	height: bpy.props.FloatProperty(
		name='Height',
		default=0.0,
		update=update_height,
		min=0.05,
		max=2.0
	) #type: ignore
	thickness: bpy.props.FloatProperty(
		name='Thickness',
		default=0.0,
		update=update_thickness,
		min=0.001,
		max=0.01
	) #type: ignore
	border_lenght: bpy.props.FloatProperty(
		name='Border Lenght',
		default=0.0,
		update=update_border_lenght,
		min=0.005,
		max=0.05
	) #type: ignore
	frame: bpy.props.FloatProperty(
		name='Frame',
		default=0.0,
		update=update_frame,
		min=0.005,
		max=0.05
	) #type: ignore
	arrow: bpy.props.BoolProperty(
		name='Arrow',
		default=False,
		update=update_arrow
	) #type: ignore
	direction: bpy.props.EnumProperty(
		name='Direction',
		items=[
			('0', 'Right', ''),
			('1', 'Left', '')
		],
		default="0",
		update=update_direction
	) #type: ignore
	strikethrough: bpy.props.BoolProperty(
		name='Strikethrough',
		default=False,
		update=update_strikethrough
	) #type: ignore
	exit: bpy.props.BoolProperty(
		name='Exit',
		default=False,
		update=update_exit
	) #type: ignore
	shape_scale: bpy.props.FloatProperty(
		name='Shape Scale',
		default=0.0,
		update=update_shape_scale,
		min=0.0,
		max=5.0
	) #type: ignore
	shape_offset: bpy.props.FloatProperty(
		name='Shape Offset',
		default=0.0,
		update=update_shape_offset,
		min=-5.0,
		max=5.0
	) #type: ignore
	post: bpy.props.BoolProperty(
		name='Post',
		default=False,
		update=update_post
	) #type: ignore
	post_width: bpy.props.FloatProperty(
		name='Post Width',
		default=0.0,
		update=update_post_width,
		min=0.01,
		max=0.2
	) #type: ignore
	post_depth: bpy.props.FloatProperty(
		name='Post Depth',
		default=0.0,
		update=update_post_depth,
		min=0.01,
		max=0.1
	) #type: ignore
	post_height: bpy.props.FloatProperty(
		name='Post Height',
		default=0.0,
		update=update_post_height,
		min=0.1,
		max=4.0
	) #type: ignore
	post_position: bpy.props.FloatProperty(
		name='Post Position',
		default=0.0,
		update=update_post_position,
		min=0.0,
		max=1.0
	) #type: ignore
	base_material: bpy.props.PointerProperty(
		name='Base Material',
		type=bpy.types.Material,
		update=update_base_material
	) #type: ignore
	background_material: bpy.props.PointerProperty(
		name='Background Material',
		type=bpy.types.Material,
		update=update_background_material
	) #type: ignore
	frame_material: bpy.props.PointerProperty(
		name='Frame Material',
		type=bpy.types.Material,
		update=update_frame_material
	) #type: ignore
	strikethrough_material: bpy.props.PointerProperty(
		name='Strikethrough Material',
		type=bpy.types.Material,
		update=update_strikethrough_material
	) #type: ignore
	text_material: bpy.props.PointerProperty(
		name='Text Material',
		type=bpy.types.Material,
		update=update_text_material
	) #type: ignore



def register():
    bpy.utils.register_class(ROAD_PG_settings)
    bpy.utils.register_class(ROAD_PG_double_post_sign)
    bpy.utils.register_class(ROAD_PG_single_post_sign)

    bpy.types.WindowManager.road_settings = PointerProperty(type=ROAD_PG_settings)
    bpy.types.WindowManager.road_sp_sign_settings = PointerProperty(type=ROAD_PG_single_post_sign)
    bpy.types.WindowManager.road_dp_sign_settings = PointerProperty(type=ROAD_PG_double_post_sign)

def unregister():
    del bpy.types.WindowManager.road_settings
    del bpy.types.WindowManager.road_sp_sign_settings
    del bpy.types.WindowManager.road_dp_sign_settings

    bpy.utils.unregister_class(ROAD_PG_settings)
    bpy.utils.unregister_class(ROAD_PG_single_post_sign)
    bpy.utils.unregister_class(ROAD_PG_double_post_sign)