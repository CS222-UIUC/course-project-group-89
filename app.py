'''this module renders a template and has two functions (testing for emily 10/1/22)'''
from flask import Flask, render_template, request

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
    cs_req = ["CS + GGIS", "CS + ASTRO", "Stats & CS", "CS"]
    return render_template('index.html', cs_req=cs_req)

@app.route('/major', methods=["POST"])
def main():
    "'This recives the major from dropdown and stores it in txt file'"
    major = request.form["major"]
    print("in main(), major: ", major)
    with open("store_user_input.txt", "w+", encoding="utf8") as curr_file:
        curr_file.write(f'User 1: {major}')
        curr_file.write("\n")
    curr_file.close()
    return render_template("index.html")

@app.route('/class', methods=["GET"])
def checkboxes():
    "'Based on major stores in txt file, send a list of classes to the front end'"
    major = ""
    with open("store_user_input.txt", "r", encoding="utf8") as curr_file:
        major = curr_file.readline().rstrip()
    cs_req = []
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "Stats & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("class.html", cs_req= cs_req)

@app.route('/class', methods=["POST"])
def store_classes():
    "'Based on checkboxes selected from checkboxes(), store the classes in txt'"
    user_classes = request.values.getlist('user_classes')
    print(user_classes)
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for item in user_classes:
            curr_file.write(f'{item}\n')
        # curr_file.write("\n")
    curr_file.close()
    return class_info_main()

@app.route('/classinfo', methods=["GET"])
def class_info_main():
    """Send the options for start and end time and # of credit hrs"""
    time_range = ["8 am", "9 am", "10 am", "11 am", "12 pm",
    "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm"]

    credit_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18]

    return render_template('classinfo.html', time_range=time_range, credit_hours = credit_hours)

@app.route('/classinfo', methods=["POST"])
def store_class_info():
    """Store User 1 info for start, end, and # of credit hrs"""
    # user_classes = request.values.getlist('user_classes')
    # with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
    #     for item in user_classes:
    #         curr_file.write("%s\n" % item)
    #     curr_file.write("\n")
    # curr_file.close()
    return render_template('classinfo.html')

@app.route('/friendmajor', methods=["GET"])
def friendmajor():
    """Sends List of Majors to Frontend for User 2"""
    cs_req = ["CS + GGIS", "CS + ASTRO", "Stats & CS", "CS"]
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
    cs_req = []
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "Stats & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("friendclass.html", cs_req = cs_req)

@app.route('/friendclass', methods=["POST"])
def storefriendclasses():
    """Store User 2's classes taken"""
    friend_classes = request.values.getlist('seconduserclass')
    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        for item in friend_classes:
            curr_file.write(f'{item}\n')
        # curr_file.write("\n")
    curr_file.close()
    return friend_class_info_main()

@app.route('/friendclassinfo', methods=["GET"])
def friend_class_info_main():
    """Send User 2's class option to frontend"""
    time_range = ["8 am", "9 am", "10 am", "11 am", "12 pm",
    "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm"]

    credit_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18]

    return render_template('friendclassinfo.html',
    time_range=time_range, credit_hours = credit_hours)


@app.route('/friendclassinfo', methods=["POST"])
def store_friends_class_info():
    """Store User 2's class info"""
    # friend_classes = request.values.getlist('user_classes')
    # print("in main(), POST, friend_classes: ", friend_classes)
    # with open("store_user_input.txt", "w+", encoding="utf8") as curr_file:
    #     curr_file.write(friend_classes)
    #     curr_file.write("\n")
    # curr_file.close()
    return choose_classes()


@app.route('/classestotake', methods=["GET"])
def choose_classes():
    """Print out the classes User 1 and 2 can take together"""
    user_one_class = []
    user_two_class = []
    user_one_major = ""
    user_two_major = ""
    with open('store_user_input.txt', encoding="utf8") as curr_file:
        line = None
        for line in curr_file:
            if line[0:4] == "User" and user_one_major == "":
                user_one_major = line
            elif user_one_major != "" and user_two_major == "" and line[0:4] != "User":
                user_one_class.append(line)
            elif line[0:4] == "User" and user_one_major != "" and user_two_major == "":
                user_two_major = line
            elif user_one_major != "" and user_two_major != "" and line[0:4] != "User":
                user_two_class.append(line)

    curr_file.close()
    for curr in user_one_class:
        curr= curr[:len(curr) - 1]
    for curr in (user_two_class):
        curr = curr[:len(curr) - 1]
    return render_template("classestotake.html", cs_req= [])

@app.route('/finaldisplay', methods=["POST", "GET"])
def loadpage():
    '''Load last page'''
    json = [
        ["123", "CS222", "9am", "10am"],
        ["222", "CS225", "1pm", "3pm"]
    ]
    print(json)
    return render_template("finaldisplay.html", json_file = json)
