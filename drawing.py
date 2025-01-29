import os
def create_grid(glist, field_names, field_widths, grid_name):
    """
    Creates a grid of glist.
    """
    start_first_row = "╔"
    end_first_row = "╗"
    start_middle_row = "╠"
    end_middle_row = "╣"
    start_last_row = "╚"
    end_last_row = "╝"
    separator_column = "║"
    separator_row = "═"
    separator_sub_row = "─"
    separator_sub_column = "│"
    separator_middle_row = "╬"
    start_middle_column = "╦"
    end_middle_column = "╩"
    end_line_corner = ""
    grid = []
    grid_first_row = start_first_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_first_row
    grid.append(grid_first_row)
    grid_middle_row = separator_column+grid_name.center(sum(field_widths)+((len(field_widths)-1)*3)," ")+separator_column
    grid.append(grid_middle_row)
    grid_middle_row = start_middle_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_middle_row
    grid.append(grid_middle_row)
    field_counter = 0
    for field_name in field_names:
        if field_counter == 0:
            grid_middle_row = separator_column+field_name.upper().center(field_widths[field_names.index(field_name)]," ")
            if field_counter != len(field_widths)-1:
                grid_middle_row += " "+separator_column+" "
            else:
                grid_middle_row += " "+separator_sub_column+" "
        elif field_counter == len(field_widths)-1:
            grid_middle_row += field_name.upper().center(field_widths[field_counter]," ")+separator_column
        else:
            grid_middle_row += field_name.upper().center(field_widths[field_names.index(field_name)]," ")+" "+separator_sub_column+" "
        field_counter += 1
    grid.append(grid_middle_row)
    grid_middle_row = separator_column+separator_sub_row * (sum(field_widths)+((len(field_widths)-1)*3))+separator_column
    grid.append(grid_middle_row)
    for row in glist:
        field_counter = 0
        for field_name in field_names:
            if field_counter == 0:
                grid_middle_row = separator_column + str(row[field_name]).center(field_widths[field_counter]," ")
                if field_counter == len(field_widths)-1:
                    grid_middle_row += " "+separator_column+" "
                else:
                    grid_middle_row += " "+separator_sub_column+" "
            elif field_counter == len(field_widths)-1:
                if row.get(field_name) == None:
                    grid_middle_row += " ".center(field_widths[field_counter]," ")
                else:
                    grid_middle_row += str(row[field_name]).center(field_widths[field_counter]," ")+separator_column
            else:
                if row.get(field_name) == None:
                    grid_middle_row +=" ".center(field_widths[field_names.index(field_name)]," ")+" "+separator_sub_column+" "
                else:
                    grid_middle_row += str(row[field_name]).center(field_widths[field_names.index(field_name)]," ")+" "+separator_sub_column+" "
            field_counter += 1
        grid.append(grid_middle_row)
        if glist.index(row) != len(glist)-1:
            grid_middle_row = separator_column+separator_sub_row*(sum(field_widths)+((len(field_widths)-1)*3))+separator_column
            grid.append(grid_middle_row)
    grid_last_row = start_last_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_last_row
    grid.append(grid_last_row)
    return grid

class Grid:
    special_characters = {"f.1":"╔","f.l":"╗","l.1":"╚","l.l":"╝","f.s":"╠","l.s":"╣","m.m":"╬",
                                 "f.m":"╦","l.m":"╩","fl":"║","fc":"═","ml":"│","mc":"─"}
    def __init__(self, grid_data=[], grid_name="", field_names=[], field_widths=[]):
        self.__grid_name = grid_name
        self.__field_names = field_names
        self.__field_widths = field_widths
        self.__gridWidth = sum(field_widths)+((len(field_widths))*3)-1
        self.__grid_data = grid_data
        self.__gridFirstLine = self.special_characters["f.1"]+self.special_characters["fc"]*(self.__gridWidth)+self.special_characters["f.l"]
        self.__gridLastLine = self.special_characters["l.1"]+self.special_characters["fc"]*(self.__gridWidth)+self.special_characters["l.l"]
        self.__gridMiddleLineNoneField = self.special_characters["f.s"]+self.special_characters["fc"]*(self.__gridWidth)+self.special_characters["l.s"]

    def __draw_grid_header(self):
        pass
    def draw_grid(self):
        """
        Creates a grid of glist.
        """
        pass

class Menu:
    special_characters = {"f.1":"╔","f.l":"╗","l.1":"╚","l.l":"╝","f.s":"╠","l.s":"╣","m.m":"╬",
                                 "f.m":"╦","l.m":"╩","fl":"║","fc":"═"}
    def __init__(self, title, options, width = 60, columns_number = 1):
        self.__title = title
        self.__options = options
        self.__width = width
        self.__invalid_choise = False
        self.__columns_number = columns_number
        self.__menu = []
    
    def __draw_header(self):
        dstr = Menu.special_characters["f.1"]+ Menu.special_characters["fc"] * (self.__width - 2) + Menu.special_characters["f.l"]
        self.__menu.append(dstr)
        # Here, the code should be developed by taking the title as an array and considering the possibility of having more lines.
        for line in self.__title:
            dstr = Menu.special_characters["fl"] + line.upper().center(self.__width - 2, " ") + Menu.special_characters["fl"]
            self.__menu.append(dstr)
        columns_width = int((self.__width - 2 - self.__columns_number) / self.__columns_number)
        dstr = Menu.special_characters["f.s"]
        for i in range(self.__columns_number):
            dstr += Menu.special_characters["fc"] * columns_width
            if i != self.__columns_number - 1:
                dstr += Menu.special_characters["f.m"]
            else:
                dstr += Menu.special_characters["fc"] * ((self.__width - 2 - self.__columns_number) % self.__columns_number)+Menu.special_characters["l.s"]
            menu.__menu.append(dstr)

    def __draw_menu():
        
        pass

    def show(self):
        # os.system("cls" if os.name == "nt" else "clear")
        # print(f"\n{self.title}")
        # for key, value in self.options.items():
        #     print(f"{key}. {value['label']}")
        # print("Q. Quit")
        # if self.invalid_choise :
        #     print("Incorrect choice. Please try again.")
        # choice = input("Enter your choice: ").strip().lower()
        # if choice.lower() in ["q","e","quit","exit"]:
        #     input("Press Enter to exit...")
        # elif choice in self.options:
        #     self.options[choice]["action"]()
        # else:
        #     self.invalid_choise = True
        #     self.show()
        pass