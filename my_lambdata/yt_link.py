"""
This function takes a YouTube Link, an hour mark, minute mark
and second mark and creates a modified link that will start 
the video at the precise time desired.  

It is very useful for creating lecture notes.
"""


def ytlink():
    # Get user inputs:
    print()
    print("This function will modify a YouTube link to start at a")
    print("specific timepoint within the video.  It is useful for")
    print("making lecture notes.")
    print()
    l = input("Please paste YouTube link here: ")
    h = int(input("Please enter hour(s): "))
    m = int(input("Please enter minute(s): "))
    s = int(input("Please enter second(s): "))
    print()
    print("A link to start the YouTube video precisely at: ", h,
          'hours ', m, "minutes ", s, "seconds will be created.")
    print()

    # Check link for "&"
    if "&" in l:
        l = l.split("&")
        l = l[0]

    t = (h*60*60) + (m*60) + s
    # create link components
    first = "https://youtu.be/"
    second = l.split("=")
    second = second[1]
    third = "?t=" + str(t)
    l = first + second + third
    print(l)
    return


if __name__ == '__main__':
    ytlink()
