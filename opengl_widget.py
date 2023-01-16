import math

from Box2D import (b2_dynamicBody, b2_staticBody, b2Body, b2BodyDef,
                   b2FixtureDef, b2PolygonShape, b2Vec2, b2World)
from OpenGL.GL import *
from PyQt6.QtCore import QElapsedTimer, QTimer
from PyQt6.QtGui import QSurfaceFormat
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

from debug_drawer import DebugDrawer


class OpenGLWidget(QOpenGLWidget):

    def __init__(self):
        super().__init__()
        self.deltaTime = 0
        # Set up physics world
        self.WORLD_SCALE = 30.0
        self.world = b2World(gravity=b2Vec2(0.0, -9.8))
        # Set format
        format = QSurfaceFormat()
        format.setSamples(8)
        self.setFormat(format)

    def initializeGL(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)

        self.debugDrawer = DebugDrawer()
        self.world.renderer = self.debugDrawer

        self.debugDrawer.flags = { 'drawShapes': True,
            'drawJoints': True, 'drawAABBs': True, 'drawPairs': True }
        # print(self.debugDrawer.flags)

        boxShape = b2PolygonShape()
        boxShape.SetAsBox(10 / self.WORLD_SCALE, 10 / self.WORLD_SCALE)
        boxBodyDef = b2BodyDef()
        boxBodyDef.type = b2_dynamicBody
        self.boxBody = self.world.CreateBody(boxBodyDef)
        boxFixtureDef = b2FixtureDef()
        boxFixtureDef.shape = boxShape
        boxFixtureDef.density = 2
        self.boxBody.CreateFixture(boxFixtureDef)
        self.boxBody.position = b2Vec2(100 / self.WORLD_SCALE, 100 / self.WORLD_SCALE)

        groundShape = b2PolygonShape()
        groundShape.SetAsBox(100 / self.WORLD_SCALE, 10 / self.WORLD_SCALE)
        groundBodyDef = b2BodyDef()
        groundBodyDef.type = b2_staticBody
        groundBody = self.world.CreateBody(groundBodyDef)
        groundFixtureDef = b2FixtureDef()
        groundFixtureDef.shape = groundShape
        groundFixtureDef.density = 2
        groundBody.CreateFixture(groundFixtureDef)
        groundBody.position = b2Vec2(100 / self.WORLD_SCALE, 0 / self.WORLD_SCALE)

        platformShape = b2PolygonShape()
        platformShape.SetAsBox(30 / self.WORLD_SCALE, 5 / self.WORLD_SCALE)
        platformBodyDef = b2BodyDef()
        platformBodyDef.type = b2_staticBody
        platformBody = self.world.CreateBody(platformBodyDef)
        platformFixtureDef = b2FixtureDef()
        platformFixtureDef.shape = platformShape
        platformFixtureDef.density = 2
        platformBody.CreateFixture(platformFixtureDef)
        platformBody.position = b2Vec2(100 / self.WORLD_SCALE, 50 / self.WORLD_SCALE)
        platformBody.angle = math.radians(-10)

        self.timer = QTimer()
        self.timer.timeout.connect(self.animationLoop)
        self.elapsedTimer = QElapsedTimer()
        self.elapsedTimer.start()
        self.timer.start(1000//60)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.world.DrawDebugData()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 200, 0, 200, -10, 10)

    def animationLoop(self):
        self.deltaTime = self.elapsedTimer.elapsed() / 1000.0
        self.elapsedTimer.restart()
        self.world.Step(self.deltaTime, 8, 3)
        self.update()

    def restartSlot(self, gravity):
        self.boxBody.linearVelocity = b2Vec2(0, 0)
        self.boxBody.angularVelocity = 0
        self.boxBody.position = b2Vec2(100 / self.WORLD_SCALE, 100 / self.WORLD_SCALE)
        self.boxBody.angle = 0
        self.boxBody.awake = True
        self.world.gravity = b2Vec2(0, gravity)
