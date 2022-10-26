"'this module is to find common course requirements of two different majors'"
import pandas as pd

# Individual DataFrames per major
df_cs_ggis = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "CS222",
"CS225","CS211", "CS233", "CS341", "CS340", "CS374", "CS421", "MATH231", "MATH257", "STAT200",
"STAT212", "CS361", "GGIS371", "GGIS379", "GGIS380"]})
df_cs_stats = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "CS222", "CS225",
"MATH241", "MATH231", "CS233", "CS341", "CS340",  "CS357", "MATH257", "MATH415", "MATH416", "CS374",
"CS421", "STAT107", "STAT200", "STAT212", "STAT400", "STAT410", "STAT425", "STAT426"]})
df_cs_astronomy = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "CS222",
"CS225",  "CS233", "CS341", "CS340", "STAT200", "STAT212", "CS361", "CS374", "CS421", "MATH221",
"MATH220", "MATH225", "MATH257", "MATH231", "PHYS211", "PHYS212", "MATH241",
"ASTR210", "ASTR310", "ASTR404", "ASTR405", "ASTR406", "ASTR414"]})
df_cs = pd.DataFrame({"technical requirements" : ["CS 124", "CS 128", "CS 173", "MATH 241",
"MATH 257", "CS 210", "CS 211", "CS 222", "CS 225", "CS 233",
"CS 341", "CS 357", "CS 361", "CS 374", "CS 421"]})

# Takes in 2 majors. Returns Courses in Both (Alphabetized A->Z)
def merge(major1, major2):
    "'Merge() returns common courses given 2 pandas dataframes'"
    common = pd.merge(major1, major2, how="inner").sort_values(by="technical requirements")
    return common
