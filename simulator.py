import random
import argparse

cards ={
"1": "frontalAssault",
"2": "frontalAssault",
"3": "frontalAssault",
"4": "frontalAssault",
"5": "frontalAssault",
"6": "frontalAssault",
"7": "frontalAssault",
"8": "frontalAssault",
"9": "frontalAssault",
"10": "frontalAssault",
"11": "frontalAssault",
"12": "frontalAssault",
"13": "flankLeft",
"14": "flankLeft",
"15": "flankLeft",
"16": "flankLeft",
"17": "flankLeft",
"18": "flankLeft",
"19": "flankLeft",
"20": "flankLeft",
"21": "flankLeft",
"22": "rightRight",
"23": "rightRight",
"24": "rightRight",
"25": "rightRight",
"26": "rightRight",
"27": "rightRight",
"28": "rightRight",
"29": "rightRight",
"30": "rightRight",
"31": "probe",
"32": "probe",
"33": "probe",
"34": "probe",
"35": "probe",
"36": "probe",
"37": "probe",
"38": "probe",
"39": "doubleEnvelopment",
"40": "doubleEnvelopment",
"41": "doubleEnvelopment",
"42": "doubleEnvelopment",
"43": "doubleEnvelopment",
"44": "doubleEnvelopment",
"45": "reserve",
"46": "reserve",
"47": "reserve",
"48": "reserve",
}


parser = argparse.ArgumentParser(description='Hannibal and Hamilcar Battle Simulator', usage='%(prog)s')
parser.add_argument('-ahs', nargs=1, required=False, type=int, default=10, help='Player A (attacker) Hand Size')
parser.add_argument('-abr', nargs=1, required=False, type=int, default=3, help='Player A (attacker) Battle Rating')
parser.add_argument('-bhs', nargs=1, required=False, type=int, default=10, help='Player B (attacker) Hand Size')
parser.add_argument('-bbr', nargs=1, required=False, type=int, default=3, help='Player B (attacker) Battle Rating')

args = parser.parse_args()

playerA_handSize = args.ahs[0]
playerB_handSize = args.bhs[0]
playerA_battleRating = args.abr[0]
playerB_battleRating = args.bbr[0]

numberOfSimulations = 100000
print("Total Simulations: " + str(numberOfSimulations))
print("Attacker Hand Size: " + str(playerA_handSize))
print("Defender Hand Size: " + str(playerB_handSize))
print("Attacker Battle Rating: " + str(playerA_battleRating))
print("Defender Battle Rating: " + str(playerB_battleRating) + "\n")

A_wins = 0
B_wins = 0
match = False

for i in range(1,numberOfSimulations):
    playerA_hand = []
    playerB_hand = []
    deck = list(range(1,49))
    initiative = "A"

    #generate player A hand
    for x in range(playerA_handSize):
        deckSize = len(deck)
        num = random.randint(0,deckSize-1)
        playerA_hand.append(deck[num])
        deck.pop(num)

    #generate player B hand
    for x in range(playerB_handSize):
        deckSize = len(deck)
        num = random.randint(0,deckSize-1)
        playerB_hand.append(deck[num])
        deck.pop(num)

    #start battle with player having initiative
    battle = True
    while battle == True:
        if len(playerA_hand) == 0:
            B_wins += 1
            break

        if len(playerB_hand) == 0:
            A_wins += 1
            break

        if initiative == "A":
            max = len(playerA_hand)
            cardNum = random.randint(0,max-1)
            #need to check for reserve
            cardAnum = playerA_hand[cardNum]
            playerA_hand.pop(cardNum)
            cardA = cards[str(cardAnum)]

            match = False
            for x, cardNum in enumerate(playerB_hand):
                cardB = cards[str(cardNum)]
                #check for match
                if cardB == cardA:
                    playerB_hand.pop(x)
                    match = True
                    break
            #check for reserve card
            if match == False:
                for x, cardNum in enumerate(playerB_hand):
                    cardB = cards[str(cardNum)]
                    # check for match
                    if cardB == "reserve":
                        playerB_hand.pop(x)
                        match = True
                        break

            if match == False:
                #player A wins
                A_wins += 1
                battle = False

        if initiative == "B":
            max = len(playerB_hand)
            cardNum = random.randint(0, max-1)
            cardBnum = playerB_hand[cardNum]
            playerB_hand.pop(cardNum)
            cardB = cards[str(cardBnum)]

            match = False
            # need to check for reserve
            for x, cardNum in enumerate(playerA_hand):
                cardA = cards[str(cardNum)]
                # check for match
                if cardB == cardA:
                    playerA_hand.pop(x)
                    match = True
                    break

            #check for reserve card
            if match == False:
                for x, cardNum in enumerate(playerA_hand):
                    cardA = cards[str(cardNum)]
                    # check for match
                    if cardA == "reserve":
                        playerA_hand.pop(x)
                        match = True
                        break

            if match == False:
                # player B wins
                B_wins += 1
                battle = False

        if match == True and initiative == 'A':
            die = random.randint(1,6)
            if die <= playerB_battleRating:
                initiative = "B"
                continue

        if match == True and initiative == 'B':
            die = random.randint(1,6)
            if die <= playerA_battleRating:
                initiative = "A"


print("Player A wins: " + str(A_wins) + "\t(" + str(A_wins/(numberOfSimulations/100)) + "%)")
print("Player B wins: " + str(B_wins) + "\t(" + str(B_wins/(numberOfSimulations/100)) + "%)")