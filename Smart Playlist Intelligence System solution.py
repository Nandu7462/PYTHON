n = int(input("Enter number of songs: "))

playlist = [0] * n

for i in range(n):
    playlist[i] = int(input("Enter song duration: "))


invalid = False

for i in range(n):
    if playlist[i] <= 0:
        invalid = True


if invalid == True:

    print("Invalid Playlist")
    print("Recommendation: Fix invalid durations")

else:

    total_duration = sum(playlist)

    print("Total Duration:", total_duration, "seconds")

    print("Songs:", len(playlist))


    

    repetitive = False

    for i in range(n):

        if playlist.count(playlist[i]) > 1:

            repetitive = True


   
    if total_duration < 300:

        print("Category: Too Short Playlist")

        print("Recommendation: Add more songs")


    elif total_duration > 3600:

        print("Category: Too Long Playlist")

        print("Recommendation: Reduce playlist length")


    elif repetitive == True:

        print("Category: Repetitive Playlist")

        print("Recommendation: Add variety")


    else:

        print("Category: Balanced Playlist")

        print("Recommendation: Good listening session")
