# 2D/2.5D Sprite Renderer for Blender

The 2D/2.5D Sprite Renderer is a Blender addon that allows users to automatically render a 3D model from multiple angles. This is particularly useful for generating 2D sprites for use in 2D or 2.5D games.

## Installation
1. Download the addon from GitHub as a .zip file. (Click green button "Code" and then "Download ZIP")
2. In Blender, navigate to Edit > Preferences.
3. In the Addons tab, click Install... to open a file dialog.
4. Navigate to where you saved the .zip file, select it, and click Install Add-on.
5. The addon should now appear in the list of addons. Check the box next to its name to enable it.

## Usage
1. Open the 3D view sidebar (press N if it's not visible), and locate the "Sprite Renderer" panel.
2. Set the parameters for rendering:
    * `Character Height`: The height of the character in the scene.
    * `Number of Angles`: The number of angles from which the character will be rendered.
    * `Output Folder`: The directory where the rendered images will be saved.
    * `Basename`: The base name for the rendered image files.
    * `Perspective`: Choose between 2D and 2.5D. In 2.5D mode, you can specify the angle of the camera.
    * `Camera Angle`: The angle of the camera when rendering the scene. This is only applicable for 2.5D perspective.
    * `Camera Type`: Select between Orthographic and Perspective.
    * `Resolution`: The resolution of the output render.
    * `Include Animation`: Check if you want to render the character's animation.
    * `Frame Step`: If animation is included, you can specify the frame step to render every n-th frame.
3. After setting the parameters, click on Render Sprites to start the rendering process. This will create a sprite image for each angle in the specified output directory.

## Note
When using this addon, make sure that the character is at the origin of the scene (`0, 0, 0`). The addon will position the camera around the character based on the given parameters and render the scene from each camera position.