def findmin(amount):
    min = 101
    minindex=0
    counter = 0
    for counter in amount:
        if  min>counter:
             min=counter
    return amount.index(min)


class Team:
    Name=''
    Color=''
    CoachName=''
    CoachSurname=''
    Tactic=0
    AllPlayers=[]
    StartPlayers=[]
    ReservePlayers=[]
    def __init__(self,Name,Color,Money,CoachName,CoachSurname,Tactic,TeamPlayers):
        self.Name=Name
        self.Color=Color
        self.Money=Money
        self.CoachName=CoachName
        self.CoachSurname=CoachSurname
        self.Tactic=Tactic
        self.AllPlayers=TeamPlayers
    def FillStartSquad(self):
        Strikers = int(self.Tactic % 10)
        Tactic = int(self.Tactic / 10)
        Middefenders = int(Tactic % 10)
        Tactic = int(Tactic / 10)
        Defenders = int(Tactic % 10)
        GKRATING=0
        DefendersRating=[]
        while Defenders>0:
            DefendersRating.append(0)
            Defenders-=1
        MiddefendersRating=[]
        while Middefenders>0:
            MiddefendersRating.append(0)
            Middefenders-=1
        StrikersRating = []
        while Strikers > 0:
            StrikersRating.append(0)
            Strikers -= 1
        Strikers = int(self.Tactic % 10)
        Tactic = int(self.Tactic / 10)
        Middefenders = int(Tactic % 10)
        Tactic = int(Tactic / 10)
        Defenders = int(Tactic % 10)
        for Player in self.AllPlayers:
            if Player.Position=='GK' and Player.Rating>GKRATING:
                if len(self.StartPlayers)>0:
                    self.StartPlayers.pop(0)
                self.StartPlayers.append(Player)
                GKRATING=Player.Rating
            if Player.Position=='DF' and Player.Rating>DefendersRating[findmin(DefendersRating)]:
                if len(self.StartPlayers)>Defenders:
                    self.StartPlayers.pop(1+findmin(DefendersRating))
                self.StartPlayers.append(Player)
                DefendersRating[findmin(DefendersRating)]=Player.Rating
            elif Player.Position=='MD' and Player.Rating>MiddefendersRating[findmin(MiddefendersRating)]:
                if len(self.StartPlayers)>Defenders+Middefenders:
                    self.StartPlayers.pop(1+Defenders+findmin(MiddefendersRating))
                self.StartPlayers.append(Player)
                MiddefendersRating[findmin(MiddefendersRating)] = Player.Rating
            elif Player.Position=='ST' and Player.Rating>StrikersRating[findmin(StrikersRating)]:
                if len(self.StartPlayers)>Defenders+Middefenders+Strikers:
                    self.StartPlayers.pop(1+Defenders+Middefenders+findmin(StrikersRating))
                self.StartPlayers.append(Player)
                StrikersRating[findmin(StrikersRating)] = Player.Rating