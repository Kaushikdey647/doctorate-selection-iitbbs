import os
import pandas as pd
import pandasgui as pdgui
import numpy as np
import matplotlib.pyplot as plt

student_data = {
    "bio": pd.read_csv("bio.csv"),
    "net": pd.read_csv("net.csv"),
    "gate": pd.read_csv("gate.csv"),
    "tenth": pd.read_csv("tenth.csv"),
    "others": pd.read_csv("others.csv"),
    "masters": pd.read_csv("masters.csv"),
    "plustwo": pd.read_csv("plustwo.csv"),
    "bachelors": pd.read_csv("bachelors.csv"),
    "experience": pd.read_csv("experience.csv"),
}

global reason

reason = pd.DataFrame(columns = ['ReasonID', 'ReasonDesc','Qualified'])
for i in range(49):
    reason.loc[i] = [i,"NA","NA"]

"""
Avoids NaN by creating different alternatives, good for everyone,
keep adding as you see fit
"""

for key in student_data.keys():
    if "Institute" in student_data[key].keys():
        student_data[key]["Institute"].fillna("NA",inplace=True) #Replace all NaN values with "NA"
    if "Programme" in student_data[key].keys():
        student_data[key]["Programme"].fillna("NA",inplace=True) #Replace all NaN values with "NA"
    if "Specialization" in student_data[key].keys():
        student_data[key]["Specialization"].fillna("NA",inplace=True) #Replace all NaN values with "NA"
    if "Discipline" in student_data[key].keys():
        student_data[key]["Discipline"].fillna("NA",inplace=True) #Replace all NaN values with "NA"
    if "Percentage" in student_data[key].keys():
            student_data[key]["Percentage"].fillna(10*(student_data[key]["CGPA"]-1) + 5,inplace=True) #Replace all NaN values with "NA"

def checkIIT(Data,CGPCri):
    """
    This Function checks for IITians, just a query check that's all
    SHORTLISTING IIT CANDIDATES WITH COOL CG
    """
    mylist =[]
    for i,row in Data.iterrows():
        
        if(
            "iit" in row["Institute"].lower() or
            "indian institute of technology" in row["Institute"].lower()
        ):
            if (
                np.isnan(row["CGPA"]) or
                row["CGPA"] < CGPCri
            ):
                continue
            else:
                mylist.append(i)
                reason = Reason(reason,i,5)
    return mylist #Return list of indices

def Reason(i,id):
    """
    The Function takes in id for reason and puts it in reason csv file
    ID For Reason Are:
    0: Qualified via GATE
    1: Not Enough 10/+2 Score
    2: Not Enough GATE Score
    3: Didn't Qualify GATE
    4: Qualified via NET-UGC
    5: Qualified as Graduates/Masters of IIT
    NET-UGC and Graduate/Post-Grad in IIT are considered Exceptions
    and not fullfilling these cannot be listed as reason
    """
    reason.loc[i]["ReasonID"] = id
    
    if id == 0:
        reason.loc[i]["ReasonDesc"] = "Qualified via GATE"
        reason.loc[i]["Qualified"] = 1
    elif id == 1:
        reason.loc[i]["ReasonDesc"] = "Not Enough 10/+2 Score"
        reason.loc[i]["Qualified"] = 0
    elif id == 2:
        reason.loc[i]["ReasonDesc"] = "Not Enough GATE Score"
        reason.loc[i]["Qualified"] = 0
    elif id == 3:
        reason.loc[i]["ReasonDesc"] = "Didn't Qualify GATE"
        reason.loc[i]["Qualified"] = 0
    elif id == 4:
        reason.loc[i]["ReasonDesc"] = "Qualified via NET-UGC"
        reason.loc[i]["Qualified"] = 1
    elif id == 5:
        reason.loc[i]["ReasonDesc"] = "Qualified as Graduates/Masters of IIT"
        reason.loc[i]["Qualified"] = 1
    elif id == 6:
        reason.loc[i]["ReasonDesc"] = "Not Enough Bachelors Score"
        reason.loc[i]["Qualified"] = 0
    elif id == 7:
        reason.loc[i]["ReasonDesc"] = "Not Enough Masters Score"
        reason.loc[i]["Qualified"] = 0
    else:
        reason.loc[i]["ReasonDesc"] = "NA"
        reason.loc[i]["Qualified"] = 0

def checkNET(Data):
    global reason
    """
    This function Checks for NET-UGC Qualification
    """
    global reason
    mylist = []
    for i,row in Data.iterrows():
        if row["Discipline"] != "NA":
            mylist.append(i)
            Reason(i,4)
    return mylist

def checkGATE(MyDict):
    """
    This function checks for GATE Qualification
    if gate qualified, check masters
    if masters yes, exec masters block
    else exec bachelors block

    All CGPA have been converted to percentage if not present
    so all evaluations will be done on basis of percentage only
    """
    global reason
    selected = True #Arbitrary var to hold selection logic,
                    #Helps avoid loops and stuff
    cutoff = 0 #Gate Marks
    perc = 0 #Percentage
    category = "GEN" #Default
    mylist = []
    for i,row in MyDict["gate"].iterrows():
        if row["Discipline"] != "NA":
            if row["Score"] > 302: #Least qualifying score possible
                selected = True
            else:
                Reason(i,2) #2: Not Enough Gate Score
                selected = False
                continue    #Eliminate some BS by skipping beforehand
        else:
            Reason(i,3) #3: Didnt qualify gate
            selected = False
            continue
        if MyDict["masters"].iloc[i]["Programme"] == "NA":
            #Btech Part
            cutoff = 500
            perc = 70
            category =  MyDict["bio"].iloc[i]["Category"]
            #category relaxations
            if category == "OBC":
                cutoff = 0.9 * cutoff
            elif category in ["SC","ST","PWD"]:
                cutoff = 0.67 * cutoff
                perc = perc - 5
            #GATE Filtering
            if row["Score"] < cutoff:
                #Check GATE Score
                Reason(i,2) #2: Not enough gate score
                selected = False
                continue
            # Boards Filtering with single relaxation
            if (
                (MyDict["tenth"].iloc[i]["Percentage"] < perc or MyDict["plustwo"].iloc[i]["Percentage"] < perc - 10) or
                (MyDict["tenth"].iloc[i]["Percentage"] < perc - 10 or MyDict["plustwo"].iloc[i]["Percentage"] < perc)
            ):
                Reason(i,1) #1: Not qualified via +2/10 score
                selected = False
                continue
            # Bachelors Filtering
            if MyDict["bachelors"].iloc[i]["Percentage"] < perc:
                Reason(i,6) #6: Not enough bachelor score
                selected = False
                continue

        else:
            #Mtech Part
            cutoff = 450
            perc = 60
            relax = 10
            category =  MyDict["bio"].iloc[i]["Category"]
            #category relaxations
            if category == "OBC":
                cutoff = 0.9 * cutoff
            elif category in ["SC","ST","PWD"]:
                relax = 5
                cutoff = 0.67 * cutoff
                perc = perc - 5
            #GATE Filtering
            if row["Score"] < cutoff:
                #Check GATE Score
                Reason(i,2) #2: Not enough gate score
                selected = False
                continue
            # Boards Filtering with single relaxation
            if (
                (MyDict["tenth"].iloc[i]["Percentage"] < perc or MyDict["plustwo"].iloc[i]["Percentage"] < perc - relax) or
                (MyDict["tenth"].iloc[i]["Percentage"] < perc - relax or MyDict["plustwo"].iloc[i]["Percentage"] < perc)
            ):
                Reason(i,1) #1: Not qualified via +2/10 score
                selected = False
                continue
            # Bachelors Filtering
            if MyDict["bachelors"].iloc[i]["Percentage"] < perc:
                Reason(i,6) #6: Not enough bachelor score
                selected = False
                continue
            if MyDict["masters"].iloc[i]["Percentage"] < perc:
                Reason(i,7) #6: Not enough master score
                selected = False
                continue
        if selected:
            Reason(i,0) #0: Qualified Via GATE
            mylist.append(i)
    return mylist


def appendShortlisted(SourceDict,ShortList):
    """
    Appends Shortlisted Rows onto dict
    Takes element of id present in ShortList present in SourceDict
    and Puts it in TargetDict
    """
    TargetDict = {}
    for key in SourceDict.keys():
        TargetDict[key] = pd.DataFrame(columns = SourceDict[key].columns.tolist()) #copy column headers
        for i in ShortList:
            TargetDict[key] = TargetDict[key].append( SourceDict[key].iloc[i] )
    return TargetDict

""" 

THIS IS THE FUNCTION INVOKING BLOCK, WE JUST RANDOMLY INVOKE FUNCTIONS AND HAVE FUN

"""

selectGATE = checkGATE(student_data)
BTechIIT = checkIIT(student_data["bachelors"],8.0)
MTechIIT = checkIIT(student_data["masters"],8.5)
selectNET = checkNET(student_data["net"])

finalList = list(
    set(selectGATE) | set(BTechIIT) | set(MTechIIT) | set(selectNET)
)

print("ID of Finalists : ",finalList)

finalDF = appendShortlisted(student_data,finalList)

OutputDf = pd.concat([
    student_data["bio"]["Category"],
    student_data["tenth"].rename({"Percentage":"Tenth"},axis=1),
    student_data["plustwo"].rename({"Percentage":"Plustwo"},axis=1),
    student_data["bachelors"].rename({"Percentage":"Bachelors"},axis=1),
    student_data["masters"].rename({"Percentage":"Masters"},axis=1),
],axis=0)

OutputDf = pd.DataFrame(
    {
        "Category" : student_data["bio"]["Category"],
        "Tenth" : student_data["tenth"]["Percentage"],
        "+2" : student_data["plustwo"]["Percentage"],
        "Bachelors" : student_data["bachelors"]["Percentage"],
        "Masters" : student_data["masters"]["Percentage"],
        "UGC NET" : student_data["net"]["Discipline"],
        "GATE" : student_data["gate"]["Score"],
        "Qualified": reason["Qualified"],
        "Reason": reason["ReasonDesc"]
    }
)

OutputDf.to_csv(r'output.csv')
pdgui.show(OutputDf)
OutputDf