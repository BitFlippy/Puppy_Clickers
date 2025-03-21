bl_info = {
    "name": "PUPPY CLICKER",
    "author": "Sarah.dxv3",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "File > Save",
    "description": "Positive reinforcement for cute puppies",
    "category": "System",
}

import bpy
import aud
import os

addon_dir = os.path.dirname(__file__)
SOUND_FILE = os.path.join(addon_dir, "Clicker_001.mp3")

def play_sound():
    device = aud.Device()
    sound = aud.Sound(SOUND_FILE)
    handle = device.play(sound)

def on_save(dummy):
    play_sound()

def register():
    bpy.app.handlers.save_post.append(on_save)

def unregister():
    bpy.app.handlers.save_post.remove(on_save)

if __name__ == "__main__":
    register()