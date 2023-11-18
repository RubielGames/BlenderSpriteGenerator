# 2D/2.5D Sprite Renderer for Blender 3.x

The 2D/2.5D Sprite Renderer is a Blender addon designed to render 3D models from many angles. It's ideal for creating 2D sprites for 2D and 2.5D games.

## Installation
1. Download the addon from GitHub as a .zip file (click "Code" then "Download ZIP").
2. In Blender, go to Edit > Preferences.
3. In the Addons tab, select Install... to open a file dialog.
4. Find and select the .zip file you downloaded, then click Install Add-on.
5. The addon should now be in the list of addons. Enable it by checking the box next to its name.

## Usage
1. Open the 3D view sidebar (press N if hidden), and find the "Sprite Renderer" panel.
2. Set rendering parameters:
    * `Camera`: Choose a camera for rendering. Leave empty to use camera(s) parameters.
    * `Output Folder`: Directory for saving rendered images.
    * `Basename`: Base name for image files.
    * `Include Animation`: Enable to render animations.
    * `Frame Step`: If using animation, define the frame step for rendering.
    * `Character Height`: Set the character's height in the scene.
    * `Number of Angles`: Define how many angles to render the character from.
    * `Perspective`: Choose 2D or 2.5D. In 2.5D, set the camera angle.
    * `Camera Angle`: Set the camera angle for 2.5D perspective.
    * `Camera Type`: Choose Orthographic or Perspective.
    * `Resolution`: Set the output render resolution.
3. Click Render Sprites to start. This creates a sprite image for each angle in the output directory.

## Usage - No Camera Selected
This is the default setting. Ensure the character is at the origin (`0, 0, 0`). The addon will position cameras around the character based on your parameters. Typical top-down game settings are a `camera angle` of 30 to 60, `perspective` at 2.5, and `camera type` as Orthographic.

## Usage - Your Own Camera
This will disable Camera Settings box. Animation is still usable, ideal for rendering effects or non-static movements. For a camera style like the default:
* Select your camera.
* Go to the `Data` tab, expand `Lens`, and set `Type` to Orthographic.
* In the `Output` tab, adjust `Resolution` in the Format box.
* Press `F12` to test rendering.

## Tested on Versions
* Blender 4.0
* Blender 3.6
* GooEngine 3.6
* Blender 3.4
