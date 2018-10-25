import json
import os


def load_from_json(file):
    try:
        with open(file) as config:
            data = json.load(config)
        return data
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku konfiguracyjnego!")
        exit(-1)


class Properties:
    def __init__(self):
        conf = os.getcwd()+"/config.json"
        data = load_from_json(conf)
        self.H = data["H"]
        self.L = data["L"]
        self.nH = data["nH"]
        self.nL = data["nL"]


class Node:
    def __init__(self, x_cord, y_cord, temp):
        self.x = x_cord
        self.y = y_cord
        self.t = temp


class Element:
    def __init__(self, a, b, c, d):
        self.id = [a, b, c, d]

    def __getitem__(self, index):
        return self.id[index]

    def __setitem__(self, index, value):
        self.id[index] = value


class Grid:
      def __init__(self):
        property = Properties()
        # temperatura startowa, moze sie pojawic w configu!
        starting_tmp = 0;
        self.nH=property.nH
        self.nL=property.nL
        delta_H = property.H/property.nH
        delta_L = property.L/property.nL

        self.nodes = []
        x = 0
        i = 0

        while i < property.H:
            j = 0
            y = 0
            while j < property.L:
                self.nodes.append(Node(x, y, starting_tmp))
                j = j + delta_L
                y = y + 1
            i = i + delta_H
            x = x + 1

        self.elements = []

        i = 0
        for i in range(0, property.nL-1):
            vertex_a = self.nH * i
            vertex_b = 7 * i + self.nH
            vertex_c = vertex_b + 1
            vertex_d = vertex_a + 1
            for j in range(0, property.nH-1):
                element = Element(vertex_a, vertex_b, vertex_c, vertex_d)
                self.elements.append(element)
                vertex_a = vertex_d
                vertex_b = vertex_c
                vertex_c = vertex_b + 1
                vertex_d = vertex_a + 1

        self.print_nodes()
        print("====")
        self.print_elements()

      def print_nodes(self):
        i = 0
        for node in self.nodes:
            print(str(i)+"\t\t"+str(node.x) +" "+ str(node.y)+" "+str(node.t))
            i += 1


      def print_elements(self):
        i = 0
        for element in self.elements:
            print(str(i)+"\t\t"+str(element.id[0])+" "+str(element.id[1])+" "+str(element.id[2])+" "+str(element.id[3]))
            i += 1
        return
