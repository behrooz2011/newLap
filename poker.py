
#hand = [["h",2], ["h",3]]
class Winner:
  def __init__(self, hand1, hand2):
    self.hand1 = hand1
    self.hand2 = hand2
  #Ranks
  rank = [
      "highCard","pair","twoPairs","three","straight",
    "flush","fullHouse","quad","straightFlush","royalFlush"
           ]

  #Royal Flush
  def royalFlush(self,hand):
    #hand = [["h",2], ["h",3]]
    suit=hand[0][0]
    for i in range(len(hand)):
        if suit != hand[i][0]:
            return False
    arr = [10 , 11, 12, 13, 14]
    arr2=[]
    for j in range(len(hand)):
      arr2.append(hand[j][1])
    # print("arr2:",arr2)
    arr2.sort()
    # print("arr",arr)
    # print("arr2 sorted: ",arr2)
    if arr != arr2:
        return False
    return True

  #Straight Flush
  def straightFlush(self,hand):
    suit=hand[0][0]
    #let's get the numerical values of a hand :
    handNumber = [ hand[i][1] for i in range(len(hand))]
    for i in range(len(hand)):
        if suit != hand[i][0]:
            return False
    handNumber.sort()
    # print("handNumber:",handNumber)
    for j in range(len(handNumber)):
      if ((j+1 < len(handNumber)) and ((handNumber[j+1]- handNumber[j] != 1))):
        return False
    return True

  #Quad
  def quad(self,hand):
    obj = {}
    for i in range(len(hand)):
      if hand[i][1] not in obj:
        obj[hand[i][1]] = 1
      else:
        obj[hand[i][1]] += 1
    # print("obj for quad:",obj)
    for key in obj:
      if obj[key] == 4:
        return True
    return False

  #fullHouse
  def fullHouse(self,hand):
    obj = {}
    for i in range(len(hand)):
      if hand[i][1] not in obj:
        obj[hand[i][1]] = 1
      else:
        obj[hand[i][1]] += 1
    # print("obj for fullhouse:",obj)
    #if the number of occurance of a certain key is
    #equal to 3 and there are only two keys, that would
    # make a full house, for example: { 4,4,4 Q Q}
    for i,val in enumerate(list(obj.items())):
      if(val[1] == 3 and len(obj) == 2):
        return True
    return False

  #flush
  def flush(self,hand):
    suit=hand[0][0]
    for i in range(len(hand)):
        if suit != hand[i][0]:
            return False
    return True

  #Straight
  def straight(self,hand):
    #Get the numerical value of each card
    handNumber = [ hand[i][1] for i in range(len(hand))]
    handNumber.sort()
    #check if the middle value equals the average
    # if not, that's not a straight
    for j in range(len(handNumber)):
      if ((j+1 < len(handNumber)) and ((handNumber[j+1]- handNumber[j] != 1))):
        return False
    return True

  #Three of a kind
  def three(self,hand):
    obj = {}
    for i in range(len(hand)):
      if hand[i][1] not in obj:
        obj[hand[i][1]] = 1
      else:
        obj[hand[i][1]] += 1
    # print("obj for 3 of a kinf:",obj)
    for i,val in enumerate(list(obj.items())):
      if(val[1] == 3):
        return True
    return False

  #two pairs
  def twoPairs(self,hand):
    obj = {}
    pairs =0
    for i in range(len(hand)):
      if hand[i][1] not in obj:
        obj[hand[i][1]] = 1
      else:
        obj[hand[i][1]] += 1
    # print("obj for two pairs:",obj)
    for i,val in enumerate(list(obj.items())):
      if(val[1] == 2):
        pairs += 2
    if pairs == 4:
      return True   
    return False

  #Pair
  def pair(self,hand):
    obj = {}
    for i in range(len(hand)):
      if hand[i][1] not in obj:
        obj[hand[i][1]] = 1
      else:
        obj[hand[i][1]] += 1
    # print("obj a pair:",obj)
    for i,val in enumerate(list(obj.items())):
      if val[1] == 2:
        return True
    return False

  #High Card
  def highCard(self,hand):
    #Get the numerical value of each card
    handNumber = [ hand[i][1] for i in range(len(hand))]
    handNumber.sort()
    return handNumber[4]# the last value is the highest.

  #Who is the winner? hand1 or hand2?
  def winner(self, hand1, hand2):
    #final_score = { hand1:[rank,value],hand2:[rank,vaue]}
    score={}
    allFunctionsHand1 = {
      "royalFlush" : self.royalFlush(hand1),
      "straightFlush" : self.straightFlush(hand1),
      "quad": self.quad(hand1),
      "fullHouse": self.fullHouse(hand1),
      "flush": self.flush(hand1),
      "straight": self.straight(hand1),
      "three":self.three(hand1),
      "twoPairs": self.twoPairs(hand1),
      "pair": self.pair(hand1),
      "highCard": self.highCard(hand1)
    }
    allFunctionsHand2 = {
      "royalFlush" : self.royalFlush(hand2),
      "straightFlush" : self.straightFlush(hand2),
      "quad": self.quad(hand2),
      "fullHouse": self.fullHouse(hand2),
      "flush": self.flush(hand2),
      "straight": self.straight(hand2),
      "three":self.three(hand2),
      "twoPairs": self.twoPairs(hand2),
      "pair": self.pair(hand2),
      "highCard": self.highCard(hand2)
    }
    for key in allFunctionsHand1:
      if key != "highCard" and allFunctionsHand1[key] == True:
        # print("rank index for hand 1 is :",self.rank.index(key))
        score["hand1"]=[self.rank.index(key),self.rank.index(key)]
        break
      elif key == "highCard":
        # print("rrrank index of hand 1 is: ",allFunctionsHand1[key])
        score["hand1"]=[self.rank.index(key),allFunctionsHand1[key]]
    for key in allFunctionsHand2:
      if key != "highCard" and allFunctionsHand2[key] == True:
        # print("rank index for hand 2 is :",self.rank.index(key))
        score["hand2"]=[self.rank.index(key),allFunctionsHand2[key]]
        break
      elif key == "highCard":
        # print("rrrank index of hand 2 is: ",allFunctionsHand2[key])
        score["hand2"] = [self.rank.index(key),allFunctionsHand2[key]]
    # return score
    if(score["hand1"][0] > score["hand2"][0]):
      print("the winner is hand 1 with a ",self.rank[score["hand1"][0]])
      return "hand1"
    if (score["hand1"][0] < score["hand2"][0]):
      print("the winner is hand 2 with a ",self.rank[score["hand2"][0]])
      return "hand2"
    if(score["hand1"][0] == score["hand2"][0]):
      if(score["hand1"][1] > score["hand2"][1]):
        print("the winner is hand 1 with a high card")
        return "hand1"
      if(score["hand1"][1] < score["hand2"][1]):
        print("the winner is hand 2 with a high card")
        return "hand2"
      if(score["hand1"][1] == score["hand2"][1]):
        print("They both tied. It's a draw")
        return "draw"
        
    


      
  

    
    
    
    
    
    

    
    
    
    
    

#######################################################################################
#                           TESTS and Hypothetical Scenarios
#######################################################################################
p1 = Winner("hand1","hand2")
# print(p1.royalFlush([["h",14], ["h",11], ["h",12], ["h",13], ["h",10]]   ))
# print(len(p1.ranks()))

# print(p1.straightFlush([["h",9], ["h",11], ["h",12], ["h",13], ["h",10]]   ))
# print(p1.straightFlush([["h",3], ["h",9], ["h",5], ["h",6], ["h",7]]   ))

# print(p1.quad([["h",3], ["h",3], ["h",11], ["h",3], ["h",3]]   ))

# print(p1.fullHouse([["h",3], ["h",3], ["h",11], ["h",3], ["h",11]]   ))

# print(p1.flush([["h",3], ["h",10], ["h",11], ["h",6], ["h",4]]   ))

# print(p1.straight([["h",3], ["s",9], ["h",5], ["h",6], ["d",7]]   ))
# print(p1.straight([["h",8], ["s",9], ["h",5], ["h",6], ["d",7]]   ))

# print(p1.three([["h",3], ["s",13], ["h",11], ["d",11], ["s",11]]   ))
# print(p1.three([["h",3], ["s",13], ["h",11], ["d",11], ["s",11]]   ))

# print(p1.twoPairs([["h",3], ["s",13], ["h",11], ["d",3], ["s",11]]   ))
# print(p1.twoPairs([["h",3], ["s",3], ["h",11], ["d",3], ["s",11]]   ))

# print(p1.pair([["h",13], ["s",13], ["h",11], ["d",3], ["s",11]]   ))
# print(p1.pair([["h",3], ["s",3], ["h",14], ["d",5], ["c",11]]   ))

# print(p1.highCard([["h",13], ["s",13], ["h",11], ["d",3], ["s",14]]   ))
# print(p1.highCard([["h",3], ["s",3], ["h",2], ["d",5], ["c",4]]   ))

print(p1.winner( [["h",9], ["h",11], ["h",12], ["h",13], ["h",10]]  , [["h",14], ["h",11], ["h",12], ["h",13], ["h",10]] ))

print(p1.winner([["h",3], ["h",10], ["h",11], ["h",6], ["h",4]],    [["h",8], ["s",9], ["h",5], ["h",6], ["d",7]] ))


print(p1.winner([["h",13], ["s",9], ["h",11], ["d",3], ["s",14]]  , [["h",3], ["s",10], ["h",9], ["d",2], ["s",6]]    ))

print(p1.winner([["h",13], ["s",9], ["h",11], ["d",3], ["s",14]]  , [["h",3], ["s",10], ["h",9], ["d",2], ["s",6]]    ))

  
  





  