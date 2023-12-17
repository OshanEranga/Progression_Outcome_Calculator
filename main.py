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
                    data.append([line.rstrip().split(',')[0].rstrip().split("-")[0], line.rstrip().split(',')[0].rstrip().split("-")[1], line.rstrip().split(',')[1], line.rstrip().split(',')[2]])
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

#Getting progression outcome
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

#Getting progression outcome count
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

#Show histrogram
def show_histrogram(bar1_count:int,bar2_count:int,bar3_count:int,bar4_count:int,names_of_bars:list):
    total_count = bar1_count + bar2_count + bar3_count + bar4_count
    try:
        #window customize
        window = GraphWin("Histrogram",770,600)
        window.setBackground(color_rgb(192,192,192))
        
        #Bar1 customize
        bar1 = Rectangle(Point(100,475),Point(220,475 - (bar1_count*15)))
        bar1.setFill(color_rgb(51,255,51))
        bar1.draw(window)

        text1_bar1 = Text(Point(160,490),names_of_bars[0])
        text1_bar1.setTextColor("blue")
        text1_bar1.setStyle("bold")
        text1_bar1.setFace("arial")
        text1_bar1.setSize(18)
        text1_bar1.draw(window)

        text2_bar1 = Text(Point(160,460 - (bar1_count*15)),str(bar1_count))
        text2_bar1.setTextColor("blue")
        text2_bar1.setStyle("bold")
        text2_bar1.setFace("arial")
        text2_bar1.setSize(18)
        text2_bar1.draw(window)

        #Bar2 customize
        bar2 = Rectangle(Point(250,475),Point(370,475 -(bar2_count*15)))
        bar2.setFill(color_rgb(102,51,0))
        bar2.draw(window)

        text1_bar2 = Text(Point(310,490),names_of_bars[1])
        text1_bar2.setTextColor("blue")
        text1_bar2.setStyle("bold")
        text1_bar2.setFace("arial")
        text1_bar2.setSize(18)
        text1_bar2.draw(window)

        text2_bar2 = Text(Point(310,460 -(bar2_count*15)),str(bar2_count))
        text2_bar2.setTextColor("blue")
        text2_bar2.setStyle("bold")
        text2_bar2.setFace("arial")
        text2_bar2.setSize(18)
        text2_bar2.draw(window)

        #Bar3 customize
        bar3 = Rectangle(Point(400,475),Point(520,475 - (bar3_count*15)))
        bar3.setFill(color_rgb(255,0,0))
        bar3.draw(window)

        text1_bar3 = Text(Point(460,490),names_of_bars[2])
        text1_bar3.setTextColor("blue")
        text1_bar3.setStyle("bold")
        text1_bar3.setFace("arial")
        text1_bar3.setSize(18)
        text1_bar3.draw(window)

        text2_bar3 = Text(Point(460,460-(bar3_count*15)),str(bar3_count))
        text2_bar3.setTextColor("blue")
        text2_bar3.setStyle("bold")
        text2_bar3.setFace("arial")
        text2_bar3.setSize(18)
        text2_bar3.draw(window)

        #Bar4 customize
        bar4 = Rectangle(Point(550,475),Point(670,475 -(bar4_count*15)))
        bar4.setFill(color_rgb(96,96,96))
        bar4.draw(window)

        text1_bar4 = Text(Point(610,490),names_of_bars[3])
        text1_bar4.setTextColor("blue")
        text1_bar4.setStyle("bold")
        text1_bar4.setFace("arial")
        text1_bar4.setSize(18)
        text1_bar4.draw(window)

        text2_bar4 = Text(Point(610,460-(bar4_count*15)),str(bar4_count))
        text2_bar4.setTextColor("blue")
        text2_bar4.setStyle("bold")
        text2_bar4.setFace("arial")
        text2_bar4.setSize(18)
        text2_bar4.draw(window)

        #title customize
        total_text = Text(Point(240,50),"Histrogram Results")
        total_text.setTextColor("black")
        total_text.setStyle("bold")
        total_text.setFace("arial")
        total_text.setSize(25)
        total_text.draw(window)

        #total text customize
        total_text = Text(Point(230,540),str(total_count) +" outcomes in total.")
        total_text.setTextColor("black")
        total_text.setStyle("bold")
        total_text.setFace("arial")
        total_text.setSize(22)
        total_text.draw(window)

        #line customize
        aline = Line(Point(70,475),Point(700,475))
        aline.setFill("black")
        aline.draw(window)

        window.getMouse()

    except GraphicsError:
        pass
    finally:
        window.close()

# Delete file contains
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




    
