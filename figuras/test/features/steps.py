# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Figuras import Figuras

@step(u'Given I have the "([^"]*)" and side = (\d+)')
def given_i_have_the_side_square_side(step,figure,side):
    world.figure = figure
    world.side = int(side)

@step(u'Given I have the "([^"]*)" and radius = (\d+)')
def given_i_have_the_circle_radius(step,figure,radius):
    world.figure = figure
    world.side = int(radius)

@step(u'Given I have the "([^"]*)" with base = (\d+) and height = (\d+)')
def given_i_have_the_rectangle_base_height(step,figure,base, height):
    world.figure = figure
    world.side = 0
    world.sides = [int(base), int(height)]

@step(u'Given I have the "([^"]*)" with diagonal1 = (\d+) and diagonal2 = (\d+)')
def given_i_have_the_rhombus_diagonal1_diagonal2(step,figure,diagonal1, diagonal2):
    world.figure = figure
    world.side = 0
    world.sides = [int(diagonal1), int(diagonal2)]

@step(u'Given I have the "([^"]*)" with base = (\d+) and height = (\d+)')
def given_i_have_the_triangle_base_height(step,figure,base, height):
    world.figure = figure
    world.side = 0
    world.sides = [int(base), int(height)]



@step(u'When I compute its area')
def when_i_compute_its_area(step):
	figura=Figuras()
        if world.side:
	    world.area = figura.getArea_1(world.figure,world.side)
        else:
            world.area = figura.getArea_2(world.figure,world.sides[0],world.sides[1])
	
@step(u'Then I see the area (\d+)')
def then_i_see_the_number_1(step, expected):
    assert world.area == int(expected),'Area = {0} y esperada = {1}'.format(world.area,expected)

@step(u'Then I see the area "([^"]*)"')
def then_i_see_the_number_1(step, expected):
    assert str(world.area) == str(expected),'Area = {0} y esperada = {1}'.format(world.area,expected)



