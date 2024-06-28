#!/bin/python

# Imports
import random
import math

# Starting variables (only change these once and once only)!
global startingDay
global startingMonth
global startingYear
startingDay = 1
startingMonth = "needfest"
startingYear = 576

# DELETE THESE
global currentmonth
global currentday
global terrain
global latitude
global sylvanPrompt

# Special variables
global debug
global verbose
global convertFBool
global convertAMPM
global customTweaks
debug = True
verbose = True
convertFBool = True
convertAMPM = False
customTweaks = True

# Global lists
global dayNameList
global monthsAll
global months
global festivals
global lunaList
global celeneList
dayNameList = [["freeday", "rest"], ["starday", "work"],["sunday", "work"], ["moonday", "work"], ["godsday", "worship"], ["waterday", "work"], ["earthday", "work"]]
monthsAll = ("needfest", "fireseek", "readying", "coldeven", "growfest", "planting", "flocktime", "wealsun", "richfest", "reaping", "good-month", "harvester", "brewfest", "patchwall", "ready'reat", "sunsebb")
months = ("fireseek", "readying", "coldeven", "planting", "flocktime", "wealsun", "reaping", "good-month", "harvester", "patchwall", "ready'reat", "sunsebb")
festivals = ("needfest", "growfest", "richfest", "brewfest")
terrainTypes = ("rough terrain", "hills", "forest", "jungle", "swamp", "marsh", "dust", "plains", "desert", "mountains", "seacoast", "sea")

## Important functions start here
## This function converts farenheit to celsius
def tempConvert(farenheit):
    if convertFBool == True:
        return str(round((farenheit-32)*5/9,1))+u'\N{DEGREE SIGN}'+'C'
    else:
        return str(farenheit)+u'\N{DEGREE SIGN}'+'F'
## This function converts between 24 hour or 12 hour format.
def hourConvert(hour):
    if convertAMPM:
        if hour < 12:
            hour += 1
            return str(hour)+":00 AM"
        else:
            hour -= 11
            return str(hour)+":00 PM"
    else:
        return str(hour).zfill(2)+":00"
# This function allows us to structure dice rolls as (x)d(y)
def dice(rolls, die):
    rollSeq = []
    while int(rolls) > 0:
        rollSeq.append(random.randint(1,die))
        rolls -= 1
    return sum(rollSeq)
##################
## DICTIONARIES ##
##################
## BASELINE VALUES ##
baseline = {
    "fireseek": {
        "base-temp": 32,
        "daily-high": lambda: random.randint(1, 10),
        "daily-low": lambda: random.randint(1, 20)-21,
        "clear-upper": 23,
        "cloud-part-lower": 24,
        "cloud-part-upper": 50,
        "cloudy-lower": 51,
        "precip": 46,
        "sunrise": "7:21",
        "sunset": "17:01"
    },
    "readying": {
        "base-temp": 34,
        "daily-high": lambda: random.randint(1, 6)+4,
        "daily-low": lambda: random.randint(1, 10)-15,
        "clear-upper": 25,
        "cloud-part-lower": 26,
        "cloud-part-upper": 50,
        "cloudy-lower": 51,
        "precip": 40,
        "sunrise": "6:55",
        "sunset": "17:36"
    },
    "coldeven": {
        "base-temp": 42,
        "daily-high": lambda: random.randint(1, 8)+4,
        "daily-low": lambda: random.randint(1, 10)-15,
        "clear-upper": 27,
        "cloud-part-lower": 28,
        "cloud-part-upper": 54,
        "cloudy-lower": 55,
        "precip": 44,
        "sunrise": "6:12",
        "sunset": "18:09"
    },
    "planting": {
        "base-temp": 52,
        "daily-high": lambda: random.randint(1, 10)+6,
        "daily-low": lambda: random.randint(1, 8)-13,
        "clear-upper": 20,
        "cloud-part-lower": 21,
        "cloud-part-upper": 55,
        "cloudy-lower": 56,
        "precip": 42,
        "sunrise": "5:24",
        "sunset": "18:39"
    },
    "flocktime": {
        "base-temp": 63,
        "daily-high": lambda: random.randint(1, 10)+6,
        "daily-low": lambda: random.randint(1, 10)-17,
        "clear-upper": 20,
        "cloud-part-lower": 21,
        "cloud-part-upper": 53,
        "cloudy-lower": 54,
        "precip": 42,
        "sunrise": "4:45",
        "sunset": "19:10"
    },
    "wealsun": {
        "base-temp": 71,
        "daily-high": lambda: random.randint(1, 8)+8,
        "daily-low": lambda: random.randint(1, 6)-13,
        "clear-upper": 20,
        "cloud-part-lower": 21,
        "cloud-part-upper": 60,
        "cloudy-lower": 61,
        "precip": 36,
        "sunrise": "4:32",
        "sunset": "19:32"
    },
    "reaping": {
        "base-temp": 77,
        "daily-high": lambda: random.randint(1, 6)+4,
        "daily-low": lambda: random.randint(1, 6)-13,
        "clear-upper": 22,
        "cloud-part-lower": 23,
        "cloud-part-upper": 62,
        "cloudy-lower": 63,
        "precip": 33,
        "sunrise": "4:45",
        "sunset": "19:29"
    },
    "good-month": {
        "base-temp": 75,
        "daily-high": lambda: random.randint(1, 4)+6,
        "daily-low": lambda: random.randint(1, 6)-13,
        "clear-upper": 25,
        "cloud-part-lower": 26,
        "cloud-part-upper": 60,
        "cloudy-lower": 61,
        "precip": 33,
        "sunrise": "5:13",
        "sunset": "18:57"
    },
    "harvester": {
        "base-temp": 68,
        "daily-high": lambda: random.randint(1, 8)+6,
        "daily-low": lambda: random.randint(1, 8)-15,
        "clear-upper": 33,
        "cloud-part-lower": 34,
        "cloud-part-upper": 54,
        "cloudy-lower": 55,
        "precip": 33,
        "sunrise": "5:42",
        "sunset": "18:10"
    },
    "patchwall": {
        "base-temp": 57,
        "daily-high": lambda: random.randint(1, 10)+5,
        "daily-low": lambda: random.randint(1, 10)-16,
        "clear-upper": 35,
        "cloud-part-lower": 36,
        "cloud-part-upper": 60,
        "cloudy-lower": 61,
        "precip": 36,
        "sunrise": "6:12",
        "sunset": "17:21"
    },
    "ready'reat": {
        "base-temp": 46,
        "daily-high": lambda: random.randint(1, 10)+6,
        "daily-low": lambda: random.randint(1, 10)-15,
        "clear-upper": 20,
        "cloud-part-lower": 21,
        "cloud-part-upper": 50,
        "cloudy-lower": 51,
        "precip": 40,
        "sunrise": "6:46",
        "sunset": "16:45"
    },
    "sunsebb": {
        "base-temp": 33,
        "daily-high": lambda: random.randint(1, 8)+5,
        "daily-low": lambda: random.randint(1, 20)-21,
        "clear-upper": 25,
        "cloud-part-lower": 26,
        "cloud-part-upper": 50,
        "cloudy-lower": 51,
        "precip": 43,
        "sunrise": "7:19",
        "sunset": "16:36"
    }
}
## TERRAINS ##
terraindict = {
    "hills": {
        "precip-mod": 0,
        "temp-mod": 0,
        "wind-mod": lambda: random.randint(0, 10)-5
    },
    "forest": {
        "precip-mod": 0,
        "temp-mod": -5,
        "wind-mod": -5
    },
    "jungle": {
        "precip-mod": 10,
        "temp-mod": 5,
        "wind-mod": -10
    },
    "swamp": {
        "precip-mod": 5,
        "temp-mod": 5,
        "wind-mod": -5
    },
    "dust": {
        "precip-mod": -25,
        "temp-mod": [10, -10],
        "wind-mod": 0
    },
    "plains": {
        "precip-mod": 0,
        "temp-mod": 0,
        "wind-mod": 5
    },
    "desert": {
        "precip-mod": -30,
        "temp-mod": [10, -10],
        "wind-mod": 5
    },
    "mountains": {
        "precip-mod": 0,
        "temp-mod": 0,
        "wind-mod": 5
    },
    "seacoast": {
        "precip-mod": 5,
        "temp-mod": [5, -5],
        "wind-mod": 5
    },
    "sea": {
        "precip-mod": 15,
        "temp-mod": [5, -10],
        "wind-mod": 10
    }
}
## PRECIPITATION ##
weatherdict = {
    "heavy blizzard": {
        "amount": lambda: dice(2,10)+10,
        "duration": lambda: dice(3,8),
        "wind": lambda: dice(6,8)+40,
        "mintemp": None,
        "maxtemp": 10,
        "continue": 5,
        "rainbow": 0
    },
    "blizzard": {
        "amount": lambda: dice(2,8)+8,
        "duration": lambda: dice(3,10),
        "wind": lambda: dice(3,8)+36,
        "mintemp": None,
        "maxtemp": 20,
        "continue": 10,
        "rainbow": 0
    },
    "heavy snowstorm": {
        "amount": lambda: dice(2,8)+2,
        "duration": lambda: dice(4,6),
        "wind": lambda: dice(3,10),
        "mintemp": None,
        "maxtemp": 25,
        "continue": 20,
        "rainbow": 0
    },
    "light snowstorm": {
        "amount": lambda: dice(1,8),
        "duration": lambda: dice(2,6),
        "wind": lambda: dice(4,6),
        "mintemp": None,
        "maxtemp": 35,
        "continue": 25,
        "rainbow": 1
    },
    "sleetstorm": {
        "amount": lambda: dice(1,2),
        "duration": lambda: dice(1,6),
        "wind": lambda: dice(3,10),
        "mintemp": None,
        "maxtemp": 35,
        "continue": 20,
        "rainbow": 0
    },
    "hailstorm": {
        "amount": lambda: dice(1,2),
        "duration": lambda: dice(1,4),
        "wind": lambda: dice(4,10),
        "mintemp": None,
        "maxtemp": 65,
        "continue": 10,
        "rainbow": 0
    },
    "heavy fog": {
        "amount": 0,
        "duration": lambda: dice(1,12),
        "wind": lambda: dice(1,20),
        "mintemp": 20,
        "maxtemp": 60,
        "continue": 25,
        "rainbow": 1
    },
    "light fog": {
        "amount": 0,
        "duration": lambda: dice(2,4),
        "wind": lambda: dice(1,10),
        "mintemp": 30,
        "maxtemp": 70,
        "continue": 30,
        "rainbow": 3
    },
    "mist": {
        "amount": 0,
        "duration": lambda: dice(2,6),
        "wind": lambda: dice(1,10),
        "mintemp": 30,
        "maxtemp": None,
        "continue": 15,
        "rainbow": 10
    },
    "drizzle": {
        "amount": lambda: dice(1,4)/4,
        "duration": lambda: dice(1,10),
        "wind": lambda: dice(1,20),
        "mintemp": 25,
        "maxtemp": None,
        "continue": 20,
        "rainbow": 5
    },
    "light rainstorm": {
        "amount": lambda: dice(1,3),
        "duration": lambda: dice(1,12),
        "wind": lambda: dice(1,20),
        "mintemp": 25,
        "maxtemp": None,
        "continue": 45,
        "rainbow": 15
    },
    "heavy rainstorm": {
        "amount": lambda: dice(1,4)+3,
        "duration": lambda: dice(1,12),
        "wind": lambda: dice(2,12)+10,
        "mintemp": 25,
        "maxtemp": None,
        "continue": 30,
        "rainbow": 20
    },
    "thunderstorm": {
        "amount": lambda: dice(1,8),
        "duration": lambda: dice(1,4),
        "wind": lambda: dice(4,10),
        "mintemp": 30,
        "maxtemp": None,
        "continue": 15,
        "rainbow": 20
    },
    "tropical storm": {
        "amount": lambda: dice(1,6),
        "duration": lambda: (dice(1,6)*24)//3,
        "wind": lambda: dice(3,12)+30,
        "mintemp": 40,
        "maxtemp": None,
        "continue": 20,
        "rainbow": 10
    },
    "monsoon": {
        "amount": lambda: dice(1,8),
        "duration": lambda: (dice(1,6)+6)*24,
        "wind": lambda: dice(6,10),
        "mintemp": 55,
        "maxtemp": None,
        "continue": 30,
        "rainbow": 5
    },
    "gale": {
        "amount": lambda: dice(1,8),
        "duration": lambda: (dice(1,6)*24)//2,
        "wind": lambda: dice(6,8)+40,
        "mintemp": 40,
        "maxtemp": None,
        "continue": 15,
        "rainbow": 10
    },
    "hurricane": {
        "amount": lambda: dice(1,10),
        "duration": lambda: (dice(1,8))//2,
        "wind": lambda: dice(7,10)+70,
        "mintemp": 55,
        "maxtemp": None,
        "continue": 20,
        "rainbow": 5
    },
    "special": {
        "continue": 1
    }
}
## SPECIAL PRECIPITATION ##
specialweatherdict = {
    "sand or dust storm": {
        "precipitation": None,
        "duration": lambda: dice(1,8),
        "movement": False,
        "vision": False,
        "ultra-vision": False,
        "tracking": True,
        "lost-risk": 80,
        "speed": lambda: dice(5,10)
        },
    "windstorm": {
        "precipitation": None,
        "duration": lambda: dice(1,10),
        "movement": 50,
        "vision": 50,
        "ultra-vision": 75,
        "tracking": True,
        "lost-risk": 30,
        "speed": lambda: dice(8,10)+20
        },
    "earthquake": {
        "precipitation": None,
        "duration": lambda: random.randint(1,10),
        "movement": 25,
        "vision": True,
        "ultra-vision": True,
        "tracking": 50,
        "lost-risk": 10,
        "speed": lambda: random.randint(1,20)
        },
    "avalanche": {
        "precipitation": lambda: dice(5,10),
        "duration": lambda: random.randint(1,10)/60,
        "movement": False,
        "vision": True,
        "ultra-vision": True,
        "tracking": 40,
        "lost-risk": 10,
        "speed": lambda: random.randint(1,10)
        },
    "volcano": {
        "precipitation": lambda: random.randint(1,8),
        "duration": lambda: (dice(1, 20)*24)//2,
        "movement": 50,
        "vision": 75,
        "ultra-vision": 50,
        "tracking": 50,
        "lost-risk": 20,
        "speed": lambda: random.randint(1, 20)
        },
    "tsunami": {
        "precipitation": lambda: dice(10,20),
        "duration": lambda: random.randint(1,2),
        "movement": True,
        "vision": True,
        "ultra-vision": True,
        "tracking": True,
        "lost-risk": None,
        "speed": lambda: dice(5,10)+10
        },
    "quicksand": {
        "precipitation": None,
        "duration": None,
        "area": lambda: random.randint(1,20),
        "movement": False,
        "vision": True,
        "ultra-vision": True,
        "tracking": True,
        "lost-risk": None,
        "speed": lambda: random.randint(1,20)
        },
    "flash flood": {
        "precipitation": None,
        "duration": lambda: random.randint(1,6)+2,
        "movement": 75,
        "vision": True,
        "ultra-vision": True,
        "tracking": None,
        "lost-risk": 10,
        "speed": lambda: random.randint(1,20)
        },
    "rain forest downpour": {
        "precipitation": 1,
        "duration": lambda: dice(3,4),
        "movement": 50,
        "vision": 75,
        "ultra-vision": 75,
        "tracking": None,
        "lost-risk": 20,
        "speed": lambda: random.randint(0,5)
        },
    "sun shower": {
        "precipitation": 0.5,
        "duration": lambda: random.randint(1,10)/10,
        "movement": True,
        "vision": True,
        "ultra-vision": True,
        "tracking": True,
        "lost-risk": False,
        "speed": lambda: random.randint(1,20)
        },
    "tornado or cyclone": {
        "precipitation": 1,
        "duration": lambda: random.randint(5,50),
        "movement": True,
        "vision": 75,
        "ultra-vision": 75,
        "tracking": False,
        "lost-risk": 40,
        "speed": 300
        },
    "oasis or mirage oasis": {
        "precipitation": None,
        "duration": None,
        "movement": True,
        "vision": True,
        "ultra-vision": True,
        "tracking": True,
        "lost-risk": False,
        "speed": lambda: random.randint(1,20)
        }
}
##################################
## REGULAR FUNCTIONS START HERE ##
##################################
## CLEAR SKY MODIFICATION
## This is a custom function outside of the ruleset meant to make cloudy days colder and clear days warmer. The effect is mild though at at maximum of 13F/7C.
## At the northmost it should average 5F/2C and southmost it should average 9F/5C.
def clearSkyTempMod(skyState):
    if customTweaks == True:
        match skyState:
            case "clear": return dice(1,4)+2
            case "partially cloudy": return dice(1,2)+1
            case "cloudy": return 0
            case "overcast": return -dice(1,4)-4
    else:
        return 0
    raise Exception("Error in clearSkyTempMod function.")
## SEASON CHECK
## This just returns the season depending on the month it's fed.
def seasonCheck(thisMonth):
    if thisMonth == "sunsebb":
        return "early winter"
    elif thisMonth == "needfest":
        return "midwinter festival"
    elif thisMonth == "fireseek":
        return "late-winter"
    elif thisMonth == "readying":
        return "early spring"
    elif thisMonth == "coldeven":
        return "late spring"
    elif thisMonth == "growfest":
        return "midspring festival"
    elif thisMonth == "planting":
        return "early low summer"
    elif thisMonth == "flocktime":
        return "mid low summer"
    elif thisMonth == "wealsun":
        return "late low summer"
    elif thisMonth == "richfest":
        return "midsummer festival"
    elif thisMonth == "reaping":
        return "early high summer"
    elif thisMonth == "good-month":
        return "mid high summer"
    elif thisMonth == "harvester":
        return "late high summer"
    elif thisMonth == "brewfest":
        return "midautumn festival"
    elif thisMonth == "patchwall":
        return "early autumn"
    elif thisMonth == "ready'reat":
        return "late autumn"
    raise Exception("Something is wrong in seasonCheck function.")
## This function checks the neighbors of another month to map to the baseline dictionary. Accepts the month to be checked and (prev/next/this)
def monthNeighbor(thisMonth, neighbor, thisDay):
    match neighbor:
        case "next":
            if thisMonth == "sunsebb":
                return "fireseek"
            elif thisMonth in festivals:
                return monthsAll[monthsAll.index(thisMonth)+2]
            else:
                return months[months.index(thisMonth)+1]
        case "prev":
            if thisMonth == "needfest":
                return "sunsebb"
            elif thisMonth in festivals:
                return monthsAll[monthsAll.index(thisMonth)-2]
            else:
                return months[months.index(thisMonth)-1]
        case "this":
            if thisMonth in festivals:
                if thisDay > 4:
                    return months[monthsAll.index(thisMonth)+1]
                elif thisMonth == "needfest":
                    return "sunsebb"
                else:
                    return months[monthsAll.index(thisMonth)-1]
            else:
                return thisMonth
        case _:
            raise Exception("ERROR: Neighbor unrecoginzed")
    raise Exception("ERROR: End of function")
## This function is meant to calculate the month from days since startdate.
def monthDayCalc(dayCount):
    currentDay = startingDay-1 # GLOBAL
    currentMonth = startingMonth # GLOBAL
    currentYear = startingYear # GLOBAL
    moonPhaseLuna = round((math.cos(( currentDay - 18 ) * math.pi / 14 )+1)*50)
    moonPhaseCelene = round((math.cos((currentDay-4)*math.pi/45.5)+1)*50)
    moonPhase = str(moonPhaseLuna)+'%', str(moonPhaseCelene)+'%'
    while dayCount > 0:
        if currentMonth in festivals and currentDay > 7:
            currentMonth = monthsAll[monthsAll.index(currentMonth) + 1]
            currentDay -= 7
        elif currentMonth == "sunsebb" and currentDay > 28:
            currentYear += 1
            currentMonth = "needfest"
            currentDay -= 28
        elif currentMonth in months and currentDay > 28:
            currentMonth = monthsAll[monthsAll.index(currentMonth) + 1]
            currentDay -= 28
        currentDay += 1
        dayCount -= 1
    dayNameIndex = currentDay%7
    return currentDay, dayNameList[dayNameIndex], currentMonth, moonPhase, currentYear
print(monthDayCalc(1))
exit()
## Precipitation Check
## This is a simpler function that just returns whenever the day should have precipitation.
def precipCheck():
    precipTest = random.randint(1, 100)
    if sylvanPrompt == False:
        precipRisk = baseline[currentmonth]["precip"]+terraindict[terrain]["precip-mod"]
    elif sylvanPrompt == True: ## Sylvan forests have minimal precipitation risk.
        precipRisk = (baseline[currentmonth]["precip"]+terraindict[terrain]["precip-mod"])//4
    else:
        raise Exception("Error: sylvanPrompt returned unexpected variable, expected bool")
    if precipTest <= precipRisk:
        return True
    else:
        return False
## Precipitation Type
## Rolls a D100 and selects the precipitation from temperature values
## Not used anymore.
def precipTypeReverse(precipType, temperature):
    if precipType == "heavy blizzard":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "blizzard":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "heavy snowstorm":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "light snowstorm":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "sleetstorm":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "hailstorm":
        if temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "heavy fog":
        if temperature >= weatherdict[precipType]["mintemp"] and temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "light fog":
        if temperature >= weatherdict[precipType]["mintemp"] and temperature <= weatherdict[precipType]["maxtemp"]:
            return True
        else:
            return False
    elif precipType == "mist":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "drizzle":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "light rainstorm":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "heavy rainstorm":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "thunderstorm":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "tropical storm":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "monsoon":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "gale":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    elif precipType == "hurricane":
        if temperature >= weatherdict[precipType]["mintemp"]:
            return True
        else:
            return False
    else:
        if precipType in specialweatherdict:
            return True
        else:
            return False
    raise Exception("ERROR: End of function in precipTypeReverse")
def preciptype(temperature):
    reroll = 24
    while reroll > 0:
        precip = random.randint(1, 100)
        if temperature <= weatherdict["heavy blizzard"]["maxtemp"] and precip >= 1 and precip <= 2 and terrain != "desert":
            return "heavy blizzard"
        elif temperature <= weatherdict["blizzard"]["maxtemp"] and precip >= 3 and precip <= 5 and terrain != "desert":
            return "blizzard"
        elif temperature <= weatherdict["heavy snowstorm"]["maxtemp"] and precip >= 6 and precip <= 10:
            return "heavy snowstorm"
        elif temperature <= weatherdict["light snowstorm"]["maxtemp"] and precip >= 11 and precip <= 20:
            return "light snowstorm"
        elif temperature <= weatherdict["sleetstorm"]["maxtemp"] and precip >= 21 and precip <= 25:
            return "sleetstorm"
        elif temperature <= weatherdict["hailstorm"]["maxtemp"] and precip >= 26 and precip <= 27 and terrain not in ("desert","dust"):
            return "hailstorm"
        elif temperature >= weatherdict["heavy fog"]["mintemp"] and temperature <= weatherdict["heavy fog"]["maxtemp"] and precip >= 28 and precip <= 30 and terrain not in ("desert","dust"):
            return "heavy fog"
        elif temperature >= weatherdict["light fog"]["mintemp"] and temperature <= weatherdict["light fog"]["maxtemp"] and precip >= 31 and precip <= 38 and terrain != "desert":
            return "light fog"
        elif temperature >= weatherdict["mist"]["mintemp"] and precip >= 39 and precip <= 40:
            return "mist"
        elif temperature >= weatherdict["drizzle"]["mintemp"] and precip >= 41 and precip <= 45:
            return "drizzle"
        elif temperature >= weatherdict["light rainstorm"]["mintemp"] and precip >= 46 and precip <= 60:
            return "light rainstorm"
        elif temperature >= weatherdict["heavy rainstorm"]["mintemp"] and precip >= 61 and precip <= 70:
            return "heavy rainstorm"
        elif temperature >= weatherdict["thunderstorm"]["mintemp"] and precip >= 71 and precip <= 84:
            return "thunderstorm"
        elif temperature >= weatherdict["tropical storm"]["mintemp"] and precip >= 85 and precip <= 89 and terrain not in ("desert","plains"):
            return "tropical storm"
        elif temperature >= weatherdict["monsoon"]["mintemp"] and precip >= 90 and precip <= 94 and terrain not in ("desert","plains","dust"):
            return "monsoon"
        elif temperature >= weatherdict["gale"]["mintemp"] and precip >= 95 and precip <= 97 and terrain not in ("desert"):
            return "gale"
        elif temperature >= weatherdict["hurricane"]["mintemp"] and precip >= 98 and precip <= 99 and terrain not in ("desert","dust"):
                return "hurricane"
        elif precip == 100:
            return "special"
        else:
            reroll -= 1
    raise Exception("Maximum rerolls done, but no precipitation selected!")
## Special Weather
## Chooses a terrain and selects the special precipitation from a D100
def specialWeatherType():
    specialRoll = random.randint(1,100)
    match terrain:
        case "hills":
            if specialRoll <= 80:
                return "windstorm"
            else:
                return "earthquake"
        case "forest":
            if specialRoll <= 80:
                return "quicksand"
            else:
                return "earthquake"
        case "jungle":
            if specialRoll <= 5:
                return "volcano"
            elif specialRoll <= 60:
                return "rain forest downpour"
            elif specialRoll <= 80:
                return "quicksand"
            else:
                return "earthquake"
        case "swamp":
            if specialRoll <= 25:
                return "quicksand"
            elif specialRoll <= 80:
                return "sun shower"
            else:
                return "earthquake"
        case "dust":
            if specialRoll <= 40:
                return "flash flood"
            elif specialRoll <= 70:
                return "duststorm"
            elif specialRoll <= 85:
                return "tornado"
            else:
                return "earthquake"
        case "desert":
            if specialRoll <= 25:
                return "flash flood"
            elif specialRoll <= 50:
                return "sandstorm"
            elif specialRoll <= 65:
                return "oasis"
            elif specialRoll <= 85:
                return "mirage oasis"
            else:
                return "earthquake"
        case "mountains":
            if specialRoll <= 20:
                return "windstorm"
            elif specialRoll <= 50:
                return "rock avalanche"
            elif specialRoll <= 75:
                return "snow avalanche"
            elif specialRoll <= 80:
                return "volcano"
            else:
                return "earthquake"
        case "seacoast":
            if specialRoll <= 80:
                return "earthquake"
            elif specialRoll <= 94:
                return "tsunami"
            else:
                return "undersea volcano"
        case "sea":
            if specialRoll <= 20:
                return "tsunami"
            elif specialRoll <= 40:
                return "undersea volcano"
            else:
                return "undersea earthquake"
## True Temperature Effects
## From windspeed and temperature returns a "true temperature" from a matrix
def windchill(windspeed, temp):
    windspeed = (windspeed//5)*5
    temp = (temp//5)*5
    if windspeed > 60:
        windspeed = 60
    if temp < -20:
        temp = -20
    temp += 20
    match windspeed:
        case 5:
            match temp:
                case 55: return 33
                case 50: return 27
                case 45: return 21
                case 40: return 16
                case 35: return 12
                case 30: return 7
                case 25: return 1
                case 20: return -6
                case 15: return -11
                case 10: return -15
                case 5: return -22
                case 0: return -28
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 10:
            match temp:
                case 55: return 21
                case 50: return 16
                case 45: return 9
                case 40: return 2
                case 35: return -2
                case 30: return -9
                case 25: return -15
                case 20: return -22
                case 15: return -27
                case 10: return -31
                case 5: return -37
                case 0: return -48
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 15:
            match temp:
                case 55: return 16
                case 50: return 11
                case 45: return 1
                case 40: return -6
                case 35: return -11
                case 30: return -18
                case 25:  return -25
                case 20:  return -33
                case 15: return -40
                case 10: return -45
                case 5: return -51
                case 0: return -58
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 20:
            match temp:
                case 55: return 12
                case 50: return 3
                case 45: return -4
                case 40: return -9
                case 35: return -17
                case 30: return -24
                case 25: return -32
                case 20: return -40
                case 15: return -46
                case 10: return -52
                case 5: return -58
                case 0: return -64
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 25:
            match temp:
                case 55: return 7
                case 50: return 0
                case 45: return -7
                case 40: return -15
                case 35: return -22
                case 30: return -29
                case 25: return -37
                case 20: return -45
                case 15: return -52
                case 10: return -58
                case 5: return -65
                case 0: return -72
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 30:
            match temp:
                case 55: return 5
                case 50: return -2
                case 45: return -11
                case 40: return -18
                case 35: return -26
                case 30: return -33
                case 25: return -41
                case 20: return -49
                case 15: return -56
                case 10: return -63
                case 5: return -70
                case 0: return -78
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 35:
            match temp:
                case 55: return 3
                case 50: return -4
                case 45: return -13
                case 40: return -20
                case 35: return -27
                case 30: return -35
                case 25: return -43
                case 20: return -52
                case 15: return -60
                case 10: return -67
                case 5: return -75
                case 0: return -82
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 40:
            match temp:
                case 55: return 1
                case 50: return -4
                case 45: return -15
                case 40: return -22
                case 35: return -29
                case 30: return -36
                case 25: return -45
                case 20: return -54
                case 15: return -62
                case 10: return -69
                case 5: return -76
                case 0: return -83
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 45:
            match temp:
                case 55: return 1
                case 50: return -6
                case 45: return -17
                case 40: return -24
                case 35: return -31
                case 30: return -38
                case 25: return -46
                case 20: return -55
                case 15: return -63
                case 10: return -70
                case 5: return -77
                case 0: return -84
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 50:
            match temp:
                case 55: return 0
                case 50: return -7
                case 45: return -17
                case 40: return -24
                case 35: return -31
                case 30: return -38
                case 25: return -47
                case 20: return -56
                case 15: return -64
                case 10: return -71
                case 5: return -78
                case 0: return -85
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 55:
            match temp:
                case 55: return -1
                case 50: return -8
                case 45: return -19
                case 40: return -25
                case 35: return -33
                case 30: return -39
                case 25: return -48
                case 20: return -57
                case 15: return -65
                case 10: return -72
                case 5: return -79
                case 0: return -86
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case 60:
            match temp:
                case 55: return -3
                case 50: return -10
                case 45: return -21
                case 40: return -27
                case 35: return -34
                case 30: return -40
                case 25: return -49
                case 20: return -58
                case 15: return -66
                case 10: return -73
                case 5: return -80
                case 0: return -87
                case _: raise Exception("Can't match to the temperature matrix. Returned temperature: " + str(temp))
        case _:
            raise Exception("Can't match to windspeed matrix. Returned windspeed: " + str(windspeed))
    raise Exception("Can't match to the matrix at all. Returned temperature: " + str(temp) + " Returned windspeed: " + str(windspeed))
## Precipitation Sequence
## Takes a precipitation and determines the sequence of change, continuation or whenever it ends with a rainbow
## It basically builds a sequence of weather phenomena.
def precipSeq(precip):
    thisPrecip = precip
    temp = list(weatherdict)
    continueChance = weatherdict[thisPrecip]["continue"]
    if random.randint(1, 100) <= continueChance:
        continue_method = random.randint(1,10)
        if continue_method == 1 and thisPrecip not in ("heavy blizzard", "special"):
            return True, temp[temp.index(thisPrecip) - 1]
        elif continue_method == 10 and thisPrecip not in ("hurricane", "special"):
            return True, temp[temp.index(thisPrecip) + 1]
        else:
            return True, thisPrecip
    else:
        if random.randint(1,100) <= weatherdict[thisPrecip]["rainbow"]:
            return True, "rainbow"
        else:
            return False, None
    raise Exception("ERROR: precipSeq didn't return a continuation")
## Temperature type
## This is meant to determine stretches of cold snaps or heat waves (but not how long).
## It returns whenever it's normal temperature or not.
def temperatureType():
    tempTypeTest = random.randint(1, 100)
    if tempTypeTest == 1:
        # Extreme record low
        return 1, "extremely low"
    elif tempTypeTest == 2:
        # Severe record low
        return 2, "very low"
    elif tempTypeTest == 3 or tempTypeTest == 4:
        # Record low
        return 3, "low"
    elif tempTypeTest == 97 or tempTypeTest == 98:
        # Record high
        return 5, "high"
    elif tempTypeTest == 99:
        # Severe record high
        return 6, "very high"
    elif tempTypeTest == 100:
        # Extreme record high
        return 7, "extremely high"
    else:
        # Normal temperature
        return 4, "normal"
## Temperature Duration
## This function determines how long a cold snap or heat wave will last.
## It returns the length in days.
def temperatureDuration():
    tempDurTest = random.randint(1, 20)
    if tempDurTest == 1:
        return 1
    elif tempDurTest >= 2 and tempDurTest <= 3:
        return 2
    elif tempDurTest >= 4 and tempDurTest <= 10:
        return 3
    elif tempDurTest >= 11 and tempDurTest <= 14:
        return 4
    elif tempDurTest >= 15 and tempDurTest <= 17:
        return 5
    elif tempDurTest >= 18 and tempDurTest <= 19:
        return 6
    elif tempDurTest == 20:
        return 7
    else:
        raise Exception("Something is wrong with the tempdur function!")
## Determines sky conditions
def skyGen(thisDay, thisMonth):
    thisMonth = monthNeighbor(thisMonth, "this", thisDay)
    weather_rand = random.randint(1, 100)
    if weather_rand >= 1 and weather_rand <= baseline[thisMonth]["clear-upper"] :
        sky = "clear"
    elif weather_rand >= baseline[thisMonth]["cloud-part-lower"] and weather_rand <= baseline[thisMonth]["cloud-part-upper"] :
        sky = "partially cloudy"
    else:
        sky = "cloudy"
    return sky
## Determines regular windspeed
def windSpeedGen():
    if terrain == "hills":
        windspeed = random.randint(1, 20)-1 + terraindict[terrain]["wind-mod"]()
    else:
        windspeed = random.randint(1, 20)-1 + terraindict[terrain]["wind-mod"]
    if windspeed < 0:
        windspeed = 0
    return windspeed
## Determines windspeed direction (seasonal)
def windDirectionCheck(thisMonth):
    windTest = random.randint(1,2)
    if seasonCheck(thisMonth) in ("early autumn","late autumn","early winter","late winter"):
        match windTest:
            case 1:return "north"
            case 2:return "north-east"
    else:
        match windTest:
            case 1: return "east"
            case 2: return "south-east"
    raise Exception("Something is wrong in windDirectionCheck function")
## This function is meant to calculate temperatures throughout the month.
def genMonthlyTemps(dateNow, monthNow):
    temporary = list(baseline)
    if monthNow == "sunsebb":
        nextMonth = "fireseek"
    else:
        nextMonth = temporary[temporary.index(monthNow) + 1]
    if monthNow == "fireseek":
        prevMonth = "sunsebb"
    else:
        prevMonth = temporary[temporary.index(monthNow) - 1]
    prevMonthTemp = baseline[prevMonth]["base-temp"]
    thisMonthTemp = baseline[monthNow]["base-temp"]
    nextMonthTemp = baseline[nextMonth]["base-temp"]
    #print(prevMonthTemp, thisMonthTemp, nextMonthTemp)
    if dateNow == 14:
        calculatedTemperature = baseline[monthNow]["base-temp"]
    elif dateNow > 14:
        tempDiffRate = (nextMonthTemp - thisMonthTemp)/28
        calculatedTemperature = thisMonthTemp + (dateNow - 14) * tempDiffRate
    elif dateNow < 14:
        tempDiffRate = (thisMonthTemp - prevMonthTemp)/28
        calculatedTemperature = thisMonthTemp + (dateNow - 14) * tempDiffRate
    else:
        raise Exception("ERROR: Could now calculate monthly temperature in genMonthlyTemps()")
    return math.ceil(calculatedTemperature)
## This function is meant to determine today's highest and lowest temperatures.
def genThisDayTemp(tempType, waterCurrentTemperature, mountainElevation, skyType):
    if mountainElevation != None:
        mountainElevationNew = mountainElevation//1000
    else:
        mountainElevationNew = 0
    basetemp = genMonthlyTemps(currentday, currentmonth)-2*(latitude-40)-3*mountainElevationNew # First we determine the baseline temperature for the day compared to the latitude and elevation (if in mountains).
    lowtemp = baseline[currentmonth]["daily-low"]() # We roll for the daily lowest temperature by invoking this dict. We should only do this once!
    hightemp = baseline[currentmonth]["daily-high"]() # We roll for the daily highest temperature by invoking this dict. We should only do this once!
    match tempType: # Here we determine whenever we have a cold snap or heat wave and adjust the baseTempNew accordingly.
        case 1:
            baseTempNew = basetemp+3*lowtemp
        case 2:
            baseTempNew = basetemp+2*lowtemp
        case 3:
            baseTempNew = basetemp+lowtemp
        case 5:
            baseTempNew = basetemp+hightemp
        case 6:
            baseTempNew = basetemp+2*hightemp
        case 7:
            baseTempNew = basetemp+3*hightemp
        case 4:
            baseTempNew = basetemp
        case _:
            raise Exception("Something is wrong with temperature calculation with genThisDayTemp")
    ## Calculate low and high temps ##
    ## Now that we have tested the cold snap we adjust low and high temperatures according to terrain modifiers.
    if terrain in ("desert","dust"): # These terrains have tumples of modifiers because they increase the range between coldest and warmest.
        hightemp += baseTempNew+terraindict[terrain]["temp-mod"][0]
        lowtemp += baseTempNew+terraindict[terrain]["temp-mod"][1]
    elif terrain not in ("seacoast","sea"):
        baseTempNew += terraindict[terrain]["temp-mod"]
        hightemp += baseTempNew
        lowtemp += baseTempNew
    else:
        if waterCurrentTemperature == "warm":
            baseTempNew += terraindict[terrain]["temp-mod"][0]
            hightemp += baseTempNew
            lowtemp += baseTempNew
        elif waterCurrentTemperature == "cold":
            baseTempNew += terraindict[terrain]["temp-mod"][1]
            hightemp += baseTempNew
            lowtemp += baseTempNew
        else:
            raise Exception("Something is wrong with determining the terrain modifiers in genThisDayTemp")
    hightemp += clearSkyTempMod(skyType)
    return lowtemp, baseTempNew, hightemp # Now we return the modified lowest, base and highest temperatures.
## This function generates and manages precipitation during the day and returns lists of sequences, durations and windspeeds.
## It also sends a start time, however it's randomly generated and because of that it's imperfect. It should start during the day when the temperature allows it.
def genPrecip(temperature):
    precip = preciptype(temperature)
    if precip == "special":
        event = specialWeatherType()
        weather = event
        if event == "mirage oasis" or event == "oasis":
            event = "oasis or mirage oasis"
        elif event == "sandstorm" or event == "duststorm":
            event = "sand or dust storm"
        elif event == "rock avalanche" or event == "snow avalanche":
            event = "avalanche"
        elif event == "undersea volcano":
            event = "volcano"
        elif event == "undersea earthquake":
            event = "earthquake"
        if specialweatherdict[event]["duration"]() == None:
            weatherDuration = 0
        else:
            weatherDuration = specialweatherdict[event]["duration"]()
        if specialweatherdict[event]["speed"]() == None:
            weatherDuration = 0
        else:
            weatherWind = specialweatherdict[event]["speed"]()
    else:
        weather = precip
        if terrain in ("seacoast", "sea") and weather in ("light fog", "heavy fog", "mist"):
            weatherDuration = 2*weatherdict[weather]["duration"]()
            weatherWind = weatherdict[weather]["wind"]()
        else:
            weatherDuration = weatherdict[weather]["duration"]()
            weatherWind = weatherdict[weather]["wind"]()
    weatherResult = [weather, weatherDuration, weatherWind]
    return weatherResult
    raise Exception("ERROR: genPrecips function was called but recorded no precipitation!")
## HUMIDITY CHECK
## This function is meant to test the humidity, it returns the relative humidity and it's severity where 0 means unaffected and 4 is the worst. - pg. 25
def humidityCheck(currentTemperature):
    relativeHumidity = random.randint(1,100)
    if currentTemperature <= 75:
        return relativeHumidity, 0
    else:
        humidityTest = currentTemperature+relativeHumidity
        if humidityTest >= 140 and humidityTest <= 160:
            return relativeHumidity, 1
        elif humidityTest >= 161 and humidityTest <= 180:
            return relativeHumidity, 2
        elif humidityTest >= 181 and humidityTest <= 200:
            return relativeHumidity, 3
        elif humidityTest > 200:
            return relativeHumidity, 4
        else:
            return relativeHumidity, 0
    raise Exception("Something went wrong with humidityCheck function.")
# SUNRISE-SUNSET CALCULATOR
# This function calculates the sunrise and sunset throughout any day during the the year.
def calcSunriseSunset():
# 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28    1  2  3  4  5  6  7  8  9 10 11 12 13 14
#  0  1  2  3  4  5  6  7  8  9 10 11 12 12 14   15 16 17 18 19 20 21 22 23 24 25 26 27  0
    #daysSinceLastMonth = None
    nextMonth = monthNeighbor(currentmonth, "next", None)
    thisMonth = monthNeighbor(currentmonth, "this", currentday)
    prevMonth = monthNeighbor(currentmonth, "prev", None)
    if currentday > 14:
        sunrise1 = baseline[thisMonth]["sunrise"]
        sunset1 = baseline[thisMonth]["sunset"]
        daysSinceLastMonth = currentday - 14
        sunrise2 = baseline[nextMonth]["sunrise"]
        sunset2 = baseline[nextMonth]["sunset"]
    elif currentday < 14:
        sunrise2 = baseline[thisMonth]["sunrise"]
        sunset2 = baseline[thisMonth]["sunset"]
        sunrise1 = baseline[prevMonth]["sunrise"]
        sunset1 = baseline[prevMonth]["sunset"]
        daysSinceLastMonth = currentday + 13
    else:
        return baseline[thisMonth]["sunrise"], baseline[thisMonth]["sunset"]
    sunRiseHours1, sunRiseMinutes1 = map(int, sunrise1.split(":"))
    sunRiseHours2, sunRiseMinutes2 = map(int, sunrise2.split(":"))
    sunRiseMinutes2 += 60*sunRiseHours2
    sunRiseMinutes1 += 60*sunRiseHours1
    sunRiseMinutesDiff = sunRiseMinutes2 - sunRiseMinutes1
    sunRiseRate = sunRiseMinutesDiff / 27
    sunriseMinutes = sunRiseMinutes1 + sunRiseRate * daysSinceLastMonth
    sunriseHours = math.trunc(sunriseMinutes) // 60
    sunriseRemainder = math.trunc(sunriseMinutes) % 60
    sunsetHours1, sunsetMinutes1 = map(int, sunset1.split(":"))
    sunsetHours2, sunsetMinutes2 = map(int, sunset2.split(":"))
    sunsetMinutes2 += 60*sunsetHours2
    sunsetMinutes1 += 60*sunsetHours1
    sunsetMinutesDiff = sunsetMinutes2 - sunsetMinutes1
    sunsetRate = sunsetMinutesDiff / 27
    sunsetMinutes = sunsetMinutes1 + sunsetRate * daysSinceLastMonth
    sunsetHours = math.trunc(sunsetMinutes) // 60
    sunsetRemainder = math.trunc(sunsetMinutes) % 60
    middayMinutes = (sunsetMinutes + sunriseMinutes)/2
    middayHours = math.trunc(middayMinutes) // 60
    middayRemainder = math.trunc(middayMinutes) % 60
    conclusion = [str(sunriseHours).zfill(2)+":"+str(sunriseRemainder).zfill(2), str(sunsetHours).zfill(2)+":"+str(sunsetRemainder).zfill(2), str(middayHours).zfill(2)+":"+str(middayRemainder).zfill(2)]
    return conclusion
## Generate temperature over the hours.
def genHoursTemp(hightempPrev, lowtemp, lowtempNext, hightemp, sunriseSunset):
    hourlyTempSeq = []
    sunriseHour, sunriseMinute = map(int, sunriseSunset[0].split(":"))
    midday, middayMinute = map(int, sunriseSunset[2].split(":"))
    sunriseLowTemp = sunriseHour - 1
    riseTempDiff2 = hightempPrev - lowtemp
    riseTempDiff = hightemp - lowtemp
    fallTempDiff = hightemp - lowtempNext
    riseTempRate2 = riseTempDiff2 / (24 - sunriseLowTemp)
    riseTempRate = riseTempDiff / (midday - sunriseLowTemp)
    fallTempRate = fallTempDiff / (24- sunriseLowTemp)
    hourGen = 0
    thisHour = 0
    while hourGen < 24:
        if thisHour == midday:
            temperatureNow = hightemp
        elif thisHour == (sunriseLowTemp):
            temperatureNow = lowtemp
        elif thisHour < midday and thisHour >= sunriseHour:
            temperatureNow = lowtemp + (hourGen-sunriseHour) * riseTempRate
        elif thisHour < (sunriseLowTemp):
            temperatureNow = hightempPrev - (hourGen+(24-midday)) * riseTempRate2
        else:
            temperatureNow = hightemp - (hourGen-midday) * fallTempRate
        hourlyTempSeq.append(math.trunc(temperatureNow))
        if thisHour < 24:
            thisHour += 1
        else:
            thisHour = 0
        hourGen += 1
    return hourlyTempSeq
## Presentation function
## This function is meant to present and structure strings to the viewer.
def conclusionPresentation(sequenceDict, thisTerrain):
    precipStartBool = False
    precipDuration = 0
    iteration = 0
    for thisDay in sequenceDict[0]:
        if thisDay > 0 and thisDay <= 7:
            todayName = dayNameList[thisDay-1][0]
            todayPurpose = dayNameList[thisDay-1][1]
        elif thisDay > 7 and thisDay <= 14:
            todayName = dayNameList[thisDay-8][0]
            todayPurpose = dayNameList[thisDay-8][1]
        elif thisDay > 14 and thisDay <= 21:
            todayName = dayNameList[thisDay-15][0]
            todayPurpose = dayNameList[thisDay-15][1]
        elif thisDay > 21 and thisDay <= 28:
            todayName = dayNameList[thisDay-22][0]
            todayPurpose = dayNameList[thisDay-22][1]
        precipString = ""
        thisHour = 0
        thisMonth = sequenceDict[1][iteration]
        thisYear = startingYear
        timeHourString = thisHour
        normalWind = sequenceDict[5][iteration]
        skyCondition = sequenceDict[4][iteration]
        sunriseSunsetToday = sequenceDict[7][iteration]
        if precipStartBool == False:
            precipBool = precipCheck()
        print("-------------------------------")
        print("It's "+str(todayName).capitalize()+" ("+todayPurpose+"), "+str(thisDay)+" in "+str(thisMonth).capitalize()+" ("+seasonCheck(thisMonth)+
              "), CY "+str(thisYear)+". Location: "+str(thisTerrain).capitalize()+" at "+str(latitude)+u'\N{DEGREE SIGN}'+"N."+" The sun will rise "+
              str(sunriseSunsetToday[0])+" and fall "+str(sunriseSunsetToday[1])+".")
        if precipBool and precipDuration <= 0:
            precipHour = random.randint(0,23)
            if convertAMPM:
                if thisHour > 12:
                    timeHourString -= 12
                    timeStringMod = " PM"
                else:
                    timeStringMod = " AM"
                precipTimeString = str(timeHourString)+timeStringMod
            else:
                precipTimeString = str(precipHour).zfill(2)+":00"
            precip = genPrecip(sequenceDict[6][iteration][precipHour])
            precipType = str(precip[0])
            precipDuration = int(precip[1])+precipHour
            precipWind = int(precip[2])
            if precipWind > normalWind:
                windString = "pick up"
            elif precipWind < normalWind:
                windString = "slow down"
            else:
                windString = "stays the same"
            print("The weather will be "+str(skyCondition)+" with a wind speed of "+str(normalWind)+" mph until a "+str(precipType)+" appears at "+hourConvert(precipHour)+" for "+str(precipDuration)+" hour(s)!")
        elif precipStartBool and precipDuration > 0:
            print("The "+str(precipType)+" continues today!")
        elif precipBool == False and precipStartBool == False:
            print("The sky will be "+str(skyCondition)+" and the wind will blow at "+str(normalWind)+" mph.")
        while thisHour < 24:
            precipString = ""
            heatCrampsString = ""
            windChillString = ""
            frostBiteString = ""
            humidityString = ""
            tempHour = int(sequenceDict[6][iteration][thisHour])
            if precipBool:
                if int(thisHour) == int(precipHour) and precipStartBool == False:
                    precipString = "A "+str(precipType)+" starts! The wind will "+str(windString)+" to "+str(precipWind)+" mph."
                    precipStartBool = True
                if precipStartBool:
                    precipDuration -= 1
                    if int(precipDuration) == 0:
                        precipContinue = precipSeq(precipType)
                        if precipContinue[0]:
                            precipPrevType = precipType
                            precipType = str(precipContinue[1])
                            if str(precipPrevType) == str(precipType):
                                precipDuration += int(weatherdict[precipContinue[1]]["duration"]())
                                precipWind = int(weatherdict[precipContinue[1]]["wind"]())
                                precipString = "The "+str(precipPrevType)+" continues for another "+str(precipDuration)+" hour(s)."
                            elif precipType != "rainbow":
                                precipDuration += int(weatherdict[precipContinue[1]]["duration"]())
                                precipWind = int(weatherdict[precipContinue[1]]["wind"]())
                                precipString = "The "+str(precipPrevType)+" gives way to "+str(precipType)+" and the wind changes to "+str(precipWind)+" mph!"
                            else:
                                precipString = "The "+str(precipPrevType)+" stops and a pretty "+str(precipType)+" appears! The wind returns to "+str(normalWind)+" mph and the sky turns "+str(skyCondition)+"."
                                precipStartBool = False
                                precipBool = False
                        else:
                            precipString = "The "+str(precipType)+" stops! The wind returns to "+str(normalWind)+" mph and the sky turns "+str(skyCondition)+"."
                            precipStartBool = False
                            precipBool = False
            if precipStartBool:
                currentWindSpeed = precipWind
            else:
                currentWindSpeed = normalWind
            if tempHour < 35 and currentWindSpeed > 5:
                windChillString = "The chilling wind will feel like "+tempConvert(windchill(currentWindSpeed, tempHour))+"!"
            if tempHour > 75:
                humidityResult = humidityCheck(tempHour)
                match humidityResult[1]:
                    case 0: humidityMag = "trivial"
                    case 1: humidityMag = "bad"
                    case 2: humidityMag = "terrible"
                    case 3: humidityMag = "horrible"
                    case 4: humidityMag = "overwhelming"
                if humidityResult[1] > 0:
                    humidityString = "The relative humidity is "+str(humidityResult[0])+"% and it's "+humidityMag+" ("+str(humidityResult[1])+")!"
            if tempHour > 120:
                heatCrampsString = "There's a high risk of heat cramps! Affects CON below "+str(12+(tempHour-120)//10)
            elif tempHour > 100:
                heatCrampsString = "There's a high risk of heat cramps! Affects CON below "+str(12)
            if tempHour < -40:
                frostBiteString = "There's a high risk of frostbite!"
            print("The time is "+hourConvert(thisHour)+" and the temperature is "+tempConvert(tempHour)+".", windChillString, heatCrampsString, frostBiteString, humidityString, precipString)

            thisHour += 1
        iteration += 1
def generateEverything(days):
    pass
#############
## QUERIES ##
#############
def startMonthQuery():
    print("What month is it?")
    print("Possible months:", monthsAll)
    while True:
        if debug:
            startingMonth = random.choice(monthsAll)
            break
        else:
            startingMonth = input().lower()
        if startingMonth in monthsAll:
            break
        elif startingMonth == "":
            startingMonth = random.choice(monthsAll)
            break
        else:
            print("This month doesn't exist, use one from the list.")
            continue
def startDayQuery():
    print("What day should we start at?")
    while True:
        if debug:
            startingDay = random.randint(1,28)
            break
        else:
            startingDaySelect = input()
        if startingDaySelect == "":
            startingDay = random.randint(1,28)
            break
        try:
            startingDay = int(startingDaySelect)
        except ValueError:
            print("Looks like you haven't put in an integer, please do so.")
            continue
        if startingDay < 1 or startingDay > 28:
            print("Only 1-28 are valid.")
            continue
        else:
            break
    return startingDay
def genDaysQuery():
    print("How many days do you want to generate forecast for?")
    while True:
        if debug:
            daysGenInput = 2
            return daysGenInput+currentday
            break
        else:
            daysGenInput = input()
        if daysGenInput == "":
            daysGenInput = random.randint(1,3)*7
            return daysGenInput+currentday
            break
        try:
            return int(daysGenInput)+currentday
        except ValueError:
            print("Looks like you haven't put in an integer, please do so.")
            continue
        if int(daysGenInput) < 1:
            print("We can't generate 0 days or generate backwards, please put in a positive integer.")
            continue
        else:
            break
        raise Exception("Error in startingDay selection. End of loop.")
def latitudeQuery():
    print("What latitude are they players at (15 - 55)?")
    while True:
        if debug:
            return random.randint(15,55)
            break
        else:
            latitudeSelect = input()
        if latitudeSelect == "":
            return random.randint(15,55)
            break
        try:
            return int(latitudeSelect)
        except ValueError:
            print("Looks like you haven't put in an integer, please do so.")
            continue
        if latitudeSelect < 15 or latitudeSelect > 55:
            print("Your party is out of bounds with the map then, try again.")
        else:
            break
def terrainQuery():
    print("What's the terrain?")
    print("Possible terrains:", terrainTypes)
    while True:
        if debug:
            terrainPrompt = "plains"
            terrain = terrainPrompt
            break
        else:
            terrainPrompt = input().lower()
        if terrainPrompt in terrainTypes:
            terrain = terrainPrompt
            break
        elif terrainPrompt == "":
            terrainPrompt = "plains"
            terrain = terrainPrompt
            break
        else:
            print("This terrain type doesn't exist, use one from the list.")
            continue
    if terrain == "rough terrain":
        terrain = "hills"
    elif terrain == "marsh":
        terrain = "swamp"
    if terrain == "jungle" and latitude > 25:
        print("Consider the fact that the climate above 25th parallel probably doesn't contain any jungles. You have selected "+terrain+" at "+str(latitude)+"th parallel.")
    if terrain == "mountains":
        print("What's the elevation (in feet)?")
        elevation = int(input())
    else:
        elevation = None
    if terrain == "sea" or terrain == "seacoast":
        print("Is the current warm or cold?")
        waterTempCurrent = str(input())
    else:
        waterTempCurrent = None
    sylvanPrompt = False
    while terrain in ("forest","jungle"):
        print("Are we in a Sylvan forest zone? (y/n)")
        sylvanPrompt = input().lower()
        if sylvanPrompt == "y":
            sylvanPrompt = True
            terrainPrompt = "Sylvan forest"
            break
        elif sylvanPrompt == "n":
            sylvanPrompt = False
            break
        else:
            print("Please write either y or n.")
            continue
if debug == False:
    currentmonth = startMonthQuery()
    currentday = startDayQuery()
    daysGenInput = genDaysQuery()
    latitude = latitudeQuery()
    terrain = terrainQuery()
else:
    currentmonth = "needfest"
    currentday = 1
    daysGenInput = 2
    latitude = 40
    terrain = "plains"
gendays = daysGenInput
iteration = currentday
extremeTempType = [4, "normal"]
tempDuration = 0
precipDur = 0
dateSeq = []
monthSeq = []
highTempSeq = []
lowTempSeq = []
skySeq = []
windSpeedSeq = []
dailyHourlyTempSeq = []
sunriseSunsetSeq = []
everySingleSeq = [dateSeq, monthSeq, highTempSeq, lowTempSeq, skySeq, windSpeedSeq, dailyHourlyTempSeq, sunriseSunsetSeq]
if int(daysGenInput) < 7:
    print("Generating "+str(daysGenInput)+" days of weather...")
elif int(daysGenInput) >= 7 and int(daysGenInput) < 56:
    print("Generating "+str(int(daysGenInput)//7)+" weeks of weather...")
elif int(daysGenInput) >= 56 and int(daysGenInput) < 672:
    print("Generating "+str(int(daysGenInput)//28)+" months of weather...")
elif int(daysGenInput) >= 672:
    print("Generating "+str(int(daysGenInput)//336)+" years of weather...")
else:
    raise Exception("ERROR: Could not determine magnitude of generation in days!")
## This very important while loop tries to calculate values throughout the generation
while iteration < gendays:
    dateSeq.append(currentday)
    monthSeq.append(currentmonth)
    sunriseSunsetResult = calcSunriseSunset()
    sunriseSunsetSeq.append(sunriseSunsetResult)
    if tempDuration <= 0: # We don't check if there's an ongoing cold snap or heat wave.
        extremeTempType = temperatureType() # First we determine if there's a cold snap or heat wave.
        tempDuration = temperatureDuration() # Now we determine how long the cold snap or heat wave is going to last.
    elif tempDuration > 0: # Apply higher temperatures when this is triggered.
        tempDuration -= 1
    skyResult = skyGen(currentday, currentmonth)
    dailyTemps = genThisDayTemp(extremeTempType[0], waterTempCurrent, elevation, skyResult) # Here we check for daily temperatures.
    highTempSeq.append(dailyTemps[2]) # We add high temperatures to a sequence for hourly generation later.
    lowTempSeq.append(dailyTemps[0]) # We add low temperatures to a sequence for hourly generation later.
    #print("The base index is", len(dateSeq), "\nThe perc index is", len(dateSeq))
    skySeq.append(skyResult)
    windSpeedSeq.append(windSpeedGen())
    ## This should be last ##
    currentday += 1
    iteration += 1
# To loop around #
    if currentday > 28:
        if currentmonth != "sunsebb":
            temp = list(baseline)
            currentmonth = temp[temp.index(currentmonth) + 1]
            currentday = 1
        else:
            currentmonth = "fireseek"
            currentday = 1
conclusionIteration = 0
for dateHere in dateSeq:
    if conclusionIteration+1 == len(dateSeq):
        dailyHourlyTempSeq.append(genHoursTemp(highTempSeq[conclusionIteration-1], lowTempSeq[conclusionIteration], lowTempSeq[conclusionIteration], highTempSeq[conclusionIteration], sunriseSunsetResult))
    elif conclusionIteration <= 0:
        dailyHourlyTempSeq.append(genHoursTemp(highTempSeq[conclusionIteration],   lowTempSeq[conclusionIteration], lowTempSeq[conclusionIteration+1], highTempSeq[conclusionIteration], sunriseSunsetResult))
    else:
        dailyHourlyTempSeq.append(genHoursTemp(highTempSeq[conclusionIteration-1], lowTempSeq[conclusionIteration], lowTempSeq[conclusionIteration+1], highTempSeq[conclusionIteration], sunriseSunsetResult))
    conclusionIteration += 1
if debug == True and verbose == True:
    for sequence in everySingleSeq:
        print("Here's the sequence:", sequence)
if verbose == False:
    conclusionPresentation(everySingleSeq, terrainPrompt)
