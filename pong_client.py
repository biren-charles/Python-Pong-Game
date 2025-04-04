# pong_client.py
import pygame
import socket
import pickle

# Connect to server
host = input("Enter server IP: ")  # e.g., 127.0.0.1
port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Client (Player 2)")
clock = pygame.time.Clock()

running = True
move = "NONE"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move = "UP"
    elif keys[pygame.K_DOWN]:
        move = "DOWN"
    else:
        move = "NONE"

    # Send input to server
    client_socket.send(move.encode())

    # Receive and draw game state
    data = client_socket.recv(4096)
    state = pickle.loads(data)

    player1_y = state["player1"]
    player2_y = state["player2"]
    ball_pos = state["ball"]
    score1 = state["score1"]
    score2 = state["score2"]
    level = state["level"]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, player1_y, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(770, player2_y, 10, 100))
    pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(ball_pos[0], ball_pos[1], 20, 20))
    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"{score1} - {score2} | Level {level}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH//2 - 100, 20))

    pygame.display.flip()
    clock.tick(60)

client_socket.close()
pygame.quit()
