'''Goal: Input a raw number of seconds (e.g., 3665). Use Integer Division // and Modulo % to 
calculate exactly how many Hours, Minutes, and Seconds this represents.'''

seconds = int(input("Enter the seconds: "))# input seconds

h = seconds // 3600                        # h = hours
remaining_seconds = seconds % 3600

min = remaining_seconds // 60              # min = minutes
sec = remaining_seconds % 60               # sec = seconds

print(f"Hours = {h}, Minutes = {min}, Seconds = {sec}")