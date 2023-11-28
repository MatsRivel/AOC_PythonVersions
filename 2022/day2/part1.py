from enum import Enum

class GameResult(Enum):
    Win = 6
    Draw = 3
    Loose = 0

class Action(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

def line_processer(line:str)->(str,str):
    return line.strip("\n").split(" ")

def line_yielder(file_name:str)->(str,str):
    for line in open(file_name,'r'):
        yield line_processer(line)

def resolve_round(a:Action, b:Action)->(Action, GameResult):
    match a:
        case Action.Rock:
            match b:
                case Action.Rock:
                    return (Action.Rock, GameResult.Draw)
                case Action.Paper:
                    return (Action.Rock, GameResult.Loose)
                case Action.Scissors:
                    return (Action.Rock, GameResult.Win)
        case Action.Paper:
            match b:
                case Action.Rock:
                    return (Action.Paper, GameResult.Win)
                case Action.Paper:
                    return (Action.Paper, GameResult.Draw)
                case Action.Scissors:
                    return (Action.Paper, GameResult.Loose)
        case Action.Scissors:
            match b:
                case Action.Rock:
                    return (Action.Scissors,GameResult.Loose)
                case Action.Paper:
                    return (Action.Scissors,GameResult.Win)
                case Action.Scissors:
                    return (Action.Scissors,GameResult.Draw)

def final_score(action:Action, result:GameResult)->int:
    return action.value + result.value
    
def main(file_name:str):
    player_actions = {"X": Action.Rock, "Y":Action.Paper ,"Z":Action.Scissors }
    bot_actions    = {"A": Action.Rock, "B":Action.Paper ,"C":Action.Scissors }
    plan = [(bot_actions[bot_str],player_actions[player_str]) for (bot_str,player_str) in line_yielder(file_name)]
    rounds = [ resolve_round(player,bot) for (bot,player) in plan ]
    scoring = [ final_score(action,result) for (action,result) in rounds]
    return sum(scoring)

if __name__ == '__main__':
    file_name, answer = "dummy.txt",15
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the dummy!")
    file_name, answer = "puzzle.txt",10941
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the puzzle!")