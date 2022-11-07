"'this module is to find common course requirements of two different majors'"
import pandas as pd

# Individual DataFrames per major
df_cs_ggis = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "CS 222",
"CS 225","CS 211", "CS 233", "CS 341", "CS 340", "CS 374", "CS 421", "MATH 231", "MATH 257",
"STAT 200","STAT 212", "CS 361", "GGIS 371", "GGIS 379", "GGIS 380"]})
df_cs_stats = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "CS 222",
"CS 225","MATH 241", "MATH 231", "CS 233", "CS 341", "CS 340",  "CS 357", "MATH 257", "MATH 415",
"MATH 416", "CS 374","CS 421", "STAT 107", "STAT 200", "STAT 212", "STAT 400", "STAT 410",
"STAT 425", "STAT 426"]})
df_cs_math = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "CS 222",
"CS 225","CS 233", "CS 341", "CS 340",  "CS 357", "CS 374", "CS 421", "CS 450",
"MATH 220", "MATH 231","MATH 241", "MATH 257", "MATH 416",]})
df_cs_astronomy = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "CS 222",
"CS 225",  "CS 233", "CS 341", "CS 340", "STAT 200", "STAT 212", "CS 361", "CS 374", "CS 421",
"MATH 221","MATH 220", "MATH 225", "MATH 257", "MATH 231", "PHYS 211", "PHYS 212", "MATH 241",
"ASTR 210", "ASTR 310", "ASTR 404", "ASTR4 05", "ASTR 406", "ASTR 414"]})
df_cs = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "MATH 241",
"MATH 257", "CS 210", "CS 211", "CS 222", "CS 225", "CS 233",
"CS 341", "CS 357", "CS 361", "CS 374", "CS 421"]})
df_gen_ed = pd.DataFrame

# Takes in 2 majors. Returns Courses in Both (Alphabetized A->Z)
def merge(major1, major2):
    "'Merge() returns common courses given 2 pandas dataframes'"
    common = pd.merge(major1, major2, how="inner").sort_values(by="technical requirements")
    return common
