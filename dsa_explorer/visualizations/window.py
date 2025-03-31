import moderngl
import moderngl_window
import numpy as np
from pyrr import Matrix44
from moderngl_window.context.base import WindowConfig

class Window(WindowConfig):
    title = "ModernGL Window"
    window_size = (800, 800)
    resource_dir = "."  # Base directory for shaders and resources

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = self.ctx.program(
            vertex_shader=open("shaders/vertex_shader.glsl").read(),
            fragment_shader=open("shaders/fragment_shader.glsl").read(),
        )

        vertices = self.ctx.buffer(
            np.array([
                # First triangle
                -0.5, -0.5,  # Bottom-left
                 0.5, -0.5,  # Bottom-right
                 0.5,  0.5,  # Top-right

                # Second triangle
                -0.5, -0.5,  # Bottom-left
                 0.5,  0.5,  # Top-right
                -0.5,  0.75,  # Top-left
            ], dtype=np.float32).tobytes()
        )

        # Vertex Array Object (VAO)
        self.vao = self.ctx.vertex_array(
            program=self.prog,
            content=[(vertices, "2f", "in_position")]
        )

        # Initialize transformation matrix
        self.transform = Matrix44.identity(dtype="f4")
        self.rotation_angle = 0.0

        # Initialize projection matrix
        aspect_ratio = self.window_size[0] / self.window_size[1]
        self.projection = Matrix44.orthogonal_projection(
            left=-aspect_ratio, 
            right=aspect_ratio, 
            bottom=-1, top=1, near=-1, far=1, 
            dtype="f4"
        )

    def on_render(self, time: float, frame_time: float):
        self.ctx.clear(0.2, 0.3, 0.3)       # Clear screen with a color

        # Update rotation angle
        self.rotation_angle += frame_time   # Rotate over time

        # Create tranformation matrix (combine rotation and translation)
        rotation = Matrix44.from_z_rotation(self.rotation_angle, dtype="f4")
        self.transform = self.projection

        self.prog["transform"].write(self.transform)

        self.vao.render(moderngl.TRIANGLES)

if __name__ == "__main__":
    moderngl_window.run_window_config(Window)