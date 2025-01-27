
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

