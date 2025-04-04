# pong_server.py
import pygame
import socket
import threading
import pickle  # for sending game state
import time

# Networking setup
host = '0.0.0.0'  # listen on all interfaces
port = 5555

# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Waiting for a connection...")
conn, addr = server_socket.accept()
print("Connected to:", addr)

# Pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Server (Player 1)")
clock = pygame.time.Clock()

# Game state
player1 = pygame.Rect(20, 250, 10, 100)
player2 = pygame.Rect(770, 250, 10, 100)
ball = pygame.Rect(390, 290, 20, 20)
ball_speed = [3, 3]
score1 = 0
score2 = 0
hit_count = 0
level = 1
max_level = 5

# Game loop
running = True
client_paddle_move = 0

def receive_client_data():
    global client_paddle_move, running
    while running:
        try:
            data = conn.recv(1024).decode()
            if data == 'UP':
                client_paddle_move = -3
            elif data == 'DOWN':
                client_paddle_move = 3
            else:
                client_paddle_move = 0
        except:
            print("Client disconnected.")
            running = False
            break

threading.Thread(target=receive_client_data, daemon=True).start()

def send_game_state():
    state = {
        "player1": player1.y,
        "player2": player2.y,
        "ball": (ball.x, ball.y),
        "score1": score1,
        "score2": score2,
        "level": level
    }
    conn.send(pickle.dumps(state))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 movement (W/S)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.move_ip(0, -3)
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.move_ip(0, 3)

    # Player 2 movement from client
    if 0 <= player2.y + client_paddle_move <= SCREEN_HEIGHT - player2.height:
        player2.move_ip(0, client_paddle_move)

    # Ball movement
    ball.move_ip(ball_speed)

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed[1] *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1
        hit_count += 1
        if hit_count % 20 == 0 and level < max_level:
            level += 1
            ball_speed[0] *= 1.2
            ball_speed[1] *= 1.2

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball = pygame.Rect(390, 290, 20, 20)
        ball_speed = [3, 3]
        level = 1
        hit_count = 0
    if ball.right >= SCREEN_WIDTH:
        score1 += 1
        ball = pygame.Rect(390, 290, 20, 20)
        ball_speed = [3, 3]
        level = 1
        hit_count = 0

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"{score1} - {score2} | Level {level}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH//2 - 100, 20))
    
    pygame.display.flip()
    clock.tick(60)

    # Send game state to client
    send_game_state()

conn.close()
pygame.quit()
