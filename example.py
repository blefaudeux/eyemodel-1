#!/usr/bin/python
# coding=utf-8

import eyemodel

#   ^
#   |    .-.
#   |   |   | <- Head
#   |   `^u^'
# Y |      ¦V <- Camera    (As seen from above)
#   |      ¦
#   |      ¦
#   |      o <- Target
#
#     ----------> X
#
# +X = left
# +Y = back
# +Z = up

with eyemodel.Renderer() as r:
    r.eye_target = [0, -1000, 0]
    r.camera_position = [20, -50, -10]
    r.camera_target = [0, -r.eye_radius, 0]
    r.eye_closedness = 0.2
    r.iris = "light"

    r.lights = [
        eyemodel.Light(
            type="sun",
            location = [10, -10, 100],
            strength = 10,
            target = [0,0,0]),
        eyemodel.Light(
            strength = 1,
            location = [15, -50, -10],
            target = r.camera_target),
        eyemodel.Light(
            strength = 1,
            location = [25, -50, -10],
            target = r.camera_target)
    ]

    r.render_samples = 50
    # r.render("example.png", "example.m")
    r.export_mesh("test.stl")
