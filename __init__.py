bl_info = {
    "name": "2D/2.5D Sprite Renderer",
    "description": "Automatically renders a character from multiple angles for use in 2D or 2.5D games",
    "author": "Rubiel",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Sidebar > Sprite Renderer Panel",
    "category": "Object",
}

import bpy
import os
from math import cos, sin, tan, atan
from mathutils import Vector


class CharacterSpriteRenderer(bpy.types.Operator):
    """2D/2.5D Sprite Renderer"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.sprite_renderer"  # Unique identifier for buttons and menu items to reference.
    bl_label = "Render Sprites"   # Display name in the interface.

    def execute(self, context): 

        # Getting properties from the scene
        character_position = Vector((0, 0, 0)) 
        character_height = context.scene.sprite_renderer.character_height
        number_of_angles = context.scene.sprite_renderer.number_of_angles

        output_folder = bpy.path.abspath(context.scene.sprite_renderer.output_folder)
        os.makedirs(output_folder, exist_ok=True)
        basename = context.scene.sprite_renderer.basename
        scene = bpy.context.scene
        scene.render.resolution_x = int(context.scene.sprite_renderer.resolution)
        scene.render.resolution_y = int(context.scene.sprite_renderer.resolution)
        scene.render.film_transparent = True

        perspective = context.scene.sprite_renderer.perspective
        camera_type = context.scene.sprite_renderer.camera_type

        # Check if the camera already exists in the scene
        camera_name = '2DSpriteCamera'
        if camera_name in bpy.data.objects:
            camera = bpy.data.objects[camera_name]
        else:
            # Add a new camera to the scene
            bpy.ops.object.camera_add(location=character_position)
            camera = bpy.context.object  # the newly added camera becomes the active object
            camera.name = camera_name  # set the camera name
        scene.camera = camera


        if camera_type == 'ORTHO':
            camera.data.type = 'ORTHO'
            camera.data.ortho_scale = character_height * 1.1
        else:
            camera.data.type = 'PERSP'

        if perspective == '2D':
            distance = 10
            z_distance = 0
        else:
            distance = 0.5 * character_height / tan(0.5 * atan(0.5 * camera.data.sensor_height / camera.data.lens))
            z_distance = distance


        # Loop to set the camera's position and render the scene
        for i in range(number_of_angles):
            angle = i * (2.0 * 3.14159 / number_of_angles)  # calculate angle

            # Set the camera's position
            camera.location.x = character_position.x + distance * cos(angle)
            camera.location.y = character_position.y + distance * sin(angle)
            camera.location.z = character_position.z + (character_height / 2) + z_distance

            # Point the camera to the character
            direction = Vector((character_position.x, character_position.y, character_position.z + (character_height / 2))) - camera.location
            camera.rotation_mode = 'QUATERNION'
            camera.rotation_quaternion = direction.to_track_quat('-Z', 'Y')  # camera looks towards the character

            # Set output path
            scene.render.filepath = os.path.join(output_folder, '{}_{}.png'.format(basename, i))

            # Render the scene
            bpy.ops.render.render(write_still = True)

        bpy.data.objects.remove(camera, do_unlink=True)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


# This is the Panel where you set the properties
class SpriteRendererPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Sprite Renderer"
    bl_idname = "OBJECT_PT_sprite_renderer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sprite Renderer"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        renderer = scene.sprite_renderer

        # draw the properties
        layout.prop(renderer, "character_height")
        layout.prop(renderer, "number_of_angles")
        layout.prop(renderer, "output_folder")
        layout.prop(renderer, "basename")
        layout.prop(renderer, "perspective")
        layout.prop(renderer, "camera_type")
        layout.prop(renderer, "resolution")

        # draw the operator
        layout.operator("object.sprite_renderer")


# This is the property group where you store your variables
class SpriteRendererProperties(bpy.types.PropertyGroup):

    character_height: bpy.props.FloatProperty(name="Character Height", default=2.0)
    number_of_angles: bpy.props.IntProperty(name="Number of Angles", default=8)
    output_folder: bpy.props.StringProperty(name="Output Folder", default="//", subtype='DIR_PATH')
    basename: bpy.props.StringProperty(name="Basename", default="render")
    perspective: bpy.props.EnumProperty(
        name="Perspective",
        description="Select Perspective type",
        items=[
            ('2D', "2D", ""),
            ('2.5D', "2.5D", "")
        ],
        default='2D',
    )
    camera_type: bpy.props.EnumProperty(
        name="Camera Type",
        description="Select Camera type",
        items=[
            ('ORTHO', "Orthographic", ""),
            ('PERSP', "Perspective", "")
        ],
        default='ORTHO',
    )
    resolution: bpy.props.EnumProperty(
        name="Resolution",
        description="Select the resolution",
        items=[
            ('32', "32x32", ""),
            ('64', "64x64", ""),
            ('128', "128x128", ""),
            ('256', "256x256", ""),
            ('512', "512x512", "")
        ],
        default='512',
    )


# Registration
def register():
    bpy.utils.register_class(CharacterSpriteRenderer)
    bpy.utils.register_class(SpriteRendererPanel)
    bpy.utils.register_class(SpriteRendererProperties)
    bpy.types.Scene.sprite_renderer = bpy.props.PointerProperty(type=SpriteRendererProperties)


def unregister():
    bpy.utils.unregister_class(CharacterSpriteRenderer)
    bpy.utils.unregister_class(SpriteRendererPanel)
    bpy.utils.unregister_class(SpriteRendererProperties)
    del bpy.types.Scene.sprite_renderer

if __name__ == "__main__":
    register()