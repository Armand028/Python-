class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle(Point):
    'Rectangle'
    def __init__(self,bottom_left,top_right,color):
        '''(Rectangle,Point,Point,str)->(None)'''
        self.bottom_left=bottom_left
        self.top_right=top_right
        self.color=color

    def get_color(self):
        '''(Rectangle)->(str)'''
        return self.color

    def get_bottom_left(self):
        '''(Rectanhgle)->(Point)'''
        return self.bottom_left

    def get_top_right(self):
        '''(Rectangle)->(Point)'''
        return self.top_right

    def reset_color(self,color2):
        '''(Rectangle,str)->(None)'''
        self.color=color2
    def __repr__(self):
       '''(Rectangle)->(str)'''
       return "Rectangle("+self.get_bottom_left().__repr__()+","+self.get_top_right().__repr__()+","+self.get_color()+")"

    def move(self,x,y):
        '''(Rectangle,number,number)->(None)'''
        bottom_left=self.get_bottom_left().move(x,y)
        top_right=self.get_top_right().move(x,y)
    def __str__(self):
        '''(Rectangle)->(str)'''
        return "I am a "+self.get_color()+" rectangle with bottom left corner at "+str(self.get_bottom_left().get())+" and top right corner at "+str(self.get_top_right().get())+"."
    def __eq__(self,other):
        '''(Rectangle,Rectangle)->(boolean)'''
        return self.get_bottom_left()==other.get_bottom_left() and self.get_top_right()==other.get_top_right() and self.get_color()==other.get_color()
        
    def get_perimeter(self):
        '''(Rectangle)->(number)'''
        return (abs(self.get_top_right().get()[0]-self.get_bottom_left().get()[0])+abs(self.get_top_right().get()[1]-self.get_bottom_left().get()[1]))*2
    def get_area(self):
        '''(Rectangle)->(number)'''
        return (abs(self.get_top_right().get()[0]-self.get_bottom_left().get()[0])*abs(self.get_top_right().get()[1]-self.get_bottom_left().get()[1]))
    def contains(self,k,l):
        '''(Rectangle,number,number)->(boolean)'''
        return k>=self.get_bottom_left().get()[0] and k<=self.get_top_right().get()[0] and l>=self.get_bottom_left().get()[1] and l<=self.get_top_right().get()[1]
    def intersects(self,other):
        '''(Rectangle,Rectangle)->(boolean)'''
        if(self.top_right.get()[0] < other.bottom_left.get()[0]):
            return False
        if(self.bottom_left.get()[0] > other.top_right.get()[0] ):
            return False
        if(self.top_right.get()[1] < other.bottom_left.get()[1]):
            return False
        if(self.bottom_left.get()[1] > other.top_right.get()[1]):
            return False
        return True

class Canvas:
    '''(Canvas)'''
    def __init__(self):
        '''(Canvas)->(None)'''
        self.list=list()
    def __len__(can):
        '''(Canvas)->(int)'''
        c=can.list
        return len(c)
    def __repr__(self):
        '''(Canvas)->(str)'''
        st=self.list.__repr__()
        return "Canvas("+st+")"
    def add_one_rectangle(self,rec):
        '''(Canvas,Rectangle)->(None)'''
        self.list.append(rec)

    def count_same_color(self,color):
        '''(Canvas,str)->(int)'''
        c=0
        for i in self.list:
            if i.get_color()==color:
                c+=1
        return c
    def total_perimeter(self):
        '''(Canvas)->(number)'''
        total=0
        for i in self.list:
            total+=i.get_perimeter()
        return total
    def common_point(self):
        '''(Canvas)->(bool)'''
        a=True
        for i in range(len(self.list)):
            b=self.list[i]
            for y in range(i+1,len(self.list)):
                other=self.list[y]
                a=b.intersects(other)
                if(a==False):
                    return a
        return a
    def min_enclosing_rectangle(self):
        '''(Canvas)->(Rectangle)'''
        x_min=self.list[0].get_bottom_left().get()[0]
        x_max=self.list[0].get_top_right().get()[0]
        y_min=self.list[0].get_bottom_left().get()[1]
        y_max=self.list[0].get_top_right().get()[1]
        for i in self.list:
            if(x_min>=i.get_bottom_left().get()[0]):
                x_min=i.get_bottom_left().get()[0]
            if(x_max<=i.get_top_right().get()[0]):
                x_max=i.get_top_right().get()[0]
            if(y_min>=i.get_bottom_left().get()[1]):
                y_min=i.get_bottom_left().get()[1]
            if(y_max<=i.get_top_right().get()[1]):
                y_max=i.get_top_right().get()[1]
        x=Point(x_min,y_min)
        y=Point(x_max,y_max)
        rec=Rectangle(x,y,"blue")
        return rec
            
            
    
        
    

