#  custom colors using HEX codes:
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


class Scene_1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            #phi=60 * DEGREES
            phi = 60*DEGREES, 
            theta = -60*DEGREES
        )
        self.begin_ambient_camera_rotation(rate=0.2)

        #axes = ThreeDAxes()
        torus = Torus(
            major_radius=2.5,
            minor_radius=1.5,
        ).set_opacity(0.5)
        torus.set_color_by_gradient(red, orange, yellow)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Write(torus), run_time = 5)
        self.wait(10)