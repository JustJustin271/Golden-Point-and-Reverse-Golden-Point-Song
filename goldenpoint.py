golden_ratio = 0.61803398875

print("==== Song Duration Input ===")
minutes_song = int(input("How long is your song in minutes? "))
seconds_song = int(input("How long is your song in seconds? "))
print("\n\n=== Calculations ===")
total_duration = (minutes_song * 60) + seconds_song

golden_point = int(golden_ratio * total_duration)
reverse_golden_point = int((1-golden_ratio) * total_duration)

print(f"""The golden point of the song is:\n
{golden_point // 60} minute(s) and {golden_point % 60} second(s)""")

print(f"""The reverse golden point of the song is:\n
{reverse_golden_point // 60} minute(s) and {reverse_golden_point % 60} second(s)""")

## Created on May 6th, 2026
## Used to find the golden and reverse golden points of a song
