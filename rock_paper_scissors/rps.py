import pygame
from sys import exit
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, is_player=True):
        super().__init__()
        self.paused = False
        #initial animation
        if is_player:
            self.hand_frame1 = pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha()
            self.hand_frame2 = pygame.image.load(r"D:\Codsoft\rps\hand\rock1.png").convert_alpha()
            self.hand_frame3 = pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha()
            #for update hand
            self.hand_images = {
            "Rock": pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha(),
            "Paper": pygame.image.load(r"D:\Codsoft\rps\hand\paper.png").convert_alpha(),
            "Scissors": pygame.image.load(r"D:\Codsoft\rps\hand\scissors.png").convert_alpha()
        }
        else:
            # flipped hand images for computer
            self.hand_frame1 = pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha(), True, False)
            self.hand_frame2 = pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\rock1.png").convert_alpha(), True, False)
            self.hand_frame3 = pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha(), True, False)
            #for update hand
            self.hand_images = {
            "Rock": pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\rock.png").convert_alpha(),True, False),
            "Paper": pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\paper.png").convert_alpha(),True, False),
            "Scissors":  pygame.transform.flip(pygame.image.load(r"D:\Codsoft\rps\hand\scissors.png").convert_alpha(), True, False)
        }
        self.hand_frame = [self.hand_frame1, self.hand_frame2, self.hand_frame3]
        self.hand_index = 0
        self.screen = screen
        self.is_player = is_player
        
        hand_surf = self.hand_frame[self.hand_index]
        hand_surf = pygame.transform.scale(hand_surf, (300, 300))
        if self.is_player:
            self.hand_rect = hand_surf.get_rect(midbottom=(self.screen.get_width() - 120, self.screen.get_height() - 120)) 
        else:
            self.hand_rect = hand_surf.get_rect(midbottom=(120, self.screen.get_height() - 120)) 

    def hand_animation(self):
        if not self.paused:  # Only update animation if not paused
            self.hand_index += 0.07
            if self.hand_index >= len(self.hand_frame):
                self.hand_index = 0
            self.hand_surf = self.hand_frame[int(self.hand_index)]
            self.hand_surf = pygame.transform.scale(self.hand_surf, (300, 300))  
            if self.is_player:
                self.hand_rect = self.hand_surf.get_rect(midbottom=(self.screen.get_width() - 120, self.screen.get_height() - 120))  # Move to the right of the screen
            else:
                self.hand_rect = self.hand_surf.get_rect(midbottom=(120, self.screen.get_height() - 120))  # Move to the left of the screen

    def update(self):
        self.hand_animation()
    
    def update_hand(self, choice):
        self.paused = True
        self.choice = choice
        self.hand_surf = self.hand_images[choice]
        self.hand_surf = pygame.transform.scale(self.hand_surf, (300, 300))
        if self.is_player:
            self.hand_rect = self.hand_surf.get_rect(midbottom=(self.screen.get_width() - 120, self.screen.get_height() - 120))
        else:
            self.hand_rect = self.hand_surf.get_rect(midbottom=(120, self.screen.get_height() - 120))
        pygame.time.set_timer(pygame.USEREVENT, 800)   

def draw_text(text, font, color, x, y, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def calc_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!", player_choice, computer_choice
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!", player_choice, computer_choice
    else:
        return "Computer wins!", player_choice, computer_choice

def draw_scores(player_score, computer_score, font, screen_width, surface):
    player_score_text = f"Player Score: {player_score}"
    comp_score_text = f"Computer Score: {computer_score}"
    draw_text(player_score_text, font, WHITE, 600, 15, surface)
    draw_text(comp_score_text, font, WHITE, 190, 15, surface)

def draw_round_result_text(round_result, player_choice, computer_choice):
    player_result_surface = f_font.render(f"Player chose: {player_choice}", True, WHITE)
    comp_result_surface = f_font.render(f"Computer chose: {computer_choice}", True, WHITE)
    result_surface = f_font.render(f"{round_result}", True, WHITE)
    player_result_rect = player_result_surface.get_rect(center=(600, 60))
    screen.blit(player_result_surface, player_result_rect)
    comp_result_rect = comp_result_surface.get_rect(center=(195, 60))
    screen.blit(comp_result_surface, comp_result_rect)
    result_rect = result_surface.get_rect(center=(400, 173))
    screen.blit(result_surface, result_rect)


def display_result(player_score, computer_score):
    display_bg = pygame.image.load(r"D:\Codsoft\rps\bg\rps_display.png").convert()
    screen.blit(display_bg, (0,0))

    draw_scores(player_score, computer_score, font, 800, screen)
    if player_score > computer_score:
        winner_text = "You Win!"
    elif player_score < computer_score:
        winner_text = "Computer Wins!"
    else:
        winner_text = "It's a Tie!"
    draw_text(winner_text, display_font, WHITE, 800 // 2, 350, screen)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rock Paper Scissors')
clock = pygame.time.Clock()

bg = pygame.image.load(r"D:\Codsoft\rps\bg\rps_bg.png").convert() 

player = Player(screen, is_player=True)
computer = Player(screen, is_player=False)

game_active = False
player_score = 0
computer_score = 0

round_result = ""
player_choice = ""
computer_choice = ""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CHOICES = ["Rock", "Paper", "Scissors"]

font = pygame.font.Font(None, 36)
f_font = pygame.font.Font(None, 32)
display_font = pygame.font.Font(r"D:\Codsoft\rps\font\SHUTTLE-X.ttf", 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if rock_button.collidepoint(mouse_pos):
                    player_choice = "Rock"
                    computer_choice = random.choice(CHOICES)
                    player.update_hand(player_choice)
                    computer.update_hand(computer_choice)
                    round_result, player_choice, computer_choice = calc_result(player_choice, computer_choice)
                    draw_text(f"Player chose: {player_choice} Computer chose: {computer_choice} {round_result}", font, BLACK, 100,70, screen)
                    if "You win" in round_result:
                        player_score += 1
                    elif "Computer wins" in round_result:
                        computer_score += 1
                    

                elif paper_button.collidepoint(mouse_pos):
                    player_choice = "Paper"
                    computer_choice = random.choice(CHOICES)
                    player.update_hand(player_choice)
                    computer.update_hand(computer_choice)
                    round_result, player_choice, computer_choice = calc_result(player_choice, computer_choice)
                    draw_text(f"Player chose: {player_choice} Computer chose: {computer_choice} {round_result}", font, BLACK, 100,70, screen)
                    if "You win" in round_result:
                        player_score += 1
                    elif "Computer wins" in round_result:
                        computer_score += 1
                    

                elif scissors_button.collidepoint(mouse_pos):
                    player_choice = "Scissors"
                    computer_choice = random.choice(CHOICES)
                    player.update_hand(player_choice)
                    computer.update_hand(computer_choice)
                    round_result, player_choice, computer_choice = calc_result(player_choice, computer_choice)
                    draw_text(f"Player chose: {player_choice} Computer chose: {computer_choice} {round_result}", font, BLACK, 100,70, screen)
                    pygame.display.update()
                    if "You win" in round_result:
                        player_score += 1
                    elif "Computer wins" in round_result:
                        computer_score += 1
                
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    game_active = True

        if event.type == pygame.USEREVENT:
            player.paused = False
            computer.paused = False
            
    if game_active:
        screen.blit(bg, (0,0))
        player.update()
        computer.update()
        screen.blit(player.hand_surf, player.hand_rect)
        screen.blit(computer.hand_surf, computer.hand_rect)

        draw_scores(player_score, computer_score, font, 800, screen) 

        draw_round_result_text(round_result, player_choice, computer_choice)

        rock_button = pygame.Rect(180, 470, 100, 100)
        rock_button_rect_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        rock_button_rect_surface.fill((0, 0, 0, 0))  # Fully transparent

        paper_button = pygame.Rect(350, 470, 100, 100)
        paper_button_rect_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        paper_button_rect_surface.fill((0, 0, 0, 0))  # Fully transparent

        scissors_button = pygame.Rect(525, 470, 100, 100)
        scissors_button_rect_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        scissors_button_rect_surface.fill((0, 0, 0, 0))  # Fully transparent

        if player_score == 3 or computer_score == 3:
            display_result(player_score, computer_score)
            pygame.display.update()
            pygame.time.delay(2000)
            # Reset scores and round count
            player_score = 0
            computer_score = 0
            round_count = 0
            game_active = False

    else:
        start_screen = pygame.image.load(r"D:\Codsoft\rps\bg\rps_start.png").convert()
        screen.blit(start_screen, (0,0))
        
        alpha_value = 0  # transparency level = 0 (fully transparent)
        play_button = pygame.Surface((250, 72), pygame.SRCALPHA)
        transparent_color = (255, 255, 255, alpha_value)  # White color with transparency
        pygame.draw.rect(play_button, transparent_color, play_button.get_rect())

        # Blit the transparent rectangle onto the screen
        screen.blit(play_button, (265, 358))
        start_button_rect = pygame.Rect(265, 358, 250, 72)

    pygame.display.update()
    clock.tick(60)
