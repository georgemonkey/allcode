from robotevents import RobotEvents

re = RobotEvents("your_token_here")
team = re.teams.get(number="42824A")
print(team)