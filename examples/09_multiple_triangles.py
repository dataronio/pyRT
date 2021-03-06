# Example 9: Raytracing two triangles
#
# This time we render two triangles

from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Triangle, Vertex
from pyrt.camera import OrthographicCamera, PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image


# Specify width/height as in example 5
width = 320
height = 240

# now create a camera and a view like in example 5:
camera = PerspectiveCamera(width, height, 60)
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

# Create a scene
scene = Scene()

# Add a triangle (same as example 5) to the scene:
scene.add(Triangle(Vertex(position=(-5, 1, 0), color=(1,1,1)),
                   Vertex(position=(0, 1, 5), color=(0,1,1)),
                   Vertex(position=(5, 1, 0), color=(1,1,1))))

scene.add(Triangle(Vertex(position=(5, 1, 0), color=(1,1,1)),
                   Vertex(position=(0, 1, -5), color=(1,1,0)),
                   Vertex(position=(-5, 1, 0), color=(1,1,1))))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
image = engine.render(scene)

# Save the resulting image using pillow
image.save("09.png")
