import streamlit as st
import json
import os
from playsound import playsound

# File to store global data
GLOBAL_DATA_FILE = "global_data.json"

# Variables

# Initialize session count
if "count" not in st.session_state:
    st.session_state.count = 0

# Initialize session multiplier
if "multiplier" not in st.session_state:
    st.session_state.multiplier = 1

# Initialize session show_double_button
if "show_double_button" not in st.session_state:
    st.session_state.show_double_button = True

def global_data_setup():
    default_data = {"count": 0, "real_mouse_clicks": 0}
    if not os.path.exists(GLOBAL_DATA_FILE):
        # Create the file if it doesn't exist
        with open(GLOBAL_DATA_FILE, "w") as f:
            json.dump(default_data, f)
    else:
        # Check if all keys are present
        with open(GLOBAL_DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # If the file is corrupted, reinitialize it
                data = {}
        # Update missing keys
        for key, value in default_data.items():
            if key not in data:
                data[key] = value
        # Save updated data
        with open(GLOBAL_DATA_FILE, "w") as f:
            json.dump(data, f)




# Function to read real mouse clicks count
def get_global_real_mouse_clicks():
    # if not os.path.exists(GLOBAL_DATA_FILE):
    #     with open(GLOBAL_DATA_FILE, "w") as f:
    #         json.dump({"real_mouse_clicks": 0}, f)
    with open(GLOBAL_DATA_FILE, "r") as f:
        data = json.load(f)
    return data["real_mouse_clicks"]

# def update_global_real_mouse_clicks():
#     count = get_global_real_mouse_clicks() + 1
#     with open(GLOBAL_DATA_FILE, "w") as f:
#         json.dump({"real_mouse_clicks": count}, f)
#     return count
def update_global_real_mouse_clicks():
    with open(GLOBAL_DATA_FILE, "r") as f:
        data = json.load(f)
    # Safeguard against missing keys
    if "real_mouse_clicks" not in data:
        data["real_mouse_clicks"] = 0
    data["real_mouse_clicks"] += 1
    with open(GLOBAL_DATA_FILE, "w") as f:
        json.dump(data, f)
    return data["real_mouse_clicks"]



# Function to read global count
def get_global_count():
    # if not os.path.exists(GLOBAL_DATA_FILE):
    #     with open(GLOBAL_DATA_FILE, "w") as f:
    #         json.dump({"count": 0}, f)
    with open(GLOBAL_DATA_FILE, "r") as f:
        data = json.load(f)
    return data["count"]

# Function to update global count
# def update_global_count():
#     count = get_global_count() + 1 * st.session_state.multiplier
#     with open(GLOBAL_DATA_FILE, "w") as f:
#         json.dump({"count": count}, f)
#     return count
def update_global_count():
    with open(GLOBAL_DATA_FILE, "r") as f:
        data = json.load(f)
    # Safeguard against missing keys
    if "count" not in data:
        data["count"] = 0
    data["count"] += 1 * st.session_state.multiplier
    with open(GLOBAL_DATA_FILE, "w") as f:
        json.dump(data, f)
    return data["count"]



global_data_setup()

st.title("how much you miss her???")

# Increment session count
if st.button("i miss her"):
    st.session_state.count += 1 * st.session_state.multiplier
    global_count = update_global_count()
    real_mouse_clicks = update_global_real_mouse_clicks()
else:
    global_count = get_global_count()
    real_mouse_clicks = get_global_real_mouse_clicks()

# Display counts
st.write(f"you miss her **{st.session_state.count}**")
st.write(f"global miss hers **{global_count}**")
st.write(f"global real mouse clicks **{real_mouse_clicks}**")

if st.session_state.count == 10:
    playsound("sounds\Get out.mp3")
elif st.session_state.count >= 40 and st.session_state.show_double_button:
    if st.button("double i miss her"):
        st.session_state.multiplier *= 2
        st.session_state.show_double_button = False
        playsound("sounds\Oh my god bruh.mp3")
elif st.session_state.count == 100:
    playsound("sounds\Get out.mp3")

#if global_count >= 675 and global_count <= 730:
    

# if(st.session_state.show_double_button):
#     if st.button("double i miss her"):
#         playsound("Oh my god bruh, oh hell naw man wtf Audio.mp3")
#         st.session_state.multiplier *= 2
#         st.session_state.show_double_button = False