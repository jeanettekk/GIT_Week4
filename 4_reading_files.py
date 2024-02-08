# open function opens files
# When we open a file, we should say why
# r stands for 'I want to read it'
# When you're done, close the file hand down! So it can be used by other programs
lyrics = open('sample_files/ShakeItOff.txt', 'r')

buffer = lyrics.read(10)
print(buffer)

# file handle has a read method
buffer = lyrics.read(20)
print(buffer)

lyric_line = lyrics.readline()
print(lyric_line)

next_line = lyrics.readline()
print(next_line)

# read the next 5 lines
for line in range(5):
    next_line = lyrics.readline()
    # print statement adds an additional \n even though lyrics already has one
    # These are two ways to remove the extra \n
    print(line, next_line, end='')
    print(line, next_line[:-1])

# # To use this slurping technique, you need to know how big your file is!
# # It reads the ENTIRE file
# print("#" * 25, "SLURPING 1 ", "#" * 25)
# # slurping 1
# # lines = open('brian.txt').read()
# song = open('sample_files/ShakeItOff.txt', 'r').read()
# print(f"Whole song:\n{song}")

# # slurping 2
# # llines= open('brian.txt').read().splitlines()
# print("#" * 25, "SLURPING 2 ", "#" * 25)
# song_as_list = open('sample_files/ShakeItOff.txt', 'r').read().splitlines()
# print(f"Whole song:\n{song_as_list}")

# # slurping 3
# print("#" * 25, "SLURPING 3 ", "#" * 25)
# # linelist = open('brian.txt').readlines()
# # includes \n end of line markers
# song_as_list = open('sample_files/ShakeItOff.txt', 'r').readlines()
# print(f"Whole song:\n{song_as_list}")


# best approach
print("#" * 25, "BEST APPROACH ", "#" * 25)
# uses the file object iterator

for line in open('sample_files/ShakeItOff.txt', 'r'):
    print(line[:-1])
