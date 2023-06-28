bl_info = {
    "name": "2D/2.5D Sprite Renderer",
    "description": "Automatically renders a character from multiple angles for use in 2D or 2.5D games",
    "author": "Rubiel",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Tool > Generate 2D Sprites",
    "category": "Object",
}

import bpy
import os
from math import cos, sin, tan, atan
from mathutils import Vector


class CharacterSpriteRenderer(bpy.types.Operator):
    """2D/2.5D Sprite Renderer"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.sprite_renderer"  # Unique identifier for buttons and menu items to reference.
    bl_label = "2D/2.5D Sprite Renderer"   # Display name in the interface.

    def execute(self, context): 

        # Assuming your character is at the center of the world, i.e., (0,0,0).
        # If not, change these values to the position of your character
        character_position = Vector((0, 0, 0)) 
        character_height = 2
        number_of_angles = 8

        output_folder = r'd:\tmp'
        os.makedirs(output_folder, exist_ok=True)
        scene = bpy.context.scene
        scene.render.resolution_x = 512
        scene.render.resolution_y = 512
        scene.render.film_transparent = True

        perspective = '2D'  # Choose the perspective: '2D' or '2.5D'
        camera_type = 'ORTHO'

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
            scene.render.filepath = os.path.join(output_folder, 'render_{}.png'.format(i))

            # Render the scene
            bpy.ops.render.render(write_still = True)

        bpy.data.objects.remove(camera, do_unlink=True)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(CharacterSpriteRenderer.bl_idname)

def register():
    bpy.utils.register_class(CharacterSpriteRenderer)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(CharacterSpriteRenderer)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()