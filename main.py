#Import the modules
from graphics import *

#Custom exeptions
class OutOfRangeError(Exception):
    "Credits which was entered you have a Out of range."
    pass

# sava data in file
def save_file(data: list):
    with open("data.txt", "w") as file:
        for x in data:
            string_list = [str(item) for item in x]
            file.write(string_list[0] + "-" + string_list[1]+","+ string_list[2] + "," + string_list[-1] + "\n")

# read data in file
def read_data() ->list:
    data = []
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            if len(lines) > 0:
                for line in lines:
                    data.append([line.rstrip().split(',')[0].split("-")[0], line.rstrip().split(',')[0].split("-")[1], line.rstrip().split(',')[1], line.rstrip().split(',')[2]])
                return data
            else:
                return data
                    
    except FileNotFoundError:
        return data
    finally:
        delete_data()

# Getting inputs function
def getting_inputs() ->int:
    while True:
        while True:
            try:
                pass_value = int(input("Enter your total PASS credits: "))
                if 0 > pass_value or pass_value > 120:
                    raise OutOfRangeError("Out of range.")
            except ValueError:
                print("Integer required.")
                continue
            except OutOfRangeError as error_message:
                print(error_message)
                continue
            break

        while True:
            try:
                defer_value = int(input("Enter your total DEFER credits: "))
                if 0 > defer_value or defer_value > 120:
                    raise OutOfRangeError("Out of range.")
            except ValueError:
                print("Integer required.")
                continue
            except OutOfRangeError as error_message:
                print(error_message)
                continue
            break

        while True:
            try:
                fail_value = int(input("Enter your total FAIL credits: "))
                if 0 > fail_value or fail_value > 120:
                    raise OutOfRangeError("Out of range.")
            except ValueError:
                print("Integer required.")
                continue
            except OutOfRangeError as error_message:
                print(error_message)
                continue
            break

        if pass_value + defer_value + fail_value != 120:
            print("Total incorrect.")
            continue
        break
    return pass_value,defer_value,fail_value

#Getting a progression outcome
def progression_outcome(pass_value:int,defer_value:int,fail_value:int) ->str:
    if pass_value == 120:
        pro_out = "Progress"
    elif pass_value >= 100:
        pro_out = "Progress(module trailer)"
    elif fail_value < 80:
        pro_out = "module retriever"
    else:
        pro_out = "Exclude"
    return pro_out

#Getting a progression outcome count
def progression_outcome_count(data_list:list) ->int:
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    excluded_count = 0
    if len(data_list) == 0:
        return progress_count,trailer_count,retriever_count,excluded_count
    else: 
        for data in data_list:
            if data[0] == "Progress":
                progress_count += 1
            elif data[0] == "Progress(module trailer)":
                trailer_count += 1
            elif data[0] == "module retriever":
                retriever_count += 1
            elif data[0] == "Exclude":
                excluded_count += 1
            else:
                pass
        return progress_count,trailer_count,retriever_count,excluded_count

#Program loop checker
def loop_checker(data:list) ->bool:
    print("\nWould you like to enter another set of data?")
    while True:
        user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "q":
            save_file(data)
            progress_count,trailer_count,retriever_count,excluded_count = progression_outcome_count(data)
            show_histrogram(progress_count,trailer_count,retriever_count,excluded_count,["Progress","Trailer","Retriever","Exclude"])
            return False
        else:
            print("Invalid input.Try again.")
            continue

#Show the histrogram 
def show_histrogram(bar1_count:int,bar2_count:int,bar3_count:int,bar4_count:int,names_of_bars:list):
    total_count = bar1_count + bar2_count + bar3_count + bar4_count
    each_count_list = [bar1_count,bar2_count,bar3_count,bar4_count]
    colours_of_bars = [color_rgb(51,255,51),color_rgb(102,51,0),color_rgb(255,0,0),color_rgb(96,96,96)]
    try:
        #create and customize the window
        window = GraphWin("Histrogram",770,600)
        window.setBackground(color_rgb(192,192,192))
        
        #create and customize the bars
        bar_x_position = 100
        text_x_position = 160
        bar_count = 0
        for bar_name in names_of_bars:
            bar = Rectangle(Point(bar_x_position,475),Point((bar_x_position+120),475 - (each_count_list[bar_count]*15)))
            bar.setFill(colours_of_bars[bar_count])
            bar.draw(window)

            text1_bar = Text(Point(text_x_position,490),bar_name)
            text1_bar.setTextColor("blue")
            text1_bar.setStyle("bold")
            text1_bar.setFace("arial")
            text1_bar.setSize(18)
            text1_bar.draw(window)

            text2_bar = Text(Point(text_x_position,460 - (each_count_list[bar_count]*15)), str(each_count_list[bar_count]))
            text2_bar.setTextColor("blue")
            text2_bar.setStyle("bold")
            text2_bar.setFace("arial")
            text2_bar.setSize(18)
            text2_bar.draw(window)

            bar_count += 1
            text_x_position += 150
            bar_x_position += 150

        #create and customize the title
        title_text = Text(Point(240,50),"Histrogram Results")
        title_text.setTextColor("black")
        title_text.setStyle("bold")
        title_text.setFace("arial")
        title_text.setSize(25)
        title_text.draw(window)

        #create and customize the total text
        total_text = Text(Point(230,540),str(total_count) +" outcomes in total.")
        total_text.setTextColor("black")
        total_text.setStyle("bold")
        total_text.setFace("arial")
        total_text.setSize(22)
        total_text.draw(window)

        #create and customize the line
        aline = Line(Point(70,475),Point(700,475))
        aline.setFill("black")
        aline.draw(window)

        window.getMouse()

    except GraphicsError:
        pass
    finally:
        window.close()

# Delete the file contains
def delete_data():
    with open("data.txt", "w") as file:
        pass

#Program variables
check = True
data_list = read_data()

# Main program loop
while check:
    pass_value,defer_value,fail_value = getting_inputs()
    pro_outcome = progression_outcome(pass_value,defer_value,fail_value)
    print(pro_outcome)
    data_list.append([pro_outcome,pass_value,defer_value,fail_value])
    check = loop_checker(data_list)

