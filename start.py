#!/usr/bin/env python3
import os
import subprocess
import time
import signal
import sys
import random
from datetime import datetime

# Define color codes for terminal
COLORS = {
    "BLUE": "\033[1;34m",
    "GREEN": "\033[1;32m",
    "RED": "\033[1;31m",
    "YELLOW": "\033[1;33m",
    "PURPLE": "\033[1;35m",
    "CYAN": "\033[1;36m",
    "WHITE": "\033[1;37m",
    "ORANGE": "\033[1;33m",
    "BOLD": "\033[1m",
    "DIM": "\033[2m",
    "ITALIC": "\033[3m",
    "UNDERLINE": "\033[4m",
    "BG_BLACK": "\033[40m",
    "BG_BLUE": "\033[44m",
    "BG_GREEN": "\033[42m",
    "BG_PURPLE": "\033[45m",
    "END": "\033[0m"
}

# Define categories and their channels
CATEGORIES = {
    "1": {
        "name": "Entertainment",
        "icon": "🎭",
        "color": COLORS["YELLOW"]
    },
    "2": {
        "name": "Movies",
        "icon": "🎬",
        "color": COLORS["RED"]
    },
    "3": {
        "name": "Series",
        "icon": "📺",
        "color": COLORS["BLUE"]
    },
    "4": {
        "name": "News",
        "icon": "📰",
        "color": COLORS["GREEN"]
    },
    "5": {
        "name": "General",
        "icon": "🌐",
        "color": COLORS["PURPLE"]
    }
}

# Define channels and their IDs with additional metadata and category assignment
CHANNELS = {
    "1": {
        "name": "Star Life",
        "id": "1487976954",
        "icon": "🌟",
        "category": "1"  # Entertainment
    },
    "2": {
        "name": "StarPlus",
        "id": "168",
        "icon": "✨",
        "category": "1"  # Entertainment
    },
    "3": {
        "name": "Zee One",
        "id": "1023102509",
        "icon": "🌍",
        "category": "1"  # Entertainment
    },
    "4": {
        "name": "Colors",
        "id": "1529033737",
        "icon": "🌈",
        "category": "1"  # Entertainment
    },
        "5": {
        "name": "PBO",
        "id": "1900548203",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "6": {
        "name": "STAR MOVIES",
        "id": "1490154337",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "7": {
        "name": "Bliss TV",
        "id": "1291168734",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "8": {
        "name": "AMC MOVIES",
        "id": "1023149121",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "9": {
        "name": "ZEE BOLLYMOVIES",
        "id": "759554478",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "10": {
        "name": "FILMBOX ACTION",
        "id": "426003040",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "11": {
        "name": "ST MOVIES",
        "id": "709",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "12": {
        "name": "ZEE CINEMA",
        "id": "206",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "13": {
        "name": "ST MOVIES PLUS",
        "id": "166",
        "icon": "🎭",
        "category": "2"  # Movies
    },
    "14": {
        "name": "Afro Novelas",
        "id": "1853457481",
        "icon": "📺",
        "category": "3"  # Series
    },
    "15": {
        "name": "TDC",
        "id": "1839721943",
        "icon": "📺",
        "category": "3"  # Series
    },
    "16": {
        "name": "STAR LIFE",
        "id": "1487976954",
        "icon": "📺",
        "category": "3"  # Series
    },
    "17": {
        "name": "ST NOLLYWOOD F",
        "id": "1468833215",
        "icon": "📺",
        "category": "3"  # Series
    },
    "18": {
        "name": "PASSION NOVELAS",
        "id": "1023196140",
        "icon": "📺",
        "category": "3"  # Series
    },
    "19": {
        "name": "ZEE ONE",
        "id": "1023102509",
        "icon": "📺",
        "category": "3"  # Series
    },
    "20": {
        "name": "ZEE MAGIC",
        "id": "1021478122",
        "icon": "📺",
        "category": "3"  # Series
    },
    "21": {
        "name": "PASSION BOLLYWOOD",
        "id": "601967670",
        "icon": "📺",
        "category": "3"  # Series
    },
    "22": {
        "name": "MAKULA TV",
        "id": "257840078",
        "icon": "📺",
        "category": "3"  # Series
    },
    "23": {
        "name": "ST NOVELA E",
        "id": "168556647",
        "icon": "📺",
        "category": "3"  # Series
    },
    "24": {
        "name": "ST NOVELA F PLUS",
        "id": "698",
        "icon": "📺",
        "category": "3"  # Series
    },
    "25": {
        "name": "ST NOVELA E PLUS",
        "id": "697",
        "icon": "📺",
        "category": "3"  # Series
    },
    "26": {
        "name": "NINA NOVELAS F",
        "id": "650",
        "icon": "📺",
        "category": "3"  # Series
    },
    "27": {
        "name": "ST SINO DRAMA",
        "id": "456",
        "icon": "📺",
        "category": "3"  # Series
    },
    "28": {
        "name": "ST NOVELA F",
        "id": "402",
        "icon": "📺",
        "category": "3"  # Series
    },
    "29": {
        "name": "STAR PLUS",
        "id": "168",
        "icon": "📺",
        "category": "3"  # Series
    },
    "30": {
        "name": "SKY NEWS",
        "id": "1840045634",
        "icon": "📰",
        "category": "4"  # News
    },
    "31": {
        "name": "RT",
        "id": "755591261",
        "icon": "📰",
        "category": "4"  # News
    },
    "32": {
        "name": "BFM TV",
        "id": "723408784",
        "icon": "📰",
        "category": "4"  # News
    },
    "33": {
        "name": "RT FRANCE",
        "id": "301153275",
        "icon": "📰",
        "category": "4"  # News
    },
    "34": {
        "name": "AFRICA NEWS",
        "id": "549",
        "icon": "📰",
        "category": "4"  # News
    },
    "35": {
        "name": "FRANCE 24",
        "id": "504",
        "icon": "📰",
        "category": "4"  # News
    },
    "36": {
        "name": "CGTN F",
        "id": "500",
        "icon": "📰",
        "category": "4"  # News
    },
    "37": {
        "name": "FRANCE 24 E",
        "id": "346",
        "icon": "📰",
        "category": "4"  # News
    },
    "38": {
        "name": "AIT",
        "id": "224",
        "icon": "📰",
        "category": "4"  # News
    },
    "39": {
        "name": "AL JAZEERA",
        "id": "217",
        "icon": "📰",
        "category": "4"  # News
    },
    "40": {
        "name": "CGTN",
        "id": "216",
        "icon": "📰",
        "category": "4"  # News
    },
    "41": {
        "name": "TVC NEWS",
        "id": "198",
        "icon": "📰",
        "category": "4"  # News
    },
    "42": {
        "name": "CHANNELS",
        "id": "185",
        "icon": "📰",
        "category": "4"  # News
    },
    "43": {
        "name": "NTA NEWS 24",
        "id": "175",
        "icon": "📰",
        "category": "4"  # News
    },
    "44": {
        "name": "FOX NEWS",
        "id": "149",
        "icon": "📰",
        "category": "4"  # News
    },
    "45": {
        "name": "BBC WORLD NEWS",
        "id": "139",
        "icon": "📰",
        "category": "4"  # News
    },
    "46": {
        "name": "TVM",
        "id": "2147205607",
        "icon": "📡",
        "category": "5"  # General
    },
    "47": {
        "name": "CINARC TV",
        "id": "1751324560",
        "icon": "📡",
        "category": "5"  # General
    },
    "48": {
        "name": "TV BREIZH",
        "id": "1639653351",
        "icon": "📡",
        "category": "5"  # General
    },
    "49": {
        "name": "ST NOLLYWOOD PLUS",
        "id": "1572293892",
        "icon": "📡",
        "category": "5"  # General
    },
    "50": {
        "name": "COLORS",
        "id": "1529033737",
        "icon": "📡",
        "category": "5"  # General
    },
    "51": {
        "name": "NIGBATI TV",
        "id": "1235400314",
        "icon": "📡",
        "category": "5"  # General
    },
    "52": {
        "name": "CBS REALITY",
        "id": "1204051782",
        "icon": "📡",
        "category": "5"  # General
    },
    "53": {
        "name": "SPARK TV",
        "id": "1060426602",
        "icon": "📡",
        "category": "5"  # General
    },
    "54": {
        "name": "MAX TV",
        "id": "1023247844",
        "icon": "📡",
        "category": "5"  # General
    },
    "55": {
        "name": "Malaika TV",
        "id": "750186374",
        "icon": "📡",
        "category": "5"  # General
    },
    "56": {
        "name": "LA3",
        "id": "526733059",
        "icon": "📡",
        "category": "5"  # General
    },
    "57": {
        "name": "ST Swahili Plus",
        "id": "343829804",
        "icon": "📡",
        "category": "5"  # General
    },
    "58": {
        "name": "UP TV",
        "id": "73406933",
        "icon": "📡",
        "category": "5"  # General
    },
    "59": {
        "name": "TV3 Ghana",
        "id": "682",
        "icon": "📡",
        "category": "5"  # General
    },
    "60": {
        "name": "JOY PRIME",
        "id": "679",
        "icon": "📡",
        "category": "5"  # General
    },
    "61": {
        "name": "ZNBC TV1",
        "id": "662",
        "icon": "📡",
        "category": "5"  # General
    },
    "62": {
        "name": "CRTV",
        "id": "647",
        "icon": "📡",
        "category": "5"  # General
    },
    "63": {
        "name": "SANYUKA TV",
        "id": "619",
        "icon": "📡",
        "category": "5"  # General
    },
    "64": {
        "name": "AFOREVO TV",
        "id": "615",
        "icon": "📡",
        "category": "5"  # General
    },
    "65": {
        "name": "ST YORUBA",
        "id": "598",
        "icon": "📡",
        "category": "5"  # General
    },
    "66": {
        "name": "TVM1",
        "id": "532",
        "icon": "📡",
        "category": "5"  # General
    },
    "67": {
        "name": "E! ENG",
        "id": "498",
        "icon": "📡",
        "category": "5"  # General
    },
    "68": {
        "name": "RTS1",
        "id": "483",
        "icon": "📡",
        "category": "5"  # General
    },
    "69": {
        "name": "K24",
        "id": "468",
        "icon": "📡",
        "category": "5"  # General
    },
    "70": {
        "name": "ST KUNGFU",
        "id": "455",
        "icon": "📡",
        "category": "5"  # General
    },
    "71": {
        "name": "TV5 MONDE",
        "id": "381",
        "icon": "📡",
        "category": "5"  # General
    },
    "72": {
        "name": "KBC",
        "id": "316",
        "icon": "📡",
        "category": "5"  # General
    },
    "73": {
        "name": "ORISUN",
        "id": "196",
        "icon": "📡",
        "category": "5"  # General
    },
    "74": {
        "name": "ST DADIN KOWA",
        "id": "159",
        "icon": "📡",
        "category": "5"  # General
    },
    "75": {
        "name": "TLC",
        "id": "132",
        "icon": "📡",
        "category": "5"  # General
    },
    "76": {
        "name": "REAL MADRID TV",
        "id": "1935265459",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "77": {
        "name": "ST Beta Sports",
        "id": "1868819766",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "78": {
        "name": "W-SPORT",
        "id": "1296220504",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "79": {
        "name": "ST MANIA",
        "id": "1241908189",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "80": {
        "name": "FUFA Tv",
        "id": "1152198097",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "81": {
        "name": "ST ADEPA",
        "id": "1026432896",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "82": {
        "name": "MUTV",
        "id": "960223060",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "83": {
        "name": "SPORTYTV",
        "id": "6754969",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "84": {
        "name": "GTV SPORTS PLUS",
        "id": "681",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "85": {
        "name": "ST WORLD FOOTBALL HD",
        "id": "649",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "86": {
        "name": "ST SPORTS ARENA",
        "id": "445",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "87": {
        "name": "ST SPORTS LIFE",
        "id": "443",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "88": {
        "name": "ST SPORTS PREMIUM",
        "id": "302",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "89": {
        "name": "ST SPORTS FOCUS",
        "id": "266",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "90": {
        "name": "ESPN 2",
        "id": "151",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "91": {
        "name": "ESPN",
        "id": "150",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "92": {
        "name": "BLAST Premier",
        "id": "1788919175",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "93": {
        "name": "Jrs Sports",
        "id": "1730472630",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "94": {
        "name": "AFRSports888",
        "id": "1215073341",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "95": {
        "name": "European Cricket",
        "id": "1042343358",
        "icon": "⚽",
        "category": "6"  # Sports
    },
    "96": {
        "name": "UE SPORTS",
        "id": "180212600",
        "icon": "⚽",
        "category": "6"  # Sports
    }
}

# Quality options
QUALITY_OPTIONS = {
    "1": {
        "name": "HD",
        "streamlink_option": "best",
        "icon": "🔹"
    },
    "2": {
        "name": "SD",
        "streamlink_option": "worst",
        "icon": "🔸"
    }
}

PORT = 8080  # Fixed port for Streamlink
running_process = None  # Global variable to store the streamlink process

# Fancy borders
BORDERS = {
    "horizontal": "━",
    "vertical": "┃",
    "top_left": "┏",
    "top_right": "┓",
    "bottom_left": "┗",
    "bottom_right": "┛",
    "t_down": "┳",
    "t_up": "┻",
    "t_right": "┣",
    "t_left": "┫",
    "cross": "╋"
}

# Animation frames for loading
SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

# [Rest of the functions remain unchanged: animate_text, animate_spinner, find_streamlink_pid, kill_streamlink, draw_progress_bar, start_stream, draw_box, print_category_card, print_channel_card, print_quality_card, print_header, print_category_menu, print_channel_menu, print_quality_menu, cleanup_and_exit, handle_exit_signal, main]

def animate_text(text, color=COLORS["CYAN"], delay=0.01):
    """Animate text being typed out"""
    for char in text:
        sys.stdout.write(f"{color}{char}{COLORS['END']}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_spinner(text, duration=3, color=COLORS["YELLOW"]):
    """Show a spinner animation while waiting"""
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        frame = SPINNER_FRAMES[i % len(SPINNER_FRAMES)]
        sys.stdout.write(f"\r{color}{frame} {text}...{COLORS['END']}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")
    sys.stdout.flush()

def find_streamlink_pid():
    """Find Streamlink PID if running"""
    try:
        result = subprocess.run(
            ["ps", "aux"], 
            stdout=subprocess.PIPE, 
            text=True, 
            check=True
        )
        for line in result.stdout.splitlines():
            if "streamlink" in line and "grep" not in line:
                return line.split()[1]
        return None
    except subprocess.SubprocessError:
        return None

def kill_streamlink():
    """Kill existing Streamlink process if running"""
    global running_process
    
    if running_process:
        try:
            running_process.terminate()
            running_process.wait(timeout=3)
            running_process = None
            return True
        except:
            pass
    
    pid = find_streamlink_pid()
    if pid:
        print(f"{COLORS['RED']}🔴 Stopping existing Streamlink process (PID: {pid})...{COLORS['END']}")
        try:
            os.kill(int(pid), signal.SIGTERM)
            animate_spinner("Terminating process", 2, COLORS["RED"])
            return True
        except:
            print(f"{COLORS['RED']}⚠️ Failed to kill process. Please terminate manually.{COLORS['END']}")
    return False

def draw_progress_bar(progress, width=40):
    """Draw a colorful progress bar"""
    filled_width = int(progress * width)
    bar = ""
    for i in range(width):
        if i < filled_width:
            if i < width * 0.3:
                color = COLORS["GREEN"]
            elif i < width * 0.6:
                color = COLORS["YELLOW"]
            else:
                color = COLORS["RED"]
            bar += f"{color}█{COLORS['END']}"
        else:
            bar += f"{COLORS['DIM']}▒{COLORS['END']}"
    
    print(f"  {bar} {int(progress * 100)}%")

def start_stream(channel_info, quality_info):
    """Start Streamlink and launch MX Player"""
    global running_process
    
    channel_name = channel_info["name"]
    channel_id = channel_info["id"]
    channel_icon = channel_info["icon"]
    
    quality_name = quality_info["name"]
    quality_option = quality_info["streamlink_option"]
    quality_icon = quality_info["icon"]
    
    print(f"\n{COLORS['GREEN']}{BORDERS['top_left']}{BORDERS['horizontal'] * 60}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{COLORS['GREEN']}{BORDERS['vertical']}{COLORS['END']} {COLORS['BOLD']}{channel_icon} Now streaming: {channel_name} ({quality_icon} {quality_name}){COLORS['END']} {' ' * (37 - len(channel_name) - len(quality_name))} {COLORS['GREEN']}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{COLORS['GREEN']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * 60}{BORDERS['bottom_right']}{COLORS['END']}\n")
    
    kill_streamlink()

    print(f"{COLORS['CYAN']}🔄 Initializing Streamlink...{COLORS['END']}")
    
    for i in range(5):
        draw_progress_bar((i+1)/5)
        time.sleep(0.2)
    
    running_process = subprocess.Popen(
        ["streamlink", "--plugin-dirs", "~/", f"startimes://channel_id={channel_id}", quality_option,
         "--player-external-http", "--player-external-http-port", str(PORT)],
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )

    animate_spinner("Preparing stream", 3, COLORS["CYAN"])

    print(f"{COLORS['YELLOW']}🎬 Opening MX Player Pro...{COLORS['END']}")
    os.system(f"am start --user 0 -n com.mxtech.videoplayer.pro/.ActivityScreen -d http://127.0.0.1:{PORT}/")
    
    print(f"\n{COLORS['GREEN']}✅ Stream started successfully!{COLORS['END']}")
    print(f"{COLORS['DIM']}   Stream available at http://127.0.0.1:{PORT}/{COLORS['END']}")
    print(f"{COLORS['DIM']}   Quality: {quality_name} ({quality_option}){COLORS['END']}")

def draw_box(text, width, style="single", padding=1, color=COLORS["BLUE"]):
    """Draw a fancy box with text inside"""
    content_width = width - 2 - (padding * 2)
    
    print(f"{color}{BORDERS['top_left']}{BORDERS['horizontal'] * width}{BORDERS['top_right']}{COLORS['END']}")
    
    for _ in range(padding):
        print(f"{color}{BORDERS['vertical']}{' ' * width}{BORDERS['vertical']}{COLORS['END']}")
    
    print(f"{color}{BORDERS['vertical']}{' ' * ((width - len(text)) // 2)}{COLORS['END']}{COLORS['BOLD']}{text}{COLORS['END']}{color}{' ' * ((width - len(text) + 1) // 2)}{BORDERS['vertical']}{COLORS['END']}")
    
    for _ in range(padding):
        print(f"{color}{BORDERS['vertical']}{' ' * width}{BORDERS['vertical']}{COLORS['END']}")
    
    print(f"{color}{BORDERS['bottom_left']}{BORDERS['horizontal'] * width}{BORDERS['bottom_right']}{COLORS['END']}")

def print_category_card(key, category_info, selected=False):
    """Print a fancy category card"""
    name = category_info["name"]
    icon = category_info["icon"]
    color = category_info["color"]
    
    border_color = COLORS["PURPLE"] if selected else color
    bg_color = COLORS["BG_PURPLE"] if selected else ""
    
    width = 25
    
    print(f"{border_color}{BORDERS['top_left']}{BORDERS['horizontal'] * width}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['vertical']}{COLORS['END']}{bg_color} {COLORS['BOLD']}{key}.{COLORS['END']}{bg_color} {icon} {name}{' ' * (width - len(name) - 5)}{COLORS['END']} {border_color}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['bottom_left']}{BORDERS['horizontal'] * width}{BORDERS['bottom_right']}{COLORS['END']}")

def print_channel_card(key, channel_info, selected=False):
    """Print a fancy channel card"""
    name = channel_info["name"]
    icon = channel_info["icon"]
    category_id = channel_info["category"]
    category_color = CATEGORIES[category_id]["color"]
    
    border_color = COLORS["PURPLE"] if selected else category_color
    bg_color = COLORS["BG_BLUE"] if selected else ""
    
    width = 25
    
    print(f"{border_color}{BORDERS['top_left']}{BORDERS['horizontal'] * width}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['vertical']}{COLORS['END']}{bg_color} {COLORS['BOLD']}{key}.{COLORS['END']}{bg_color} {icon} {name}{' ' * (width - len(name) - 5)}{COLORS['END']} {border_color}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['bottom_left']}{BORDERS['horizontal'] * width}{BORDERS['bottom_right']}{COLORS['END']}")

def print_quality_card(key, quality_info, selected=False):
    """Print a fancy quality option card"""
    name = quality_info["name"]
    option = quality_info["streamlink_option"]
    icon = quality_info["icon"]
    
    border_color = COLORS["PURPLE"] if selected else COLORS["YELLOW"]
    bg_color = COLORS["BG_GREEN"] if selected else ""
    
    width = 20
    
    print(f"{border_color}{BORDERS['top_left']}{BORDERS['horizontal'] * width}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['vertical']}{COLORS['END']}{bg_color} {COLORS['BOLD']}{key}.{COLORS['END']}{bg_color} {icon} {name}{' ' * (width - len(name) - 5)}{COLORS['END']} {border_color}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['t_right']}{BORDERS['horizontal'] * width}{BORDERS['t_left']}{COLORS['END']}")
    option_display = f"Quality: {option}"
    print(f"{border_color}{BORDERS['vertical']}{COLORS['END']}{bg_color} {option_display}{' ' * (width - len(option_display) - 1)}{COLORS['END']} {border_color}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{border_color}{BORDERS['bottom_left']}{BORDERS['horizontal'] * width}{BORDERS['bottom_right']}{COLORS['END']}")

def print_header():
    """Print a stylish header"""
    os.system("clear")
    
    current_time = datetime.now().strftime("%H:%M:%S")
    title = "📺 STARTIMES STREAMING HUB 📺"
    width = 60
    
    print(f"{COLORS['BLUE']}{BORDERS['top_left']}{BORDERS['horizontal'] * 20} {current_time} {BORDERS['horizontal'] * (width - 22 - len(current_time))}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{COLORS['BLUE']}{BORDERS['vertical']}{COLORS['END']} {COLORS['BOLD']}{title}{COLORS['END']} {' ' * (width - len(title) - 3)} {COLORS['BLUE']}{BORDERS['vertical']}{COLORS['END']}")
    subtitle = "Stream your favorite channels with style"
    print(f"{COLORS['BLUE']}{BORDERS['vertical']}{COLORS['END']} {COLORS['ITALIC']}{subtitle}{COLORS['END']} {' ' * (width - len(subtitle) - 3)} {COLORS['BLUE']}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{COLORS['BLUE']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * width}{BORDERS['bottom_right']}{COLORS['END']}")
    print()

def print_category_menu():
    """Print the category selection menu with cards"""
    animate_text("SELECT A CATEGORY:", COLORS["CYAN"], 0.005)
    print()
    
    row = []
    for key, category_info in CATEGORIES.items():
        row.append((key, category_info))
        if len(row) == 2:
            for i, (cat_key, cat_info) in enumerate(row):
                print_category_card(cat_key, cat_info, selected=False)
                if i < len(row) - 1:
                    print(" ", end="")
            print("\n")
            row = []
    
    if row:
        for i, (cat_key, cat_info) in enumerate(row):
            print_category_card(cat_key, cat_info, selected=False)
            if i < len(row) - 1:
                print(" ", end="")
        print("\n")
    
    print(f"\n{COLORS['PURPLE']}{BORDERS['top_left']}{BORDERS['horizontal'] * 50}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']} Enter category number or type '{COLORS['BOLD']}exit{COLORS['END']}' to quit {' ' * 8} {COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * 50}{BORDERS['bottom_right']}{COLORS['END']}")
    print(f"\n{COLORS['GREEN']}🔷 Your choice: {COLORS['END']}", end="")

def print_channel_menu(category_id=None):
    """Print the channel selection menu with cards"""
    if category_id and category_id != "5":
        category_name = CATEGORIES[category_id]["name"]
        animate_text(f"SELECT A CHANNEL FROM {category_name.upper()}:", COLORS["YELLOW"], 0.005)
        filtered_channels = {k: v for k, v in CHANNELS.items() if v["category"] == category_id}
    else:
        animate_text("SELECT A CHANNEL TO WATCH:", COLORS["YELLOW"], 0.005)
        filtered_channels = CHANNELS
    
    print()
    
    row = []
    for key, channel_info in filtered_channels.items():
        row.append((key, channel_info))
        if len(row) == 2:
            for i, (ch_key, ch_info) in enumerate(row):
                print_channel_card(ch_key, ch_info, selected=False)
                if i < len(row) - 1:
                    print(" ", end="")
            print("\n")
            row = []
    
    if row:
        for i, (ch_key, ch_info) in enumerate(row):
            print_channel_card(ch_key, ch_info, selected=False)
            if i < len(row) - 1:
                print(" ", end="")
        print("\n")
    
    print(f"\n{COLORS['PURPLE']}{BORDERS['top_left']}{BORDERS['horizontal'] * 50}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']} Enter channel number or type '{COLORS['BOLD']}back{COLORS['END']}' to go back {' ' * 7} {COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * 50}{BORDERS['bottom_right']}{COLORS['END']}")
    print(f"\n{COLORS['GREEN']}🔷 Your choice: {COLORS['END']}", end="")

def print_quality_menu():
    """Print the quality selection menu with cards"""
    animate_text("SELECT STREAMING QUALITY:", COLORS["YELLOW"], 0.005)
    print()
    
    for key, quality_info in QUALITY_OPTIONS.items():
        print_quality_card(key, quality_info)
        print()
    
    print(f"\n{COLORS['PURPLE']}{BORDERS['top_left']}{BORDERS['horizontal'] * 50}{BORDERS['top_right']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']} Enter quality number or type '{COLORS['BOLD']}back{COLORS['END']}' to go back {' ' * 7} {COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']}")
    print(f"{COLORS['PURPLE']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * 50}{BORDERS['bottom_right']}{COLORS['END']}")
    print(f"\n{COLORS['GREEN']}🔷 Your choice: {COLORS['END']}", end="")

def cleanup_and_exit():
    """Clean up and exit the program with style"""
    print(f"\n{COLORS['YELLOW']}👋 Exiting...{COLORS['END']}")
    
    if kill_streamlink():
        print(f"{COLORS['GREEN']}✅ Streamlink process terminated.{COLORS['END']}")
    
    animate_spinner("Cleaning up resources", 1.5, COLORS["CYAN"])
    
    print()
    draw_box("All processes cleaned up. Goodbye!", 40, "double", 1, COLORS["GREEN"])
    print()
    
    sys.exit(0)

def handle_exit_signal(signum, frame):
    """Handle exit signals like Ctrl+C"""
    print("\nCaught interrupt signal.")
    cleanup_and_exit()

def main():
    signal.signal(signal.SIGINT, handle_exit_signal)
    signal.signal(signal.SIGTERM, handle_exit_signal)

    os.system("clear")
    animate_text("WELCOME TO", COLORS["YELLOW"], 0.01)
    draw_box("STARTIMES STREAMING HUB", 40, "double", 1, COLORS["BLUE"])
    time.sleep(1)
    
    try:
        while True:
            print_header()
            print_category_menu()
            
            category_choice = input().strip().lower()
            
            if category_choice == 'exit' or category_choice == '':
                cleanup_and_exit()
            
            if category_choice not in CATEGORIES:
                print(f"\n{COLORS['RED']}⚠️ Invalid choice. Please try again.{COLORS['END']}")
                time.sleep(1.5)
                continue
            
            while True:
                os.system("clear")
                print_header()
                
                print_category_card(category_choice, CATEGORIES[category_choice], selected=True)
                print()
                
                print_channel_menu(category_choice)
                
                channel_choice = input().strip().lower()
                
                if channel_choice == 'back':
                    break
                
                if channel_choice == 'exit':
                    cleanup_and_exit()
                
                if channel_choice not in CHANNELS:
                    print(f"\n{COLORS['RED']}⚠️ Invalid choice. Please try again.{COLORS['END']}")
                    time.sleep(1.5)
                    continue
                
                if category_choice != "5" and CHANNELS[channel_choice]["category"] != category_choice:
                    print(f"\n{COLORS['RED']}⚠️ This channel is not in the selected category.{COLORS['END']}")
                    time.sleep(1.5)
                    continue
                
                os.system("clear")
                print_header()
                print_channel_card(channel_choice, CHANNELS[channel_choice], selected=True)
                print()
                print_quality_menu()
                
                quality_choice = input().strip().lower()
                
                if quality_choice == 'back':
                    continue
                
                if quality_choice == 'exit':
                    cleanup_and_exit()
                    
                if quality_choice not in QUALITY_OPTIONS:
                    print(f"\n{COLORS['RED']}⚠️ Invalid quality. Please try again.{COLORS['END']}")
                    time.sleep(1.5)
                    continue
                
                os.system("clear")
                print_header()
                animate_text("CHANNEL & QUALITY SELECTED:", COLORS["GREEN"], 0.01)
                print()
                print_channel_card(channel_choice, CHANNELS[channel_choice], selected=True)
                print()
                print_quality_card(quality_choice, QUALITY_OPTIONS[quality_choice], selected=True)
                print()
                
                start_stream(CHANNELS[channel_choice], QUALITY_OPTIONS[quality_choice])
                
                print(f"\n{COLORS['PURPLE']}{BORDERS['top_left']}{BORDERS['horizontal'] * 50}{BORDERS['top_right']}{COLORS['END']}")
                print(f"{COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']} Press Enter to return to menu or type 'exit' to quit {COLORS['PURPLE']}{BORDERS['vertical']}{COLORS['END']}")
                print(f"{COLORS['PURPLE']}{BORDERS['bottom_left']}{BORDERS['horizontal'] * 50}{BORDERS['bottom_right']}{COLORS['END']}")
                print(f"\n{COLORS['GREEN']}🔷 Your choice: {COLORS['END']}", end="")
                
                choice = input().strip().lower()
                if choice == 'exit':
                    cleanup_and_exit()
                else:
                    break
                
    except KeyboardInterrupt:
        cleanup_and_exit()
    except Exception as e:
        print(f"\n{COLORS['RED']}⚠️ An error occurred: {e}{COLORS['END']}")
        cleanup_and_exit()

if __name__ == "__main__":
    main()