import tkinter as tk
import math

WIDTH = 800
HEIGHT = 600
UPDATE_DELAY = 50
PLAYER_SPEED_FACTOR = 0.5

class Planet:
    def __init__(self, x, y, gravitation):
        self.x = x
        self.y = y
        self.gravitation = gravitation

class Player:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

class PhysicsSimulation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.planets = []
        self.player = None

        main_frame = tk.Frame(root,  bg=  "black")
        main_frame.pack()

        planet_frame = tk.Frame(main_frame, bg='white')
        planet_frame.pack(fill='x', padx='5', pady='5')

        planet_label = tk.Label(planet_frame, text="Planet", bg='white')
        planet_label.pack(side='top', fill='x', padx='5', pady='5')

        frame_p_Pos=tk.Frame(planet_frame, bg="black")
        frame_p_Pos.pack(side='left', padx='5', pady='5')

        label_p_pos=tk.Label(frame_p_Pos, text='planet position', bg='white')
        label_p_pos.pack(side='top', fill='x', padx='5', pady='5')

        self.planet_x_entry = tk.Entry(frame_p_Pos)
        self.planet_x_entry.pack(side='top', padx='5', pady='5')

        self.planet_y_entry = tk.Entry(frame_p_Pos)
        self.planet_y_entry.pack(side='top', padx='5', pady='5')

        frame_grav=tk.Frame(planet_frame, bg="black")
        frame_grav.pack(side='left', padx='5', pady='5')

        planet_grav_label = tk.Label(frame_grav, text="Gravitation:", bg='white')
        planet_grav_label.pack(side='top', fill='x', padx='5', pady='5')
        self.planet_grav_entry = tk.Entry(frame_grav)
        self.planet_grav_entry.pack(side='top', padx='5', pady='5')

        create_planet_button = tk.Button(planet_frame, text="Create Planet", command=self.create_planet, bg='black', fg='white')
        create_planet_button.pack(side='left', padx='5', pady='5')

        player_frame = tk.Frame(main_frame, bg='white')
        player_frame.pack(side='left',fill='x', padx='5', pady='5')

        player_label = tk.Label(player_frame, text="Player", bg='white')
        player_label.pack(side='top', fill='x', padx='5', pady='5')

        frame_s_Pos = tk.Frame(player_frame, bg="black")
        frame_s_Pos.pack(side='left', padx='5', pady='5')

        Label_s_pos=tk.Label(frame_s_Pos, text='player position', bg='white')
        Label_s_pos.pack(side='top', fill='x', padx='5', pady='5')

        self.player_x_entry = tk.Entry(frame_s_Pos)
        self.player_x_entry.pack(side='top', padx='5', pady='5')

        self.player_y_entry = tk.Entry(frame_s_Pos)
        self.player_y_entry.pack(side='top', padx='5', pady='5')

        frame_v=tk.Frame(player_frame, bg="black")
        frame_v.pack(side='left', padx='5', pady='5')

        Label_v=tk.Label(frame_v, text='velocity', bg='white')
        Label_v.pack(side='top', fill='x', padx='5', pady='5')

        self.player_vx_entry = tk.Entry(frame_v)
        self.player_vx_entry.pack(side='top', padx='5', pady='5')

        self.player_vy_entry = tk.Entry(frame_v)
        self.player_vy_entry.pack(side='top', padx='5', pady='5')

        create_player_button = tk.Button(player_frame, text="Create Player", command=self.create_player, bg='black', fg='white')
        create_player_button.pack(side='left', padx='5', pady='5')

        play_button = tk.Button(main_frame, text="Play", command=self.run_simulation, bg='white')
        play_button.pack(side='right', padx='5',fill='x' , pady='5')

    def create_planet(self):
        x_entry = self.planet_x_entry.get()
        y_entry = self.planet_y_entry.get()
        grav_entry = self.planet_grav_entry.get()

        if x_entry and y_entry and grav_entry:
            try:

                x = float(x_entry)
                y = float(y_entry)
                gravitation = float(grav_entry)
                planet = Planet(x, y, gravitation)

                self.planets.append(planet)
            except ValueError:
                print("Invalid planet parameters")
        else:
            print("Please enter all planet parameters")

    def create_player(self):

        x_entry = self.player_x_entry.get()
        y_entry = self.player_y_entry.get()
        vx_entry = self.player_vx_entry.get()
        vy_entry = self.player_vy_entry.get()


        x = float(x_entry)
        y = float(y_entry)
        if x_entry and y_entry and vx_entry and vy_entry:
            try:
                x = float(x_entry)
                y = float(y_entry)
                velocity_x = float(vx_entry)
                velocity_y = float(vy_entry)

                self.player = Player(x, y, velocity_x, velocity_y)
            except ValueError:
                print("Invalid player parameters")
        else:
            print("Please enter all player parameters")

    def update_player_position(self):

        for planet in self.planets:

            dx = planet.x - self.player.x
            dy = planet.y - self.player.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance == 0:
                continue
            force = planet.gravitation / distance ** 2
            acceleration_x = force * dx / distance
            acceleration_y = force * dy / distance

            self.player.velocity_x += acceleration_x * PLAYER_SPEED_FACTOR
            self.player.velocity_y += acceleration_y * PLAYER_SPEED_FACTOR
            self.player.x += self.player.velocity_x
            self.player.y += self.player.velocity_y

    def draw_objects(self):
        self.canvas.delete(tk.ALL)

        self.canvas.create_rectangle(
            2, 2, WIDTH - 2, HEIGHT - 2,
            outline="white", width=2
        )

        for planet in self.planets:
            self.canvas.create_oval(
                planet.x - 20, planet.y - 20,
                planet.x + 20, planet.y + 20,
                fill="white"
            )

        self.canvas.create_oval(
            self.player.x - 10, self.player.y - 10,
            self.player.x + 10, self.player.y + 10,
            fill="red"
        )

    def run_simulation(self):
        while True:
            self.update_player_position()
            self.draw_objects()
            self.root.update()
            self.root.after(UPDATE_DELAY)

root = tk.Tk()
root.title("Planet Traveller v1.0")

simulation = PhysicsSimulation(root)

root.mainloop()
