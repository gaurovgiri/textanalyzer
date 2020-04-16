####
####
####
####

user_input = str(input("Have you put your file in the same directory where the program is?(Y/N): "))

if user_input == 'y':

  def count_char(text, char):
    count = 0
    for c in text:
      if c == char:
        count += 1
    return count
  try:
    filename = input("Enter a filename(only name!!): ")
    with open(filename+".txt") as f:
      text = f.read()
      print(text)
      print(" ")
      print("The following are the analyzed data of the text: \n ")

    for char in "abcdefghijklmnopqrstuvwxyz":
      perc = 100 * count_char(text, char) / len(text)
      print("{0} - {1}%".format(char, round(perc, 2)))
  except FileNotFoundError:
    print("File not Found! Please check the name of the file and rerun the program with correct file name.")
else:
  print("Rerun the program again after putting your file in the same directory where you program locates.")
  a = input("Press any key to exit.")
  exit()