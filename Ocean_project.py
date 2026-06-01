import tkinter as tk 

root = tk.Tk() 
root.title("Ocean explorer - Made by Mai Gia Linh") 
root.geometry("1600x900") 

canvas = tk.Canvas(root, bg="white", highlightthickness=0) 
content_frame = tk.Frame(canvas, bg="DodgerBlue4") 

canvas.create_window((0, 0), window=content_frame, anchor="nw") 
canvas.pack(fill="both", expand=True) 

sky = tk.Frame(content_frame, bg="lightblue") 
sky.pack(fill="x") 

tk.Label( 
    sky, 
    text="OCEAN EXPLORER - MADE BY MAI GIA LINH", 
    bg="lightblue", 
    fg="white", 
    font=("Courier", 50), 
).pack(pady=200, padx=150, anchor="w") 

original_whale_image = tk.PhotoImage(file="humpback_whale.png") 
scaled_whale_image = original_whale_image.subsample(2, 2) 

original_whale1_image = tk.PhotoImage(file="blue_whale.png") 
scaled_whale1_image = original_whale1_image.subsample(2, 2) 

original_bottlenose_image = tk.PhotoImage(file="bottlenose_dolphin.png")
scaled_bottlenose_image = original_bottlenose_image.subsample(3, 3)

original_flying_fish_image = tk.PhotoImage(file="flying_fish.png")
scaled_flying_fish_image = original_flying_fish_image.subsample(4, 4)

original_orca_image = tk.PhotoImage(file="orca.png")
scaled_orca_image = original_orca_image.subsample(3, 3)

original_mola_image = tk.PhotoImage(file="mola.png")
scaled_mola_image = original_mola_image.subsample(3, 3)

original_coelacanth_image = tk.PhotoImage(file="coelacanth.png")
scaled_coelacanth_image = original_coelacanth_image.subsample(4, 4)

original_lantern_fish_image = tk.PhotoImage(file="lantern_fish.png")
scaled_lantern_fish_image = original_lantern_fish_image.subsample(4, 4)

original_great_white_shark_image = tk.PhotoImage(file="great_white.png")
scaled_great_white_shark_image = original_great_white_shark_image.subsample(3, 3)

original_whale_shark_image = tk.PhotoImage(file="whale_shark.png")
scaled_whale_shark_image = original_whale_shark_image.subsample(3, 3)

for i in range(1, 11): 
    current_depth = i * 100 
    
    if current_depth == 100: 
        zone_100m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_100m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_100m, 
            text="100m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        flying_fish_label = tk.Label(zone_100m, image=scaled_flying_fish_image, bg="DodgerBlue4")
        flying_fish_label.pack(side="left", padx=20)

        flying_fish_desc = "Flying Fish can make powerful, self-propelled leaps out of the water into the air."
        tk.Label(
            zone_100m,
            text=flying_fish_desc,
            bg="DodgerBlue4",
            fg="white",
            font=("Courier", 15),
            justify="left",
            wraplength=250
        ).pack(side="left", padx=10)

    elif current_depth == 200: 
        zone_200m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_200m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_200m, 
            text="200m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        bottlenose_label = tk.Label(zone_200m, image=scaled_bottlenose_image, bg="DodgerBlue4") 
        bottlenose_label.pack(side="left", padx=20) 

        bottlenose_desc = "Bottlenose Dolphin, they are known for their intelligence and playful behavior." 
        tk.Label( 
            zone_200m, 
            text=bottlenose_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="left", 
            wraplength=250 
        ).pack(side="left", padx=10)

    elif current_depth == 300: 
        zone_300m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_300m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_300m, 
            text="300m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        orca_label = tk.Label(zone_300m, image=scaled_orca_image, bg="DodgerBlue4") 
        orca_label.pack(side="right", padx=20) 

        orca_desc = "Orca, these intelligent marine mammals are known for their complex social structures and hunting strategies." 
        tk.Label( 
            zone_300m, 
            text=orca_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)

    elif current_depth == 400: 
        zone_400m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_400m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_400m, 
            text="400m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        whale_label = tk.Label(zone_400m, image=scaled_whale_image, bg="DodgerBlue4") 
        whale_label.pack(side="right", padx=20) 

        humpback_desc = "Humpback whales, these magnificent creatures are known for their songs which they sing to attract mates." 
        tk.Label( 
            zone_400m, 
            text=humpback_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)

    elif current_depth == 500: 
        zone_500m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_500m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_500m, 
            text="500m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        whale1_label = tk.Label(zone_500m, image=scaled_whale1_image, bg="DodgerBlue4") 
        whale1_label.pack(side="left", padx=20) 

        blue_whale_desc = "Blue Whale, they feed almost exclusively on tiny shrimp-like creatures called krill." 
        tk.Label( 
            zone_500m, 
            text=blue_whale_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="left", 
            wraplength=250 
        ).pack(side="left", padx=10) 
        
    elif current_depth == 600: 
        zone_600m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_600m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_600m, 
            text="600m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        mola_label = tk.Label(zone_600m, image=scaled_mola_image, bg="DodgerBlue4") 
        mola_label.pack(side="right", padx=20) 

        mola_desc = "Mola Mola, these large and unique marine animals are known for their distinctive flat, oval shape." 
        tk.Label( 
            zone_600m, 
            text=mola_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)
    
    elif current_depth == 700: 
        zone_700m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_700m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_700m, 
            text="700m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        coelacanth_label = tk.Label(zone_700m, image=scaled_coelacanth_image, bg="DodgerBlue4") 
        coelacanth_label.pack(side="left", padx=20) 

        coelacanth_desc = "Coelacanth, these ancient fish are often called 'living fossils' due to their primitive characteristics." 
        tk.Label( 
            zone_700m, 
            text=coelacanth_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="left", 
            wraplength=250 
        ).pack(side="left", padx=10) 

    elif current_depth == 800: 
        zone_800m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_800m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_800m, 
            text="800m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        lantern_fish_label = tk.Label(zone_800m, image=scaled_lantern_fish_image, bg="DodgerBlue4") 
        lantern_fish_label.pack(side="right", padx=20) 

        lantern_fish_desc = "Lantern Fish, these bioluminescent fish are known for their ability to produce light." 
        tk.Label( 
            zone_800m, 
            text=lantern_fish_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)
    
    elif current_depth == 900: 
        zone_900m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_900m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_900m, 
            text="900m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        great_white_shark_label = tk.Label(zone_900m, image=scaled_great_white_shark_image, bg="DodgerBlue4") 
        great_white_shark_label.pack(side="right", padx=20) 

        great_white_shark_desc = "Great White Shark, these apex predators are known for their size and power." 
        tk.Label( 
            zone_900m, 
            text=great_white_shark_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)

    else: 
        zone_1000m = tk.Frame(content_frame, bg="DodgerBlue4") 
        zone_1000m.pack(fill="x", padx=50, pady=250) 
        
        tk.Label( 
            zone_1000m, 
            text="1000m", 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 25), 
        ).pack(side="left") 

        whale_shark_label = tk.Label(zone_1000m, image=scaled_whale_shark_image, bg="DodgerBlue4") 
        whale_shark_label.pack(side="right", padx=20) 

        whale_shark_desc = "Whale Shark, these gentle giants are the largest fish in the ocean." 
        tk.Label( 
            zone_1000m, 
            text=whale_shark_desc, 
            bg="DodgerBlue4", 
            fg="white", 
            font=("Courier", 15), 
            justify="right", 
            wraplength=250 
        ).pack(side="right", padx=10)

content_frame.bind( 
    "<Configure>", 
    lambda event: canvas.configure(scrollregion=canvas.bbox("all")), 
) 
canvas.bind_all( 
    "<MouseWheel>", lambda event: canvas.yview_scroll(-1 * event.delta, "units") 
) 

root.mainloop()