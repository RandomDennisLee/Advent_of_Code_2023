class Pyramid:
    def __init__(self, bottom_layer: []):
        self.layers = [bottom_layer]

    def __repr__(self):
        result = ''
        for each in self.layers:
            result += str(each) + '\n'
        return result

    def add_layer (self):
        new_layer = []
        for i in range (len (self.layers[0]) - 1):
            new_layer.append(self.layers[0][i+1] - self.layers[0][i])

        self.layers.insert(0, new_layer)
        return new_layer

    def build (self):
        while self.layers[0].count(0) != len (self.layers[0]):
            self.add_layer()

    def extend (self):
        self.layers[0].append(0)
        for i in range (len (self.layers) - 1):
            self.layers[i+1].insert(0, self.layers[i+1][0]-self.layers[i][0])


if __name__ == '__main__':
    data = open ('input.txt').readlines()
    pyramids = []
    for line in data:
        bottom_layer = []
        for each in line.split():
            bottom_layer.append (int (each))

        pyramid = Pyramid (bottom_layer)
        pyramid.build()
        pyramid.extend()
        pyramids.append(pyramid)
        print (pyramid)

    result = 0
    for each in pyramids:
        bottom_layer = each.layers[len(each.layers)-1]
        result += bottom_layer[0]

    print (result)


