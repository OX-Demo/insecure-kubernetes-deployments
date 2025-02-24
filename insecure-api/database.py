from models import VideoGame, User

# Simulated database
video_games = [
    VideoGame(id=1, title="The Legend of Zelda: Breath of the Wild", developer="Nintendo EPD", publisher="Nintendo", year_published=2017, sales=25_000_000),
    VideoGame(id=2, title="Super Mario Odyssey", developer="Nintendo EPD", publisher="Nintendo", year_published=2017, sales=21_000_000),
    VideoGame(id=3, title="Red Dead Redemption 2", developer="Rockstar Studios", publisher="Rockstar Games", year_published=2018, sales=50_000_000),
    VideoGame(id=4, title="God of War", developer="Santa Monica Studio", publisher="Sony Interactive Entertainment", year_published=2018, sales=19_500_000),
    VideoGame(id=5, title="Marvel's Spider-Man", developer="Insomniac Games", publisher="Sony Interactive Entertainment", year_published=2018, sales=20_000_000),
    VideoGame(id=6, title="Grand Theft Auto V", developer="Rockstar North", publisher="Rockstar Games", year_published=2013, sales=150_000_000),
    VideoGame(id=7, title="Minecraft", developer="Mojang Studios", publisher="Xbox Game Studios", year_published=2011, sales=238_000_000),
    VideoGame(id=8, title="Fortnite", developer="Epic Games", publisher="Epic Games", year_published=2017, sales=0),  # Free-to-play
    VideoGame(id=9, title="Call of Duty: Modern Warfare", developer="Infinity Ward", publisher="Activision", year_published=2019, sales=30_000_000),
    VideoGame(id=10, title="Apex Legends", developer="Respawn Entertainment", publisher="Electronic Arts", year_published=2019, sales=0),  # Free-to-play
    VideoGame(id=11, title="Animal Crossing: New Horizons", developer="Nintendo EPD", publisher="Nintendo", year_published=2020, sales=33_890_000),
    VideoGame(id=12, title="Cyberpunk 2077", developer="CD Projekt Red", publisher="CD Projekt", year_published=2020, sales=13_700_000),
    VideoGame(id=13, title="Halo Infinite", developer="343 Industries", publisher="Xbox Game Studios", year_published=2021, sales=1_000_000),
    VideoGame(id=14, title="Doom Eternal", developer="id Software", publisher="Bethesda Softworks", year_published=2020, sales=3_000_000),
    VideoGame(id=15, title="The Last of Us Part II", developer="Naughty Dog", publisher="Sony Interactive Entertainment", year_published=2020, sales=10_000_000),
    VideoGame(id=16, title="FIFA 21", developer="EA Vancouver", publisher="Electronic Arts", year_published=2020, sales=20_000_000),
    VideoGame(id=17, title="NBA 2K21", developer="Visual Concepts", publisher="2K Sports", year_published=2020, sales=8_000_000),
    VideoGame(id=18, title="Assassin's Creed Valhalla", developer="Ubisoft Montreal", publisher="Ubisoft", year_published=2020, sales=12_000_000),
    VideoGame(id=19, title="Ghost of Tsushima", developer="Sucker Punch Productions", publisher="Sony Interactive Entertainment", year_published=2020, sales=6_500_000),
    VideoGame(id=20, title="Hades", developer="Supergiant Games", publisher="Supergiant Games", year_published=2020, sales=1_000_000),
    VideoGame(id=21, title="Resident Evil Village", developer="Capcom", publisher="Capcom", year_published=2021, sales=5_000_000),
    VideoGame(id=22, title="Monster Hunter: World", developer="Capcom", publisher="Capcom", year_published=2018, sales=17_000_000),
    VideoGame(id=23, title="Super Smash Bros. Ultimate", developer="Bandai Namco Studios/Sora Ltd.", publisher="Nintendo", year_published=2018, sales=25_710_000),
    VideoGame(id=24, title="Mario Kart 8 Deluxe", developer="Nintendo EPD", publisher="Nintendo", year_published=2017, sales=38_740_000),
    VideoGame(id=25, title="Pokémon Sword and Shield", developer="Game Freak", publisher="Nintendo", year_published=2019, sales=22_640_000),
    VideoGame(id=26, title="Fall Guys", developer="Mediatonic", publisher="Devolver Digital", year_published=2020, sales=11_000_000),
    VideoGame(id=27, title="Among Us", developer="InnerSloth", publisher="InnerSloth", year_published=2018, sales=3_000_000),
    VideoGame(id=28, title="Death Stranding", developer="Kojima Productions", publisher="Sony Interactive Entertainment", year_published=2019, sales=5_000_000),
    VideoGame(id=29, title="Sekiro: Shadows Die Twice", developer="FromSoftware", publisher="Activision", year_published=2019, sales=5_000_000),
    VideoGame(id=30, title="Control", developer="Remedy Entertainment", publisher="505 Games", year_published=2019, sales=2_000_000),
    VideoGame(id=31, title="Horizon Zero Dawn", developer="Guerrilla Games", publisher="Sony Interactive Entertainment", year_published=2017, sales=10_000_000),
    VideoGame(id=32, title="Cuphead", developer="Studio MDHR", publisher="Studio MDHR", year_published=2017, sales=6_000_000),
    VideoGame(id=33, title="The Witcher 3: Wild Hunt", developer="CD Projekt Red", publisher="CD Projekt", year_published=2015, sales=30_000_000),
    VideoGame(id=34, title="Overwatch", developer="Blizzard Entertainment", publisher="Blizzard Entertainment", year_published=2016, sales=50_000_000),
    VideoGame(id=35, title="Dark Souls III", developer="FromSoftware", publisher="Bandai Namco Entertainment", year_published=2016, sales=10_000_000),
    VideoGame(id=36, title="Bloodborne", developer="FromSoftware", publisher="Sony Interactive Entertainment", year_published=2015, sales=2_000_000),
    VideoGame(id=37, title="Rocket League", developer="Psyonix", publisher="Psyonix", year_published=2015, sales=10_500_000),
    VideoGame(id=38, title="Destiny 2", developer="Bungie", publisher="Bungie", year_published=2017, sales=1_000_000),
    VideoGame(id=39, title="Battlefield V", developer="EA DICE", publisher="Electronic Arts", year_published=2018, sales=7_300_000),
    VideoGame(id=40, title="Far Cry 5", developer="Ubisoft Montreal", publisher="Ubisoft", year_published=2018, sales=5_000_000),
    VideoGame(id=41, title="The Elder Scrolls V: Skyrim", developer="Bethesda Game Studios", publisher="Bethesda Softworks", year_published=2011, sales=30_000_000),
    VideoGame(id=42, title="Metal Gear Solid V: The Phantom Pain", developer="Kojima Productions", publisher="Konami", year_published=2015, sales=6_000_000),
    VideoGame(id=43, title="No Man's Sky", developer="Hello Games", publisher="Hello Games", year_published=2016, sales=2_000_000),
    VideoGame(id=44, title="Stardew Valley", developer="ConcernedApe", publisher="ConcernedApe", year_published=2016, sales=15_000_000),
    VideoGame(id=45, title="Persona 5", developer="Atlus", publisher="Atlus", year_published=2016, sales=3_200_000),
    VideoGame(id=46, title="Resident Evil 2", developer="Capcom", publisher="Capcom", year_published=2019, sales=10_000_000),
    VideoGame(id=47, title="Resident Evil 3", developer="Capcom", publisher="Capcom", year_published=2020, sales=4_000_000),
    VideoGame(id=48, title="Borderlands 3", developer="Gearbox Software", publisher="2K Games", year_published=2019, sales=14_000_000),
    VideoGame(id=49, title="Final Fantasy VII Remake", developer="Square Enix Business Division 1", publisher="Square Enix", year_published=2020, sales=5_000_000),
    VideoGame(id=50, title="The Outer Worlds", developer="Obsidian Entertainment", publisher="Private Division", year_published=2019, sales=3_000_000),
    VideoGame(id=51, title="Ori and the Will of the Wisps", developer="Moon Studios", publisher="Xbox Game Studios", year_published=2020, sales=2_000_000),
    VideoGame(id=52, title="Genshin Impact", developer="miHoYo", publisher="miHoYo", year_published=2020, sales=0),  # Free-to-play
    VideoGame(id=53, title="Valorant", developer="Riot Games", publisher="Riot Games", year_published=2020, sales=0),  # Free-to-play
    VideoGame(id=54, title="Call of Duty: Warzone", developer="Infinity Ward/Raven Software", publisher="Activision", year_published=2020, sales=0),  # Free-to-play
    VideoGame(id=55, title="PUBG: Battlegrounds", developer="PUBG Studios", publisher="Krafton", year_published=2017, sales=70_000_000),
    VideoGame(id=56, title="Nier: Automata", developer="PlatinumGames", publisher="Square Enix", year_published=2017, sales=6_000_000),
    VideoGame(id=57, title="Dead Cells", developer="Motion Twin", publisher="Motion Twin", year_published=2018, sales=5_000_000),
    VideoGame(id=58, title="Hollow Knight", developer="Team Cherry", publisher="Team Cherry", year_published=2017, sales=3_000_000),
    VideoGame(id=59, title="Celeste", developer="Maddy Makes Games", publisher="Matt Makes Games", year_published=2018, sales=1_000_000),
    VideoGame(id=60, title="Dishonored 2", developer="Arkane Studios", publisher="Bethesda Softworks", year_published=2016, sales=2_500_000),
    VideoGame(id=61, title="Fire Emblem: Three Houses", developer="Intelligent Systems/Koei Tecmo", publisher="Nintendo", year_published=2019, sales=3_000_000),
    VideoGame(id=62, title="Crash Bandicoot N. Sane Trilogy", developer="Vicarious Visions", publisher="Activision", year_published=2017, sales=10_000_000),
    VideoGame(id=63, title="Spyro Reignited Trilogy", developer="Toys for Bob", publisher="Activision", year_published=2018, sales=2_000_000),
    VideoGame(id=64, title="Subnautica", developer="1_000_000 Worlds Entertainment", publisher="1_000_000 Worlds Entertainment", year_published=2018, sales=5_000_000),
    VideoGame(id=65, title="Terraria", developer="Re-Logic", publisher="Re-Logic", year_published=2011, sales=35_000_000),
    VideoGame(id=66, title="League of Legends", developer="Riot Games", publisher="Riot Games", year_published=2009, sales=0),  # Free-to-play
    VideoGame(id=67, title="World of Warcraft", developer="Blizzard Entertainment", publisher="Blizzard Entertainment", year_published=2004, sales=14_000_000),
    VideoGame(id=68, title="Dota 2", developer="Valve", publisher="Valve", year_published=2013, sales=0),  # Free-to-play
    VideoGame(id=69, title="Team Fortress 2", developer="Valve", publisher="Valve", year_published=2007, sales=0),  # Free-to-play
    VideoGame(id=70, title="Portal 2", developer="Valve", publisher="Valve", year_published=2011, sales=4_000_000),
    VideoGame(id=71, title="Half-Life: Alyx", developer="Valve", publisher="Valve", year_published=2020, sales=2_000_000),
    VideoGame(id=72, title="Among Us", developer="InnerSloth", publisher="InnerSloth", year_published=2018, sales=3_000_000),
    VideoGame(id=73, title="Warframe", developer="Digital Extremes", publisher="Digital Extremes", year_published=2013, sales=0),  # Free-to-play
    VideoGame(id=74, title="Path of Exile", developer="Grinding Gear Games", publisher="Grinding Gear Games", year_published=2013, sales=0),  # Free-to-play
    VideoGame(id=75, title="Final Fantasy XIV", developer="Square Enix", publisher="Square Enix", year_published=2013, sales=24_000_000),
    VideoGame(id=76, title="Tetris Effect", developer="Monstars Inc./Resonair", publisher="Enhance Games", year_published=2018, sales=1_000_000),
    VideoGame(id=77, title="Deathloop", developer="Arkane Studios", publisher="Bethesda Softworks", year_published=2021, sales=1_000_000),
    VideoGame(id=78, title="Forza Horizon 4", developer="Playground Games", publisher="Xbox Game Studios", year_published=2018, sales=10_000_000),
    VideoGame(id=79, title="Gran Turismo Sport", developer="Polyphony Digital", publisher="Sony Interactive Entertainment", year_published=2017, sales=8_000_000),
    VideoGame(id=80, title="Need for Speed Heat", developer="Ghost Games", publisher="Electronic Arts", year_published=2019, sales=3_000_000),
    VideoGame(id=81, title="Control", developer="Remedy Entertainment", publisher="505 Games", year_published=2019, sales=2_000_000),
    VideoGame(id=82, title="It Takes Two", developer="Hazelight Studios", publisher="Electronic Arts", year_published=2021, sales=3_000_000),
    VideoGame(id=83, title="Ratchet & Clank: Rift Apart", developer="Insomniac Games", publisher="Sony Interactive Entertainment", year_published=2021, sales=1_100_000),
    VideoGame(id=84, title="Kena: Bridge of Spirits", developer="Ember Lab", publisher="Ember Lab", year_published=2021, sales=1_000_000),
    VideoGame(id=85, title="Psychonauts 2", developer="Double Fine", publisher="Xbox Game Studios", year_published=2021, sales=1_000_000),
    VideoGame(id=86, title="Returnal", developer="Housemarque", publisher="Sony Interactive Entertainment", year_published=2021, sales=560_000),
    VideoGame(id=87, title="Mario Party Superstars", developer="NDcube", publisher="Nintendo", year_published=2021, sales=5_430_000),
    VideoGame(id=88, title="Metroid Dread", developer="MercurySteam/Nintendo EPD", publisher="Nintendo", year_published=2021, sales=2_900_000),
    VideoGame(id=89, title="Back 4 Blood", developer="Turtle Rock Studios", publisher="Warner Bros. Interactive Entertainment", year_published=2021, sales=1_000_000),
    VideoGame(id=90, title="Ghostrunner", developer="One More Level", publisher="505 Games", year_published=2020, sales=600_000),
    VideoGame(id=91, title="Sifu", developer="Sloclap", publisher="Sloclap", year_published=2022, sales=500_000),
    VideoGame(id=92, title="Elden Ring", developer="FromSoftware", publisher="Bandai Namco Entertainment", year_published=2022, sales=13_400_000),
    VideoGame(id=93, title="Tiny Tina's Wonderlands", developer="Gearbox Software", publisher="2K Games", year_published=2022, sales=1_000_000),
    VideoGame(id=94, title="Horizon Forbidden West", developer="Guerrilla Games", publisher="Sony Interactive Entertainment", year_published=2022, sales=8_400_000),
    VideoGame(id=95, title="Gran Turismo 7", developer="Polyphony Digital", publisher="Sony Interactive Entertainment", year_published=2022, sales=1_000_000),
    VideoGame(id=96, title="Kirby and the Forgotten Land", developer="HAL Laboratory", publisher="Nintendo", year_published=2022, sales=4_530_000),
    VideoGame(id=97, title="LEGO Star Wars: The Skywalker Saga", developer="Traveller's Tales", publisher="Warner Bros. Interactive Entertainment", year_published=2022, sales=3_200_000),
    VideoGame(id=98, title="Stray", developer="BlueTwelve Studio", publisher="Annapurna Interactive", year_published=2022, sales=1_000_000),
    VideoGame(id=99, title="God of War Ragnarök", developer="Santa Monica Studio", publisher="Sony Interactive Entertainment", year_published=2022, sales=11_000_000),
    VideoGame(id=100, title="Call of Duty: Vanguard", developer="Sledgehammer Games", publisher="Activision", year_published=2021, sales=5_700_000),
    VideoGame(id=101, title="Halo Infinite", developer="343 Industries", publisher="Xbox Game Studios", year_published=2021, sales=1_000_000),
    VideoGame(id=102, title="Resident Evil 4 Remake", developer="Capcom", publisher="Capcom", year_published=2023, sales=4_000_000),
    VideoGame(id=103, title="Dead Space Remake", developer="Motive Studio", publisher="Electronic Arts", year_published=2023, sales=1_000_000),
    VideoGame(id=104, title="Forspoken", developer="Luminous Productions", publisher="Square Enix", year_published=2023, sales=1_000_000),
    VideoGame(id=105, title="Hogwarts Legacy", developer="Avalanche Software", publisher="Warner Bros. Interactive Entertainment", year_published=2023, sales=12_000_000),
    VideoGame(id=106, title="The Legend of Zelda: Tears of the Kingdom", developer="Nintendo EPD", publisher="Nintendo", year_published=2023, sales=10_000_000),
    VideoGame(id=107, title="Starfield", developer="Bethesda Game Studios", publisher="Bethesda Softworks", year_published=2023, sales=1_000_000),
    VideoGame(id=108, title="Diablo IV", developer="Blizzard Entertainment", publisher="Blizzard Entertainment", year_published=2023, sales=10_000_000),
    VideoGame(id=109, title="Final Fantasy XVI", developer="Square Enix Creative Business Unit III", publisher="Square Enix", year_published=2023, sales=3_000_000),
    VideoGame(id=110, title="Baldur's Gate III", developer="Larian Studios", publisher="Larian Studios", year_published=2023, sales=5_200_000),
    VideoGame(id=111, title="Armored Core VI: Fires of Rubicon", developer="FromSoftware", publisher="Bandai Namco Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=112, title="Marvel's Spider-Man 2", developer="Insomniac Games", publisher="Sony Interactive Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=113, title="Assassin's Creed Mirage", developer="Ubisoft Bordeaux", publisher="Ubisoft", year_published=2023, sales=1_000_000),
    VideoGame(id=114, title="Forza Motorsport", developer="Turn 10 Studios", publisher="Xbox Game Studios", year_published=2023, sales=1_000_000),
    VideoGame(id=115, title="Alan Wake II", developer="Remedy Entertainment", publisher="Epic Games Publishing", year_published=2023, sales=1_000_000),
    VideoGame(id=116, title="Sonic Frontiers", developer="Sonic Team", publisher="Sega", year_published=2022, sales=3_200_000),
    VideoGame(id=117, title="The Callisto Protocol", developer="Striking Distance Studios", publisher="Krafton", year_published=2022, sales=2_000_000),
    VideoGame(id=118, title="Mario + Rabbids Sparks of Hope", developer="Ubisoft Milan/Ubisoft Paris", publisher="Ubisoft", year_published=2022, sales=1_000_000),
    VideoGame(id=119, title="Splatoon 3", developer="Nintendo EPD", publisher="Nintendo", year_published=2022, sales=10_130_000),
    VideoGame(id=120, title="Bayonetta 3", developer="PlatinumGames", publisher="Nintendo", year_published=2022, sales=1_000_000),
    VideoGame(id=121, title="Dying Light 2 Stay Human", developer="Techland", publisher="Techland", year_published=2022, sales=5_000_000),
    VideoGame(id=122, title="Saints Row", developer="Volition", publisher="Deep Silver", year_published=2022, sales=1_000_000),
    VideoGame(id=123, title="Pokemon Legends: Arceus", developer="Game Freak", publisher="Nintendo", year_published=2022, sales=14_630_000),
    VideoGame(id=124, title="Pokemon Scarlet and Violet", developer="Game Freak", publisher="Nintendo", year_published=2022, sales=20_610_000),
    VideoGame(id=125, title="Triangle Strategy", developer="Artdink", publisher="Square Enix", year_published=2022, sales=1_000_000),
    VideoGame(id=126, title="Xenoblade Chronicles 3", developer="Monolith Soft", publisher="Nintendo", year_published=2022, sales=1_810_000),
    VideoGame(id=127, title="Mario Strikers: Battle League", developer="Next Level Games", publisher="Nintendo", year_published=2022, sales=2_170_000),
    VideoGame(id=128, title="Fire Emblem Engage", developer="Intelligent Systems", publisher="Nintendo", year_published=2023, sales=1_610_000),
    VideoGame(id=129, title="Octopath Traveler II", developer="Square Enix/Acquire", publisher="Square Enix", year_published=2023, sales=1_000_000),
    VideoGame(id=130, title="Dead Island 2", developer="Dambuster Studios", publisher="Deep Silver", year_published=2023, sales=2_000_000),
    VideoGame(id=131, title="Minecraft Dungeons", developer="Mojang Studios/Double Eleven", publisher="Xbox Game Studios", year_published=2020, sales=11_500_000),
    VideoGame(id=132, title="Remnant II", developer="Gunfire Games", publisher="Gearbox Publishing", year_published=2023, sales=1_000_000),
    VideoGame(id=133, title="Street Fighter 6", developer="Capcom", publisher="Capcom", year_published=2023, sales=2_000_000),
    VideoGame(id=134, title="Pikmin 4", developer="Nintendo EPD", publisher="Nintendo", year_published=2023, sales=1_000_000),
    VideoGame(id=135, title="Armored Core VI", developer="FromSoftware", publisher="Bandai Namco Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=136, title="Mortal Kombat 1", developer="NetherRealm Studios", publisher="Warner Bros. Interactive Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=137, title="S.T.A.L.K.E.R. 2: Heart of Chornobyl", developer="GSC Game World", publisher="GSC Game World", year_published=2023, sales=1_000_000),
    VideoGame(id=138, title="Payday 3", developer="Overkill Software", publisher="Starbreeze Studios", year_published=2023, sales=1_000_000),
    VideoGame(id=139, title="Suicide Squad: Kill the Justice League", developer="Rocksteady Studios", publisher="Warner Bros. Interactive Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=140, title="Atomic Heart", developer="Mundfish", publisher="Focus Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=141, title="The Lord of the Rings: Gollum", developer="Daedalic Entertainment", publisher="Daedalic Entertainment", year_published=2023, sales=1_000_000),
    VideoGame(id=142, title="Diablo II: Resurrected", developer="Vicarious Visions", publisher="Blizzard Entertainment", year_published=2021, sales=5_000_000),
    VideoGame(id=143, title="Death's Door", developer="Acid Nerve", publisher="Devolver Digital", year_published=2021, sales=1_000_000),
    VideoGame(id=144, title="Disco Elysium", developer="ZA/UM", publisher="ZA/UM", year_published=2019, sales=2_000_000),
    VideoGame(id=145, title="Outer Wilds", developer="Mobius Digital", publisher="Annapurna Interactive", year_published=2019, sales=1_000_000),
    VideoGame(id=146, title="Hellblade: Senua's Sacrifice", developer="Ninja Theory", publisher="Ninja Theory", year_published=2017, sales=1_000_000),
    VideoGame(id=147, title="Sea of Thieves", developer="Rare", publisher="Xbox Game Studios", year_published=2018, sales=5_000_000),
    VideoGame(id=148, title="Ghostwire: Tokyo", developer="Tango Gameworks", publisher="Bethesda Softworks", year_published=2022, sales=1_000_000),
    VideoGame(id=149, title="Evil West", developer="Flying Wild Hog", publisher="Focus Entertainment", year_published=2022, sales=1_000_000),
    VideoGame(id=150, title="Return to Monkey Island", developer="Terrible Toybox", publisher="Devolver Digital", year_published=2022, sales=1_000_000),
]

users = [
    User(username="user1", token="user1token", is_admin=False, email="user1@example.com"),
    User(username="admin", token="admintoken", is_admin=True, email="admin@example.com"),
]

