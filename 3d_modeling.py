from vpython import *

# Create a canvas
scene = canvas(title="Amazing 3D Solar System", 
               width=800, height=600, 
               center=vector(0, 0, 0), 
               background=color.black)

# Create the sun (glowing sphere)
sun = sphere(pos=vector(0, 0, 0), 
             radius=1, 
             color=color.yellow, 
             emissive=True, 
             shininess=1)

# Add some planets with orbital motion
planet1 = sphere(pos=vector(3, 0, 0), 
                 radius=0.2, 
                 color=color.blue, 
                 make_trail=True, 
                 trail_color=color.white)

planet2 = sphere(pos=vector(5, 0, 0), 
                 radius=0.4, 
                 color=color.red, 
                 make_trail=True, 
                 trail_color=color.yellow)

planet3 = sphere(pos=vector(8, 0, 0), 
                 radius=0.3, 
                 color=color.green, 
                 make_trail=True, 
                 trail_color=color.cyan)

# Add orbiting motion to the planets
t = 0
while True:
    rate(60)  # Frame rate of the animation
    
    # Orbital paths of the planets
    planet1.pos = vector(3 * cos(t), 3 * sin(t), 0)
    planet2.pos = vector(5 * cos(t * 0.8), 5 * sin(t * 0.8), 0)
    planet3.pos = vector(8 * cos(t * 0.6), 8 * sin(t * 0.6), 0)
    
    # Make the sun rotate for a dynamic effect
    sun.rotate(angle=0.02, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
    
    t += 0.01
