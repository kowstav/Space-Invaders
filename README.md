# Space Invaders Reloaded

**Python Game**

Developed a simple, yet engaging, Python game inspired by the classic Space Invaders arcade game. The objective is to control a spaceship, shoot at invading alien ships, and achieve the highest score possible.

## Features
- Player spaceship movement (left/right)
- Shooting lasers at enemies
- Multiple enemies with grid formation
- Score tracking and high score display
- Game over condition when enemies reach the bottom

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kowstav/SpaceInvadersReloaded.git
   cd SpaceInvadersReloaded
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running the Game

```bash
python src/main.py
```

## Controls

* **Left Arrow**: Move left
* **Right Arrow**: Move right
* **Space**: Shoot

## Dependencies

* Python 3.6+
* [pygame](https://www.pygame.org/)

## Assets

Place `player.png`, `enemy.png`, and `laser.png` in `src/assets/`.

## License

Apache 2.0