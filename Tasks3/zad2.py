"""test dzialania geompy"""
import geompy.figury2d as f2d
import geompy.figury3d as f3d


print(f"pole prostokata 2x3 {f2d.rectangle_area(2, 3)}")

circle_circumference1 = f2d.circle_circumference(16)
print(f"obwod kola r16 {circle_circumference1}")
print(f"objetosc szescianu a29 {f3d.cube_volume(29)}")
print(f"pole powierzchni kuli r51 {f3d.ball_area(51)}")
