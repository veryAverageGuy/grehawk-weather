#!/bin/python

# Imports
import random
import math

# Special variables
global debug
global verbose
global convertFBool
global convertAMPM
global customTweaks
global sylvanBool
debug = False
verbose = False
convertFBool = True
convertAMPM = False
customTweaks = False
sylvanBool = False

# Global lists
global dayNameList
global monthsAll
global months
global festivals
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
    "cyclone": {
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
## This function is meant to calculate the month and date from days since startdate.
def monthDayCalc(dayCountFromStart):
    dayCount = dayCountFromStart
    currentDay = 0
    currentMonth = "needfest"
    currentYear = 576
    moonPhaseLuna = round(100*(0.5*(1+math.cos( ( dayCountFromStart - 18 ) * math.pi / 14 ))+math.sin( ( dayCountFromStart - 18 ) * math.pi / 14 )/4))
    moonPhaseCelene = round(100*(0.5*(1+math.cos( ( dayCountFromStart - 4 ) * math.pi / 45.5))+math.sin( ( dayCountFromStart - 4 ) * math.pi / 45.5 )/4))
    moonPhase = "Luna: "+str(max(min(moonPhaseLuna,100),0))+'%', "Celene: "+str(max(min(moonPhaseCelene,100),0))+'%'
    while dayCount > 0:
        currentDay += 1
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
        dayCount -= 1
    dayNameIndex = currentDay%7
    return currentDay, dayNameList[dayNameIndex], currentMonth, moonPhase, currentYear
## This function checks the neighbors of another month to map to the baseline dictionary. Accepts the month to be checked and (prev/next/this)
## It returns a tuple containing the previous or next month and the time between day 14 between last month and the one it's asking about.
def monthNeighbor(thisDay, thisMonth, neighbor):
    if thisMonth == "needfest":
        prevMonth = "sunsebb"
    else:
        prevMonth = monthsAll[monthsAll.index(thisMonth)-1]
    if thisMonth == "sunsebb":
        nextMonth = "fireseek"
    else:
        nextMonth = monthsAll[monthsAll.index(thisMonth)+1]
    match neighbor:
        case "next":
            if thisMonth == "sunsebb":
                return "fireseek", 35
            elif nextMonth in festivals:
                return monthsAll[monthsAll.index(thisMonth)+2], 35
            else:
                return nextMonth, 28
        case "prev":
            if thisMonth == "needfest":
                return "sunsebb", 35
            elif prevMonth in festivals:
                return monthsAll[monthsAll.index(thisMonth)-2], 35
            else:
                return prevMonth, 28
        case "this":
            if thisMonth in festivals:
                if thisDay > 4:
                    return nextMonth, 35
                elif thisMonth == "needfest":
                    return "sunsebb", 35
                else:
                    return prevMonth, 35
            else:
                return thisMonth, 35
        case _:
            raise Exception("ERROR: Neighbor unrecoginzed")
    raise Exception("ERROR: End of function")
## CLEAR SKY MODIFICATION
## This is a custom function outside of the ruleset meant to make cloudy days colder and clear days warmer.
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
        return "spring festival"
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
        return "autumn festival"
    elif thisMonth == "patchwall":
        return "early autumn"
    elif thisMonth == "ready'reat":
        return "late autumn"
    raise Exception("Something is wrong in seasonCheck function.")
## CLIMATE CHECK
## This functions simply returns the climate description depending on the latitude.
def climateCheck(latitude):
    if latitude >= 15 and latitude < 23:
        return "tropic"
    elif latitude < 35:
        return "sub-tropic"
    elif latitude < 45:
        return "temperate"
    elif latitude <= 55:
        return "frigid"
    raise Exception("ERROR: Could not determine climate zone")
## Precipitation Check
## This is a simpler function that just returns whenever the day should have precipitation.
def precipBoolCheck(thisMonth, terrain):
    thisMonth = monthNeighbor(1, thisMonth, "this")[0]
    precipTest = random.randint(1, 100)
    if sylvanBool == False:
        precipRisk = baseline[thisMonth]["precip"]+terraindict[terrain]["precip-mod"]
    elif sylvanBool == True: ## Sylvan forests have minimal precipitation risk.
        precipRisk = (baseline[thisMonth]["precip"]+terraindict[terrain]["precip-mod"])//4 ## Sylvan Forests have much less risk of precipitation.
    else:
        raise Exception("ERROR: sylvanBool returned unexpected variable, expected bool")
    if precipTest <= precipRisk:
        return True
    else:
        return False
## This function returns specific precipitation.
def precipTypeSelect(temperature):
    reroll = 16 # We can set rerolls here to cut down on or increase rerolling.
    while reroll > 0:
        precip = random.randint(1, 100) # Roll D100 to determine a random precip.
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
        elif temperature >= weatherdict["cyclone"]["mintemp"] and precip >= 98 and precip <= 99 and terrain not in ("desert","dust"):
                return "cyclone"
        elif precip == 100:
            return "special"
        else:
            reroll -= 1
    return "special"
    raise Exception("Maximum rerolls done, but no precipitation selected!")
## Special Weather
## Chooses a terrain and selects the special precipitation from a D100
def specialWeatherType(terrain):
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
        case "plains":
            if specialRoll <= 50:
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
    raise Exception("ERROR: End of function", terrain)
## Causation of special weather
def specialWeatherCause():
    causeTest = random.randint(1,10)
    if causeTest == 10:
        causeTest = random.randint(1,100)
        if causeTest >= 1 and causeTest <= 30:
            return "elemental(s) or giant(s)"
        elif causeTest > 30 and causeTest <= 60:
            return "elemental(s) under NPC control"
        elif causeTest > 60 and causeTest <= 90:
            return "NPC or monster"
        elif causeTest == 99:
            return "a deity or his/her servants"
        elif causeTest == 100:
            return "two or more battling deites"
    else:
        return "natural"
    raise Exception("ERROR: End of function")
## True Temperature Effects
## From windspeed and temperature returns a "true temperature" from a matrix
def windchillTest(windspeed, temp):
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
    try:
        continueChance = weatherdict[thisPrecip]["continue"]
    except KeyError:
        return False, None
    if random.randint(1, 100) <= continueChance:
        continue_method = random.randint(1,10)
        if continue_method == 1 and thisPrecip not in ("heavy blizzard", "special"):
            return True, temp[temp.index(thisPrecip) - 1]
        elif continue_method == 10 and thisPrecip not in ("cyclone", "special"):
            return True, temp[temp.index(thisPrecip) + 1]
        else:
            return True, thisPrecip
    else:
        if random.randint(1,100) <= weatherdict[thisPrecip]["rainbow"]:
            return True, "rainbow"
        else:
            return False, None
    raise Exception("ERROR: No continuation returned")
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
    thisMonth = monthNeighbor(thisDay, thisMonth, "this")[0]
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
## This functions determines damage from windspeed
def precipDamage(windSpeed, precipType):
    if precipType == "cyclone":
        return dice(1,6), "every turn"
    elif precipType == "tornado or cyclone":
        return dice(3,6), "every turn"
    elif precipType in ("storm", "monsoon", "gale") and windSpeed > 40 and random.randint(1,10) == 1:
        return dice(1,6)*(windSpeed-40)//10, "every third turn"
    elif precipType in ("sandstorm", "duststorm") and random.randint(1,2 == 1):
        return dice(1,4), "every third turn"
    else:
        return 0, "no effect"
## This functions assigns the windspeed a beaufort classification (mph)
def windSpeedDesc(windSpeed):
    if windSpeed <= 1:
        return "calm", "smoke rises vertically"
    elif windSpeed < 3:
        return "light air", "wind motion visible in smoke"
    elif windSpeed < 7:
        return "light breeze", "wind felt on exposed skins, leaves rustle"
    elif windSpeed < 12:
        return "gentle breeze", "leaves and smaller twigs in constant motion"
    elif windSpeed < 18:
        return "moderate breeze", "dust and loose paper are raised, small branches begin to move"
    elif windSpeed < 24:
        return "fresh breeze", "small trees begin to sway"
    elif windSpeed < 31:
        return "strong breeze", "large branches in motion, whistling is heard, umbrella use is difficult"
    elif windSpeed < 38:
        return "near gale", "whole trees in motion, some difficulty experienced walking into wind"
    elif windSpeed < 46:
        return "gale", "twigs and small branches break from trees, the wind speeds will make it harder for men to move"
    elif windSpeed < 54:
        return "strong gale", "larger branches break from trees, light structural damage"
    elif windSpeed < 63:
        return "storm", "trees broken and uprooted, considerable structural damage"
    elif windSpeed < 72:
        return "violent storm", "widespread damage to structures and vegetation, there's a risk of men being swept off their feet"
    elif windSpeed < 95:
        return "category 1 cyclone", "coastal flooding, toppling of small dwellings, uprooting and snapping of weak trees"
    elif windSpeed < 110:
        return "category 2 cyclone", "extensive damage on roofs, doors and windows, small dwellings destroyed, sea-crafts break their moorings and float out into sea"
    elif windSpeed < 129:
        return "category 3 cyclone", "devastating damage on small buildings to an unrepairable degree, small dwellings are destroyed, flooding near the coast is extensive even inland, a large numbers of trees are uprooted and snapped, watch out for flying debris!"
    elif windSpeed < 156:
        return "category 4 cyclone", "complete structural failure on small buildings, heavy and irreparable damage done on overhangs, small dwellings are completely flattened, only the hardiest trees survive, flooding is overwhelming even far inland"
    elif windSpeed >= 157:
        return "category 5 cyclone", "apocalyptic damage will occur, even the sturdiest roofs will fail, most small buildings are blown away, only stone buildings stand a chance of surviving and only if located inland, most coastal structures will be washed away, virtually all trees will be uprooted and swept away"
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
def genMonthlyTemps(dateNow, thisMonth):
    prevMonth = monthNeighbor(dateNow, thisMonth, "prev")
    prevMonthTemp = baseline[prevMonth[0]]["base-temp"]
    nextMonth = monthNeighbor(dateNow, thisMonth, "next")
    nextMonthTemp = baseline[nextMonth[0]]["base-temp"]
    if thisMonth not in festivals:
        thisMonth = monthNeighbor(dateNow, thisMonth, "this")
        thisMonthTemp = baseline[thisMonth[0]]["base-temp"]
    else:
        thisMonth = thisMonth, 35
    if thisMonth[0] in festivals:
        tempDiffRate = (nextMonthTemp - prevMonthTemp)/thisMonth[1]
        calculatedTemperature = prevMonthTemp + (dateNow + 14) * tempDiffRate
        if verbose:
            print(dateNow, round(tempDiffRate,2), round(calculatedTemperature,2), dateNow + 14)
    elif dateNow == 14:
        calculatedTemperature = thisMonthTemp
        if verbose:
            print(dateNow, round(calculatedTemperature,2))
    elif dateNow > 14:
        tempDiffRate = (nextMonthTemp - thisMonthTemp)/nextMonth[1]
        calculatedTemperature = thisMonthTemp + (dateNow-14) * tempDiffRate
        if verbose:
            print(dateNow, round(tempDiffRate,2), round(calculatedTemperature,2), dateNow-14)
    elif dateNow < 14:
        tempDiffRate = (thisMonthTemp - prevMonthTemp)/prevMonth[1]
        calculatedTemperature = thisMonthTemp + (dateNow-14) * tempDiffRate
        if verbose:
            print(dateNow, round(tempDiffRate,2), round(calculatedTemperature,2), dateNow-14, prevMonth[1])
    else:
        raise Exception("ERROR: Could not calculate monthly temperature in genMonthlyTemps()")
    calculatedTemperature = round(calculatedTemperature,1)
    return calculatedTemperature
## This function is meant to determine today's highest and lowest temperatures.
def genThisDayTemp(thisDay, thisMonth, tempType, waterCurrentTemperature, mountainElevation, latitude, terrain):
    if mountainElevation != None:
        mountainElevationNew = mountainElevation//1000
    else:
        mountainElevationNew = 0
    basetemp = genMonthlyTemps(thisDay, thisMonth)-2*(latitude-40)-3*mountainElevationNew # First we determine the baseline temperature for the day compared to the latitude and elevation (if in mountains).
    thisMonth = monthNeighbor(thisDay, thisMonth, "this")[0]
    lowtemp = baseline[thisMonth]["daily-low"]() # We roll for the daily lowest temperature by invoking this dict. We should only do this once!
    hightemp = baseline[thisMonth]["daily-high"]() # We roll for the daily highest temperature by invoking this dict. We should only do this once!
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
            raise Exception("ERROR: No extreme temp type")
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
    return round(lowtemp,1), round(baseTempNew,1), round(hightemp,1) # Now we return the modified lowest, base and highest temperatures.
## This function generates and manages precipitation during the day and returns lists of sequences, durations and windspeeds.
## It also sends a start time, however it's randomly generated and because of that it's imperfect. It should start during the day when the temperature allows it.
def genPrecip(temperature, terrain):
    if len(temperature) != 24:
        raise Exception("ERROR: The array passed into function is too low, expected 24 got"+str(len(temperature))+"!")
    precipHour = int(*random.sample(range(0,23),1))
    precip = precipTypeSelect(temperature[precipHour])
    if precip == "special":
        event = specialWeatherType(terrain)
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
        elif event == "tornado":
            event = "tornado or cyclone"
        if specialweatherdict[event]["duration"]() == None:
            weatherDuration = 0
        else:
            weatherDuration = specialweatherdict[event]["duration"]()
        try:
            if specialweatherdict[event]["speed"]() == None:
                weatherWind = 0
            else:
                weatherWind = specialweatherdict[event]["speed"]()
        except TypeError:
            weatherWind = specialweatherdict[event]["speed"]
        cause = specialWeatherCause()
    else:
        weather = precip
        if terrain in ("seacoast", "sea") and weather in ("light fog", "heavy fog", "mist"):
            weatherDuration = 2*weatherdict[weather]["duration"]()
        else:
            weatherDuration = weatherdict[weather]["duration"]()
        weatherWind = weatherdict[weather]["wind"]()
        cause = "natural"
    weatherResult = [weather, weatherDuration, weatherWind, cause, precipHour]
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
            return relativeHumidity, 1, "bad"
        elif humidityTest >= 161 and humidityTest <= 180:
            return relativeHumidity, 2, "terrible"
        elif humidityTest >= 181 and humidityTest <= 200:
            return relativeHumidity, 3, "horrible"
        elif humidityTest > 200:
            return relativeHumidity, 4, "overwhelming"
        else:
            return relativeHumidity, 0, "trivial"
    raise Exception("Something went wrong with humidityCheck function.")
# SUNRISE-SUNSET CALCULATOR
# This function calculates the sunrise and sunset throughout any day during the the year.
def calcSunriseSunset(thisDay, thisMonth):
# 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28    1  2  3  4  5  6  7  8  9 10 11 12 13 14
#  0  1  2  3  4  5  6  7  8  9 10 11 12 12 14   15 16 17 18 19 20 21 22 23 24 25 26 27  0
    daysSinceLastMonth = None
    nextMonth = monthNeighbor(thisDay, thisMonth, "next")
    prevMonth = monthNeighbor(thisDay, thisMonth, "prev")
    thisMonth = monthNeighbor(thisDay, thisMonth, "this")
    if thisDay > 14:
        sunrise1 = baseline[thisMonth[0]]["sunrise"]
        sunset1 = baseline[thisMonth[0]]["sunset"]
        sunrise2 = baseline[nextMonth[0]]["sunrise"]
        sunset2 = baseline[nextMonth[0]]["sunset"]
        daysSinceLastMonth = thisDay - 14
    elif thisDay < 14:
        sunrise2 = baseline[thisMonth[0]]["sunrise"]
        sunset2 = baseline[thisMonth[0]]["sunset"]
        sunrise1 = baseline[prevMonth[0]]["sunrise"]
        sunset1 = baseline[prevMonth[0]]["sunset"]
        if prevMonth[1] == 28:
            daysSinceLastMonth = thisDay + 14
        else:
            daysSinceLastMonth = thisDay + 21
    elif thisDay == 14:
        sunrise2 = baseline[thisMonth[0]]["sunrise"]
        sunset2 = baseline[thisMonth[0]]["sunset"]
        sunrise1 = baseline[thisMonth[0]]["sunrise"]
        sunset1 = baseline[thisMonth[0]]["sunset"]
        daysSinceLastMonth = thisDay - 14
    sunRiseHours1, sunRiseMinutes1 = map(int, sunrise1.split(":"))
    sunRiseHours2, sunRiseMinutes2 = map(int, sunrise2.split(":"))
    sunRiseMinutes2 += 60*sunRiseHours2
    sunRiseMinutes1 += 60*sunRiseHours1
    sunRiseMinutesDiff = sunRiseMinutes2 - sunRiseMinutes1
    sunRiseRate = sunRiseMinutesDiff / prevMonth[1]
    sunriseMinutes = sunRiseMinutes1 + sunRiseRate * daysSinceLastMonth
    sunriseHours = math.ceil(sunriseMinutes) // 60
    sunriseRemainder = math.ceil(sunriseMinutes) % 60
    sunsetHours1, sunsetMinutes1 = map(int, sunset1.split(":"))
    sunsetHours2, sunsetMinutes2 = map(int, sunset2.split(":"))
    sunsetMinutes2 += 60*sunsetHours2
    sunsetMinutes1 += 60*sunsetHours1
    sunsetMinutesDiff = sunsetMinutes2 - sunsetMinutes1
    sunsetRate = sunsetMinutesDiff / 27
    sunsetMinutes = sunsetMinutes1 + sunsetRate * daysSinceLastMonth
    sunsetHours = math.ceil(sunsetMinutes) // 60
    sunsetRemainder = math.ceil(sunsetMinutes) % 60
    middayMinutes = (sunsetMinutes + sunriseMinutes)/2
    middayHours = math.ceil(middayMinutes) // 60
    middayRemainder = math.ceil(middayMinutes) % 60
    conclusion = str(sunriseHours).zfill(2)+":"+str(sunriseRemainder).zfill(2), str(sunsetHours).zfill(2)+":"+str(sunsetRemainder).zfill(2), str(middayHours).zfill(2)+":"+str(middayRemainder).zfill(2)
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
def genMonth(thisDay, thisMonth, tempType, terrain):
    conclusion = None
    waterCurrentTemperature = None
    mountainElevation = None
    winddirection = windDirectionCheck(thisMonth)
    skyType = skyGen(thisDay, thisMonth)
    prevDayTemp = genThisDayTemp(thisDay-1, thisMonth, tempType, waterCurrentTemperature, mountainElevation, latitude, skyType)
    nextDayTemp = genThisDayTemp(thisDay+1, thisMonth, tempType, waterCurrentTemperature, mountainElevation, latitude, skyType)
    thisDayTemp = genThisDayTemp(thisDay, thisMonth, tempType, waterCurrentTemperature, mountainElevation, latitude, skyType)
    dayTemp = prevDayTemp[0], thisDayTemp[0], nextDayTemp[2], thisDayTemp[2]
    dayDetails = genDay(thisDay, thisMonth, dayTemp, terrain)
    conclusion = winddirection, skyType, dayDetails
    return conclusion
## This function is meant to determine the conditions for the day.
## Expects a list of yesterday high temperature, today high and low and tomorrows low temperature.
def genDay(thisDay, thisMonth, terrain):
    # Calculate the sunset and sunrise for the day.
    sunriseSunset = calcSunriseSunset(thisDay, thisMonth)
    # Generate sky conditions
    windspeed = windSpeedGen()
    return conclusion
## Generate the conditions for the hours
def genHour(temperature, windspeed):
    windchill = 100000
    humidity = None, 0, None
    heatcramps = None
    frostbiteBool = False
    sunstrokeBool = (False, None)
    precipitationContinue = False
    if temperature < 35 and windspeed > 5:
        windchill = windchillTest(windspeed, temperature)
    if temperature < -40 or windchill < -40:
        frostbiteBool = True
    if temperature > 75:
        humidity = humidityCheck(temperature)
        sunstrokeBool = (True, "mild")
        if temperature > 120:
            heatcramps = 12+( ( temperature - 120 ) // 10 )
            if temperature+humidity[0] > 200:
                sunstrokeBool = (True, "severe")
        elif temperature > 100:
            heatCrampsString = 12
    return windchill, humidity, heatcramps, frostbiteBool, sunstrokeBool
## Presentation function
## This function is meant to present and structure strings to the view7er.
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
            print("The time is "+hourConvert(thisHour)+" and the temperature is "+tempConvert(tempHour)+".", windChillString, heatCrampsString, frostBiteString, humidityString, precipString)

            thisHour += 1
        iteration += 1
## This function is meant to work out the days range we're looking for
def dayCountFromStart(startDay, startMonth):
    daysReturn = 0
    for monthName in monthsAll:
        if monthName == startMonth:
            break
        elif monthName in festivals:
            daysReturn += 7
        elif monthName in months:
            daysReturn += 28
        else:
            raise Exception("ERROR: Couldn't determine month")
    daysReturn += startDay
    return int(daysReturn)
## This function is meant to generate everything
def generateEverything(startMonth, startDay, daysToGen, latitude, terrain):
    waterCurrentTemperature = None
    mountainElevation = None
    conclusion = None
    tempDuration = 0
    tempType = 4, "normal"
    calendarSeq = []
    dailyTempSeq = []
    skySeq = []
    windSeq = []
    dailyHourlyTempSeq = []
    sunriseSunsetSeq = []
    dayCount = dayCountFromStart(startDay, startMonth)
    endDate = daysToGen+dayCount
    while dayCount < endDate: # Populate the sequence of the calendar
        calendarSeq.append(monthDayCalc(dayCount))
        dayCount += 1
    for dayDetail in calendarSeq:
        if tempDuration > 0:
            tempDuration -= 1
        elif tempDuration <= 0:
            tempType = temperatureType()
            if tempType[0] != 4:
                tempDuration = temperatureDuration()
        dailyTemp = genThisDayTemp(dayDetail[0], dayDetail[2], tempType[0], waterCurrentTemperature, mountainElevation, latitude, terrain)
        dailyTempSeq.append( dailyTemp )
        skySeq.append( skyGen(dayDetail[0], dayDetail[2]) )
        windSeq.append( windSpeedGen() )
        sunriseSunsetSeq.append(calcSunriseSunset(dayDetail[0], dayDetail[2]))
    dayIteration = 0
    while dayIteration < daysToGen:
        if dayIteration+1 == daysToGen:
            dailyHourlyTempSeq.append(genHoursTemp(dailyTempSeq[dayIteration-1][2], dailyTempSeq[dayIteration][0], dailyTempSeq[dayIteration][0],   dailyTempSeq[dayIteration][2], sunriseSunsetSeq[dayIteration]))
        elif dayIteration <= 0:
            dailyHourlyTempSeq.append(genHoursTemp(dailyTempSeq[dayIteration][2],   dailyTempSeq[dayIteration][0], dailyTempSeq[dayIteration+1][0], dailyTempSeq[dayIteration][2], sunriseSunsetSeq[dayIteration]))
        else:
            dailyHourlyTempSeq.append(genHoursTemp(dailyTempSeq[dayIteration-1][2], dailyTempSeq[dayIteration][0], dailyTempSeq[dayIteration+1][0], dailyTempSeq[dayIteration][2], sunriseSunsetSeq[dayIteration]))
        dayIteration += 1
    # precipDuration = 0
    # continuePrecip = False, None
    # for day in dailyHourlyTempSeq:
    #     daySeqIndex = dailyHourlyTempSeq.index(day)
    #     thisMonth = calendarSeq[daySeqIndex][2]
    #     if precipDuration <= 0:
    #         if precipBoolCheck(thisMonth, terrain): # Is there precipitation today?
    #             todayPrecip = genPrecip(day, terrain)
    #             continuePrecip = precipSeq(todayPrecip[0]) # Will this continue?
    #             if terrain in ("seacoast", "sea") and continuePrecip[1] in ("light fog", "heavy fog", "mist"):
    #                 weatherDuration = 2*weatherdict[todayPrecip[0]]["duration"]()
    #             else:
    #                 weatherDuration = weatherdict[todayPrecip[0]]["duration"]()
    #             precipDuration = todayPrecip[4]+todayPrecip[1]+weatherDuration
    #             print(todayPrecip, continuePrecip, precipDuration, "hours.")
    #         else:
    #             print("No precipitation today...")
    #     else:
    #         print("Precipitation from yesterday continues today...", todayPrecip[0])
    #     precipDuration -= 24
    #     if precipDuration > 0 and precipDuration <= 24:
    #         print("The precipitation ends at "+str(24-precipDuration)+":00")
    conclusion = calendarSeq, skySeq, windSeq, dailyHourlyTempSeq
    return conclusion
def presentationFunction(conclusionMatrix, thisTerrain):
    precipStartedCheck = False
    thisDay = 0
    while thisDay < len(conclusionMatrix[0]):
        daySummaryString = "---------------------------------\nDate: "+str(conclusionMatrix[0][thisDay][1][0]).capitalize()+" "+str(conclusionMatrix[0][thisDay][0])+" of "+str(conclusionMatrix[0][thisDay][2]).capitalize()+", common year "+str(conclusionMatrix[0][thisDay][4])+". It's a "+str(conclusionMatrix[0][thisDay][1][1])+" day.\nThe moons are currently in this state: "+str(conclusionMatrix[0][thisDay][3])+"\nThe weather will be "+str(conclusionMatrix[1][thisDay])+" and the windspeed will be a "+windSpeedDesc(conclusionMatrix[2][thisDay])[0]+' at '+str(conclusionMatrix[2][thisDay])+" mph."
        if precipStartedCheck:
            pass
        else:
            precipDayBool = precipBoolCheck(conclusionMatrix[0][thisDay][2], thisTerrain)
        if precipDayBool:
            todaysPrecip = genPrecip(conclusionMatrix[3][thisDay], thisTerrain)
            precipDuration = todaysPrecip[1]
            precipWindspeed = todaysPrecip[2]
            daySummaryString += "\nWe'll be seeing a "+todaysPrecip[0]+" and the wind will change to a "+windSpeedDesc(precipWindspeed)[0]+" at "+str(precipWindspeed)+" mph."
        print(daySummaryString+'\n')
        thisHour = 0
        while thisHour < len(conclusionMatrix[3][thisDay]):
            dailyTemp = conclusionMatrix[3][thisDay][thisHour]
            extendedHourStats = genHour(dailyTemp, conclusionMatrix[2][thisDay])
            fullString = hourConvert(thisHour)
            if extendedHourStats[0] < dailyTemp:
                fullString += ", Windchill("+tempConvert(extendedHourStats[0])+')'
            else:
                fullString += ' '+tempConvert(dailyTemp)
            if extendedHourStats[3]:
                fullString += " There's a risk of frostbite!"
            if extendedHourStats[2] != None:
                fullString += " Heatcramps CON ("+str(extendedHourStats[2])+')'
            if extendedHourStats[4][0]:
                fullString += " There's a risk of "+extendedHourStats[4][1]+" sunstroke."
            if extendedHourStats[1][1] > 0:
                fullString += " The humidity will be "+extendedHourStats[1][2]+'.'
            if precipDayBool and thisHour == todaysPrecip[4]:
                fullString += " The "+todaysPrecip[0]+" starts now."
                precipStartedCheck = True
                precipDayBool = False
            if precipStartedCheck and precipDuration <= 0:
                continueResult = precipSeq(todaysPrecip[0])
                if continueResult[0] and continueResult[1] == "rainbow":
                    fullString += " The "+todaysPrecip[0]+" ends now and a pretty rainbow appears."
                    precipStartedCheck = False
                elif continueResult[0]:
                    if continueResult[1] != todaysPrecip[0]:
                        fullString += " The precipiation changes into a "+continueResult[1]+'.'
                    precipDuration += weatherdict[continueResult[1]]["duration"]()
                else:
                    fullString += " The "+todaysPrecip[0]+" ends now."
                    precipStartedCheck = False
            print(fullString)
            if precipStartedCheck and precipDuration > 0:
                precipDuration -= 1
            thisHour += 1
        thisDay += 1
#############
## QUERIES ##
#############
def startMonthQuery():
    print("What month is it?\nPossible months:", monthsAll, "\nPress enter for random")
    while True:
        startingMonth = input().lower()
        if startingMonth in monthsAll:
            break
        elif startingMonth == "":
            startingMonth = random.choice(monthsAll)
            print("Randomly selected "+startingMonth+" as the starting month.")
            break
        else:
            print("This month doesn't exist, use one from the list or leave empty for random.")
            continue
    return startingMonth
def startDayQuery(monthSelected):
    print("What day should we start at?")
    while True:
        startingDaySelect = input()
        if startingDaySelect == "" and monthSelected in months:
            startingDay = random.randint(1,28)
            print("Randomly selected "+str(startingDay)+" as the starting day.")
            break
        elif startingDaySelect == "" and monthSelected in festivals:
            startingDay = random.randint(1,7)
            print("Randomly selected "+str(startingDay)+" as the starting day.")
            break
        try:
            startingDay = int(startingDaySelect)
        except ValueError:
            print("Looks like you haven't put in an integer, please do so.")
            continue
        if monthSelected in months and startingDay < 1 or startingDay > 28:
            print("Only 1-28 are valid for "+monthSelected)
            continue
        elif monthSelected in festivals and startingDay < 1 or startingDay > 7:
            print("Only 1-7 are valid for "+monthSelected)
            continue
        else:
            break
    return startingDay
def genDaysQuery():
    print("How many days do you want to generate forecast for?")
    while True:
        if debug:
            daysGenInput = 2
            return daysGenInput
            break
        else:
            daysGenInput = input()
        if daysGenInput == "":
            daysGenInput = random.randint(1,3)*7
            print("Randomly selected "+str(daysGenInput)+" days to generate.")
            return daysGenInput
            break
        try:
            return int(daysGenInput)
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
        latitudeSelect = input()
        if latitudeSelect == "":
            return random.randint(15,55)
            break
        try:
            int(latitudeSelect)
        except ValueError:
            print("Looks like you haven't put in an integer, please do so.")
            continue
        if int(latitudeSelect) < 15 or int(latitudeSelect) > 55:
            print("Your party is out of bounds with the map then, try again.")
        else:
            break
    return int(latitudeSelect)
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
    return terrainPrompt
###########
## START ##
###########
if debug == False: # We only query for months if debug is set as off.
    startMonth = startMonthQuery()
    startDay = startDayQuery(startMonth)
    daysToGen = genDaysQuery()
    latitude = latitudeQuery()
    terrain = terrainQuery()
else: # When debug is on, we set the parameters automatically or randomly.
    startMonth = str(*random.sample(monthsAll, 1))
    startDay = random.randint(1,7)
    daysToGen = 15
    latitude = random.randint(15,55)
    terrain = "plains"
if int(daysToGen) < 7:
    genDayString = "Generating "+str(daysToGen)+" days of weather"
elif int(daysToGen) >= 7 and int(daysToGen) < 56:
    genDayString = "Generating "+str(int(daysToGen)//7)+" weeks of weather"
elif int(daysToGen) >= 56 and int(daysToGen) < 672:
    genDayString = "Generating "+str(int(daysToGen)//28)+" months of weather"
elif int(daysToGen) >= 672:
    genDayString = "Generating "+str(int(daysToGen)//336)+" years of weather"
else:
    raise Exception("ERROR: Could not determine magnitude of generation in days!")
summaryString = "Summary: "+genDayString+" after "+str(startDay)+" of "+str(startMonth)+" ("+str(seasonCheck(startMonth))+"), common year 576. The location is "+str(terrain)+" at "+str(latitude)+u'\N{DEGREE SIGN}'+"N ("+str(climateCheck(latitude))+" climate)."
print(summaryString)
fullDict = generateEverything(startMonth, startDay, daysToGen, latitude, terrain)
presentationFunction(fullDict, terrain)
print("End of script!")
exit()
## END HERE
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
