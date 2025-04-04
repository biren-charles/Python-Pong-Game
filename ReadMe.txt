# Pong Game - Network Python Project 🎮

A 2-Player Pong game using **Python** and **Sockets**, created as part of the Networks 2 lab assignment.

##  Multiplayer Features
- 2 players over local network (LAN / Wi-Fi / mobile hotspot) (tried out over Ethernet LAN)
- Real-time gameplay using TCP sockets
- Host acts as the game server
- Second player connects as client

##  Files
- `pong_server.py` → to be run on host machine (Player 1)
- `pong_client.py` → to be run on second device (Player 2)

##  Requirements
- Python 3.x
- Pygame


BEFORE RUNNING THE GAME
(make sure to have python installed == download python online and "add to PATH" during installation)
(make sure to have pygame installed == in console write "pip install pygame")
there is 2 files, the pong_server.py file must be on the server device; the pong_client.py file must be on the client device 

##  HOW TO RUN THE GAME 

### Server file (Player 1)
1. Connect both devices to same LAN or hotspot
2. Run (in terminal on device 1) :

python pong_server.py

it will display : waiting for connection.... 
3. Wait for client to connect

### Client (Player 2)
1. Run (in terminal on device 2) : 

python pong_client.py

it will prompt the user to input the IP adress of the previously started server 
2. Enter **server's IP address** - this can be found using ipconfig and then reading ipv4 adress of the server. 
on the connecting laptop u can try the address out using "ping [adress]"

Once the adress is input the game will instantanously launch on both devices, make sure to be ready as the game IMMEDIATLY begins.

---

## 🎮 Controls
- Player 1: `W` / `S` (device 1)
- Player 2: `Arrow Up` / `Arrow Down` (device 2)

## ⚙️ Features
- Score tracking
- Level system (ball speed increases) after 10 hits (on each side)
- Ball bounce & collision detection
- Win condition logic
- Game resets correctly after someone score

## 📌 Notes
- Make sure Python is allowed through firewall on the server device
- Ensure both machines are connected on the same **local network**
- When the Game resets the ball always starts towards the right side on the same direction. In a future version this should be randomized

---

## 👨‍💻 Authors
Charles Biren 

---

> © Charles BIREN aka Charlie BIREN aka Schnötzke – University of Luxembourg