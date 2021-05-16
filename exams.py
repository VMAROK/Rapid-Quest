#!/usr/bin/env python3
import os



exams = ["CompTIA A+", "CompTIA Linux+", "Cisco Certified Network Associate (CCNA)", "Certified Ethical Hacker (CEH)"]
choice = 0

while choice < 5:
   print("\n\n\n\n\n")
   for x in exams:
      print(str((exams.index(x) + 1)) + ". " + x)
   print("\n\n\n\n\n")

   choice = int(input("Pick an exam: "))

   def exam():
      os.system("figlet -c -t '" + exams[int(choice) - 1] + "' |lolcat")

   for x in exams:
      if str(choice) == str(exams.index(x) + 1):
         exam()
