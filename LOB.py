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
import math as m
import numpy as np

class Lemniscate_of_Bernoulli(ThreeDScene, Scene):
    def construct(self):
        ax = ThreeDAxes()
        Bernouli = Surface(
            lambda u,v : ax.c2p(*self.BernouliEq(u,v)),
            u_range = [0, TAU],
            v_range = [-PI/12, PI/6],
            resolution = 8 , 
            color = red 
        ).set_fill(opacity=0.7)
        Bernouli.set_color_by_gradient(blue, neon)
        # Bernouli.set_fill_by_value(
        #     axes= ax,
        #     colorscale= [ 
        #         #(red, 0),
        #         (blue, 0.5),
        #         (neon, 0.5)
        #     ]
        # )

        self.set_camera_orientation(
            #phi=60 * DEGREES
            phi = 60*DEGREES, 
            theta = -60*DEGREES
        )
        self.begin_ambient_camera_rotation(rate=0.2)

        #self.play(Create(ax), run_time=1.5)
        self.play(Write(Bernouli), run_time=5)
        self.wait(10)
    
    def BernouliEq(self, u, v):
        return [
            4*np.cos(u) / (1+ (np.sin(v)* np.sin(v))),
            4*(np.sin(u)* np.cos(u)) / (1+ (np.sin(v)* np.sin(v))), 
            4*np.sin(v)
                
            # 4*np.cos(v)*np.cos(u),
            # 4*np.cos(v)*np.sin(u),
            # 4*np.sin(v)
        ]