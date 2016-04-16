"""

Material Demo

This demonstrates the various materials the pipeline supports.
It is also a reference scene, for testing BRDF changes.

"""

from __future__ import print_function

import os
import sys
from panda3d.core import Vec3, load_prc_file_data
from direct.showbase.ShowBase import ShowBase

# Change to the current directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Insert the pipeline path to the system path, this is required to be
# able to import the pipeline classes
pipeline_path = "../../"

# Just a special case for my development setup, so I don't accidentally
# commit a wrong path. You can remove this in your own programs.
if not os.path.isfile(os.path.join(pipeline_path, "setup.py")):
    pipeline_path = "../../RenderPipeline/"

sys.path.insert(0, pipeline_path)

from rpcore import RenderPipeline, SpotLight

# This is a helper class for better camera movement - its not really
# a rendering element, but it included for convenience
from rpcore.util.movement_controller import MovementController

class Application(ShowBase):
    def __init__(self):

        # Setup window size, title and so on
        load_prc_file_data("", """
            win-size 1600 900
            window-title Render Pipeline - Material Sample
        """)

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        # Set time of day
        self.render_pipeline.daytime_mgr.time = "19:09"

        # Load the scene
        model = loader.load_model("scene/TestScene.bam")
        model.reparent_to(render)
        self.render_pipeline.prepare_scene(model)

        # Enable parallax mapping on the floor
        self.render_pipeline.set_effect(model.find("**/FloorPlane"),
            "effects/default.yaml", {"parallax_mapping": True}, 100)

        # Initialize movement controller
        self.controller = MovementController(self)
        self.controller.set_initial_position(
            Vec3(-15.0, -13.7, 5.9), Vec3(-12.0, -8.0, 4.6))
        self.controller.setup()

Application().run()
