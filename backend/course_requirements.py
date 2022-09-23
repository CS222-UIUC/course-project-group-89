"'this module is to find common course requirements of two different majors'"
import pandas as pd

# Individual DataFrames per major
df_cs = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "MATH241", "MATH257",
"CS210", "CS211", "CS222", "CS225", "CS233", "CS341", "CS357", "CS361", "CS374", "CS421"]},)
df_cs_stats = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "CS222", "CS225",
"MATH241", "CS233", "CS341", "CS340",  "CS357", "MATH257", "MATH415", "MATH416", "CS374",
"CS421", "STAT107", "STAT200", "STAT212", "STAT400", "STAT410", "STAT425", "STAT426"]})
df_cs_astronomy = pd.DataFrame({"technical requirements" : ["CS124", "CS128", "CS173", "CS222",
"CS225",  "CS233", "CS341", "CS340", "STAT200", "STAT212", "CS361", "CS374", "CS421", "MATH221",
"MATH220", "MATH225", "MATH257", "MATH231", "PHYS211", "PHYS212", "MATH241",
"ASTR210", "ASTR310", "ASTR404", "ASTR405", "ASTR406", "ASTR414"]})

# Takes in 2 majors. Returns Courses in Both (Alphabetized A->Z)
def merge(major1, major2):
    "'Merge() returns common courses given 2 pandas dataframes'"
    common = pd.merge(major1, major2, how="inner").sort_values(by="technical requirements")
    return common
