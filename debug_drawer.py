from Box2D import b2Draw
from OpenGL.GL import *


class DebugDrawer(b2Draw):

    def DrawSolidPolygon(self, vertexes, color):
        # print("Polygon. Begin")
        # print(vertexes[0][0] * 30, vertexes[0][1] * 30)
        # print(vertexes[1][0] * 30, vertexes[1][1] * 30)
        # print(vertexes[2][0] * 30, vertexes[2][1] * 30)
        # print(vertexes[3][0] * 30, vertexes[3][1] * 30)
        # print("Polygon. End")

        glLineWidth(3)

        glBegin(GL_LINES)
        glColor3f(color.r, color.g, color.b)

        glVertex2f(vertexes[0][0] * 30, vertexes[0][1] * 30)
        glVertex2f(vertexes[1][0] * 30, vertexes[1][1] * 30)

        glVertex2f(vertexes[1][0] * 30, vertexes[1][1] * 30)
        glVertex2f(vertexes[2][0] * 30, vertexes[2][1] * 30)

        glVertex2f(vertexes[2][0] * 30, vertexes[2][1] * 30)
        glVertex2f(vertexes[3][0] * 30, vertexes[3][1] * 30)
        
        glVertex2f(vertexes[3][0] * 30, vertexes[3][1] * 30)
        glVertex2f(vertexes[0][0] * 30, vertexes[0][1] * 30)
        glEnd()

    def DrawPolygon(self, vertexes, color):
        pass
    def DrawSegment(self, p1, p2, color):
        pass
    def DrawPoint(self, p, size, color):
        pass
    def DrawCircle(self, center, radius, color, drawwidth=1):
        pass
    def DrawSolidCircle(self, center, radius, axis, color):
        pass
    def DrawTransform(self, xf):
        pass
