#!/usr/bin/python3
"""
    base Module
"""
import json as js
import csv
import turtle
import random as rd
import time


class Base:
    """
        Base class
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """
            Initializion special method

            Args:
                id: integer to be initialized
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            gets the JSON string representation

            Args:
                list_dictionaries: Initial dictionary

            Returns:
                the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return js.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the json string representation to a
            file

            Args:
                list_objs: initial list
        """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                in_list = list()
                for instance in list_objs:
                    in_list.append(instance.to_dictionary())

                file.write(cls.to_json_string(in_list))

    @staticmethod
    def from_json_string(json_string):
        """
            gets the list of the JSON string representation json_string

            Args:
                json_string: string representing list of dictionaries

            Returns:
                the list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []

        return js.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Updates the base class

            Args:
                dictionary: dictionary to be updated

            Returns:
                an instance with all attributes already set
        """
        # create a dummy instance
        if cls.__name__ == "Square":
            dum_obj = cls(2)
        else:
            dum_obj = cls(2, 5)

        # update dummy instance with dictionary given
        dum_obj.update(**dictionary)

        # return updated dummy instance
        return dum_obj

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        list_convert = list()
        try:
            with open(cls.__name__ + '.json', encoding='utf-8') as filename:
                read_file = filename.read()
                convertt = cls.from_json_string(read_file)

                # convert list of dictionaries to list of instances
                for dictionary in convertt:
                    list_convert.append(cls.create(**dictionary))

                return list_convert
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes in csv

            Args:
                list_objs: list of objects
        """
        # create and write to the csv file
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as file:
            field_name = list()

            # get list of object keys
            field_name = (list_objs[0].to_dictionary()).keys()
            write_csv = csv.DictWriter(file, fieldnames=field_name)

            write_csv.writeheader()  # display the keys on the first line
            for dum in list_objs:
                write_csv.writerow(dum.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            returns deserialized csv content
        """
        with open(cls.__name__ + '.csv', encoding='utf-8') as file:
            new_l = []
            reader_csv = csv.DictReader(file)

            new_dic = dict()
            for content in reader_csv:
                for key, value in content.items():
                    new_dic[key] = int(value)
                new_l.append(cls.create(**new_dic))

            return new_l

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            a window that draws all instances of
            rectangles and squares

            Args:
                list_rectangles: list of rectangle objects
                list_squares: list of square objects
        """
        # create screen for GUI
        window_screen = turtle.Screen()
        window_screen.bgcolor("light blue")
        window_screen.title("Diagrams of Rectangles and Squares")

        # set up turtle color and objects
        colors = ['green', 'red', 'blue', 'black', 'purple', 'orange']
        col_len = len(colors)
        obj = turtle.Turtle()
        obj.speed(1)
        obj.pensize(5)

        # draw rectangles using turtle and clear screen
        obj.write("Rectangle Instances", align='center')
        time.sleep(1)
        for instance in list_rectangles:
            color_index = rd.randrange(0, col_len)
            obj.color(colors[color_index], colors[rd.randrange(0, col_len)])
            obj.begin_fill()
            obj.penup()
            obj.setpos((instance.x, instance.y))
            obj.pendown()

            for i in range(2):
                obj.forward(instance.height * 3)
                obj.right(90)
                obj.forward(instance.width * 3)
                obj.right(90)
            obj.end_fill()
            time.sleep(1)
            obj.clear()

        # draw squares using turtle and clear screen
        for index, instance in enumerate(list_squares):
            color_index = rd.randrange(0, col_len)  # get random colors
            obj.color(colors[color_index], colors[rd.randrange(0, col_len)])
            obj.begin_fill()
            obj.penup()
            obj.setpos((instance.x, instance.y))
            obj.pendown()

            for i in range(4):
                obj.forward(instance.size * 3)
                obj.right(90)

            if index != len(list_squares) - 1:
                obj.clear()
                time.sleep(1)
            obj.end_fill()
            time.sleep(1)

        # End the turtle GUI
        turtle.done()
