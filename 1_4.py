days=int(input("Enter the number of days:"))
years=int(days/365)
weeks=int((days%365)/7)
d=(days%365)%7
print("Age of Alex=",years," Years ",weeks," Weeks and ",d," Days")