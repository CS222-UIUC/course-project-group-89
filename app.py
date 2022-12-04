'''this module renders a template and has two functions (testing for emily 10/1/22)'''
import time
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from parsing import filter_based_on_time, get_all_classes, remaining_classes, sort_core_classes


app = Flask(__name__)
class_cs =  ["CS 124", "CS 128", "CS 173", "MATH 241", "MATH 257",
    "CS 210", "CS 211", "CS 222", "CS 225", "CS 233", "CS 341",
    "CS 357", "CS 361", "CS 374", "CS 421"]

class_cs_stats =  ["CS 124", "CS 128", "CS 173", "CS 222", "CS 225",
    "MATH 241", "CS 233", "CS 341", "CS 340",  "CS 357", "MATH 257",
    "MATH 415", "MATH 416", "CS 374","CS 421", "STAT 107", "STAT 200",
     "STAT 212", "STAT 400", "STAT 410", "STAT 425", "STAT 426"]

class_cs_astro =  ["CS 124", "CS 128", "CS 173", "CS 222", "CS 225",
    "CS 233", "CS 341", "CS 340", "STAT 200", "STAT 212", "CS 361", "CS 374",
    "CS 421", "MATH 221", "MATH 220", "MATH 225", "MATH 257", "MATH 231",
    "PHYS 211", "PHYS 212", "MATH 241", "ASTR 210", "ASTR 310", "ASTR 404",
    "ASTR 405", "ASTR 406", "ASTR 414"]

class_cs_ggis = ["Needs to be Removed"]

@app.route('/')
def dropdown():
    """Sends List of Majors to Frontend"""
    cs_req = ["CS + GGIS", "CS + ASTRO", "STAT & CS", "CS"]
    return render_template('index.html', cs_req=cs_req)

@app.route('/major', methods=["POST"])
def main():
    "'This recives the major from dropdown and stores it in txt file'"
    major = request.form["major"]
    with open("store_user_input.txt", "w+", encoding="utf8") as curr_file:
        curr_file.write(f'User 1: {major}')
        curr_file.write("\n")
    curr_file.close()
    return render_template("index.html")

@app.route('/class', methods=["GET"])
def checkboxes():
    "'Based on major stores in txt file, send a list of classes to the front end'"
    major = ""
    with open('store_user_input.txt', encoding="utf8") as curr_file:
        major = curr_file.readline().strip('\n')
    cs_req = []
    major = major[8:].strip('\n')
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "STAT & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("class.html", cs_req= cs_req)

@app.route('/class', methods=["POST"])
def store_classes():
    "'Based on checkboxes selected from checkboxes(), store the classes in txt'"
    user_classes = request.form.getlist('user_classes')
    # user_classes = request.form["class"]
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for item in user_classes:
            curr_file.write(f'{item}\n')
        # curr_file.write("\n")
    curr_file.close()
    # return render_template("class.html")
    return redirect(url_for('class_info_main'))

@app.route('/classinfo', methods=["GET"])
def class_info_main():
    """Send the options for start and end time and # of credit hrs"""
    time_range = [
        "08:00 AM", "08:30 AM",
        "09:00 AM", "09:30 AM",
        "10:00 AM", "10:30 AM",
        "11:00 AM", "11:30 AM",
        "12:00 PM", "12:30 PM",
        "01:00 PM", "01:30 PM",
        "02:00 PM", "02:30 PM",
        "03:00 PM", "03:30 PM",
        "04:00 PM", "04:30 PM",
        "05:00 PM", "05:30 PM",
        "06:00 PM", "06:30 PM",
        "07:00 PM", "07:30 PM",
        "08:00 PM", "08:30 PM",
        "09:00 PM"]

    credit_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18]

    return render_template('classinfo.html', time_range=time_range, credit_hours = credit_hours)

@app.route('/info', methods=["POST"])
def store_class_info():
    """Store User 1 info for start, end, and # of credit hrs"""
    s_time = request.form["start_time"]
    end_time = request.form["end_time"]
    c_hours = request.form["credit_hour"]
    items = []
    items.append(s_time)
    items.append(end_time)
    items.append(c_hours)
    counter = 0
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for curr in items:
            if counter == 0:
                curr_file.write(f"User 1 Start Time: {curr}")
                counter = counter + 1
            elif counter == 1:
                curr_file.write(f"User 1 End Time: {curr}")
                counter = counter + 1
            else:
                curr_file.write(f"User 1 Credit Hours: {curr}")
            curr_file.write("\n")
    curr_file.close()
    return render_template('classinfo.html')

@app.route('/friendmajor', methods=["GET"])
def friendmajor():
    """Sends List of Majors to Frontend for User 2"""
    cs_req = ["CS + GGIS", "CS + ASTRO", "STAT & CS", "CS"]
    return render_template('friendmajor.html', cs_req=cs_req)

@app.route('/friendmajor', methods=["POST"])
def storefriendmajor():
    """For User 2, returns the major and stores it"""
    friend_major = request.form["friendmajor"]
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        curr_file.write(f'User 2: {friend_major}')
        curr_file.write("\n")
    curr_file.close()
    return render_template("friendmajor.html")

@app.route('/friendclass', methods=["GET"])
def friendclasses():
    """For User 2, read last line to get major for User 2 & return classes"""
    major = ""
    with open('store_user_input.txt', encoding="utf8") as curr_file:
        line = None
        for line in curr_file:
            pass
        major = line
    major = major[8:].strip('\n')
    cs_req = []
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "STAT & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("friendclass.html", cs_req = cs_req)

@app.route('/friendclass', methods=["POST"])
def storefriendclasses():
    """Store User 2's classes taken"""
    friend_classes = request.values.getlist('user_classes')
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for item in friend_classes:
            curr_file.write(f'{item}\n')
        # curr_file.write("\n")
    curr_file.close()
    return redirect(url_for('friend_class_info_main'))

@app.route('/friendclassinfo', methods=["GET"])
def friend_class_info_main():
    """Send User 2's class option to frontend"""
    time_range = [
        "08:00 AM", "08:30 AM",
        "09:00 AM", "09:30 AM",
        "10:00 AM", "10:30 AM",
        "11:00 AM", "11:30 AM",
        "12:00 PM", "12:30 PM",
        "01:00 PM", "1:30 PM",
        "02:00 PM", "02:30 PM",
        "03:00 PM", "03:30 PM",
        "04:00 PM", "04:30 PM",
        "05:00 PM", "05:30 PM",
        "06:00 PM", "06:30 PM",
        "07:00 PM", "07:30 PM",
        "08:00 PM", "08:30 PM",
        "09:00 PM"]

    credit_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18]

    return render_template('friendclassinfo.html',
    time_range=time_range, credit_hours = credit_hours)


@app.route('/friendinfo', methods=["POST"])
def store_friends_class_info():
    """Store User 2's class info"""
    s_time = request.form["start_time"]
    end_time = request.form["end_time"]
    c_hours = request.form["credit_hour"]
    items = []
    items.append(s_time)
    items.append(end_time)
    items.append(c_hours)
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for curr in items:
            if counter == 0:
                curr_file.write(f"User 2 Start Time: {curr}")
                counter = counter + 1
            elif counter == 1:
                curr_file.write(f"User 2 End Time: {curr}")
                counter = counter + 1
            else:
                curr_file.write(f"User 2 Credit Hours: {curr}")
            curr_file.write("\n")
        curr_file.write("\n")
    curr_file.close()
    return render_template('friendclassinfo.html')


@app.route('/classestotake', methods=["GET"])
def choose_classes():
    """Print out the classes User 1 and 2 can take together"""
    return_val = helper_function()
    user_one_class = return_val[0]
    user_two_class = return_val[1]
    user_one_major = return_val[2]
    user_two_major = return_val[3]
    user_one_class_info = return_val[4]
    user_two_class_info = return_val[5]

    smart_one = get_all_classes(sort_core_classes(user_one_major))
    temp_one = filter_based_on_time(smart_one, user_one_class_info[0], user_one_class_info[1])

    smart_two = get_all_classes(sort_core_classes(user_two_major))
    temp_two = filter_based_on_time(smart_two, user_two_class_info[0], user_two_class_info[1])

    para = [user_one_class, user_one_major, temp_one,
    temp_two, user_two_class, user_two_major]

    rem = helper_fun_two(para)
    return render_template("classestotake.html", json_file= rem.drop_duplicates().to_numpy())

def helper_function():
    """Helper function for choose_classes"""
    user_one_class = []
    user_two_class = []
    user_one_class_info = []
    user_one_major = ""
    user_two_major = ""
    user_two_class_info = []
    time.sleep(2)
    with open('store_user_input.txt', encoding="utf8") as curr_file:
        line = None
        for line in curr_file:
            if line[0:4] == "User" and user_one_major == "":
                user_one_major = line
            elif user_one_major != "" and user_two_major == "" and line[0:4] != "User":
                user_one_class.append(line)
            elif line[0:19] == "User 1 Start Time: ":
                user_one_class_info.append(line[19:].strip("\n"))
            elif line[0:17] == "User 1 End Time: ":
                user_one_class_info.append(line[17:].strip("\n"))
            elif line[0:21] == "User 1 Credit Hours: ":
                user_one_class_info.append(line[21:].strip("\n"))
            elif line[0:4] == "User" and user_one_major != "" and user_two_major == "":
                user_two_major = line
            elif user_one_major != "" and user_two_major != "" and line[0:4] != "User":
                user_two_class.append(line)
            elif line[0:19] == "User 2 Start Time: ":
                user_two_class_info.append(line[19:].strip("\n"))
            elif line[0:17] == "User 2 End Time: ":
                user_two_class_info.append(line[17:].strip("\n"))
            elif line[0:21] == "User 2 Credit Hours: ":
                user_two_class_info.append(line[21:].strip("\n"))
    curr_file.close()
    temp = edit_class(user_one_class, user_two_class)
    user_one_class = temp[0]
    user_two_class = temp[1]
    return_val = [user_one_class, user_two_class,
    user_one_major, user_two_major,
    user_one_class_info, user_two_class_info]
    return return_val

def edit_class(user_one_class, user_two_class):
    for curr in user_one_class:
        curr = curr[:len(curr) - 1]
    for curr in (user_two_class):
        curr = curr[:len(curr) - 1]
    answer = [user_one_class, user_two_class]
    return answer

def helper_fun_two(para):
    """Cut Down on Branches"""
    user_one_class = para[0]
    user_one_major = para[1]
    temp_one = para[2]
    temp_two = para[3]
    user_two_class = para[4]
    user_two_major = para[5]
    store_one = pd.DataFrame()
    store_two = pd.DataFrame()
    for curr in remaining_classes(user_one_class, user_one_major):
        curr_df = temp_one.loc[temp_two["Subject and Number"] == curr]
        frames = [store_one, curr_df]
        store_one = pd.concat(frames)

    for curr in remaining_classes(user_two_class, user_two_major):
        curr_df = temp_two.loc[temp_two["Subject and Number"] ==  curr]
        frames = [store_two, curr_df]
        store_two = pd.concat(frames)
    rem = pd.concat([store_one, store_two], ignore_index=True)
    return rem

@app.route('/finaldisplay', methods=["POST", "GET"])
def loadpage():
    '''Load last page'''
    json = [
        ["123", "CS222", "9AM", "10AM"],
        ["222", "CS225", "1PM", "3PM"]
    ]
    print(json)
    return render_template("finaldisplay.html", json_file = json)
