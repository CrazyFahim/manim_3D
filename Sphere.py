#custom colors using HEX codes:
orange  = "#FF7F00"
blue    = "#2A32FA"
red     = "#E70A2E"
green   = "#58E70A"
yellow  = "#F7F609"
purple  = "#610788"
pink    = "#F71EF7"
neon    = "#1EF7F2"
black   = "#343434"
stale   = "#a2a2a2"
white   = "#ece6e2" 

from manim import*

class Scene_2(ThreeDScene, Scene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        ax = ThreeDAxes(
            x_range=[-4,4],
            x_length=8,
            y_range=[-4,4],
            y_length=8,
            z_range=[-4,4],
            z_length=8
        )
        sphere1 = Sphere(
            center=(0, 0, 0),
            radius=1.5,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color_by_gradient(neon, blue)
        sphere1.set_fill(opacity=0.5)
        
        self.set_camera_orientation(phi=60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        #self.play(Create(ax), run_time=1.5)
        self.play(Write(sphere1), run_time=3)

        self.wait(10)

        return super().construct()
