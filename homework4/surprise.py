# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names(targets):
	for star in targets:
		print(star)

def print_star_spectral_types(targets):
	for star, info in targets.items():
		print(f"{star}: {info['Spectral Type']}")

def refine_by_mag(targets):
	for star, info in targets.items():
		if info["Magnitude"] > 0.1:
			print(f"{star}: {info["Magnitude"]}")

targets.setdefault("Albireo", {
	"RA": "19h 30m 43.3s",
	"Dec": "+27° 57′ 34.62″",
	"Magnitude": 3.09,
	"Spectral Type": "K2II"})

def find_brightest_near_dec(targets, target_dec=20):
    def parse_dec(dec_str):
        dec_str = dec_str.replace("−", "-").replace("+", "")
        parts = dec_str.replace("°", "").replace("′", "").replace("″", "").split()
        degrees, minutes, seconds = float(parts[0]), float(parts[1]), float(parts[2])
        if degrees < 0:
            return degrees - minutes / 60 - seconds / 3600
        return degrees + minutes / 60 + seconds / 3600

    closest_star = min(targets, key=lambda star: abs(parse_dec(targets[star]["Dec"]) - target_dec))
    print(f"Brightest star closest to {target_dec}°: {closest_star} "
          f"(Dec: {targets[closest_star]['Dec']}, Magnitude: {targets[closest_star]['Magnitude']})")

# My favorite constellation is Cygnus, the swan.

