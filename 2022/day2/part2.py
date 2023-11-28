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

def action_to_get_result(result_wanted:GameResult, opponent_action:Action)->(Action, GameResult):
    if not isinstance(opponent_action,Action) or not isinstance(result_wanted, GameResult):
        raise ValueError("Wrong enums put in!")
    match result_wanted:
        case GameResult.Win:
            match opponent_action:
                case Action.Rock:
                    return (Action.Paper, result_wanted)
                case Action.Paper:
                    return (Action.Scissors, result_wanted)
                case Action.Scissors:
                    return (Action.Rock, result_wanted)
        case GameResult.Loose:
            match opponent_action:
                case Action.Rock:
                    return (Action.Scissors, result_wanted.Win)
                case Action.Paper:
                    return (Action.Rock,result_wanted)
                case Action.Scissors:
                    return (Action.Paper, result_wanted)
        case GameResult.Draw:
            match opponent_action:
                case Action.Rock:
                    return (Action.Rock,result_wanted)
                case Action.Paper:
                    return (Action.Paper,result_wanted)
                case Action.Scissors:
                    return (Action.Scissors,result_wanted)

def final_score(action:Action, result:GameResult)->int:
    if not isinstance(action,Action) or not isinstance(result, GameResult):
        raise ValueError("Wrong enums put in!")
    return action.value + result.value

def main(file_name:str)->int:
    player_must = {"X": GameResult.Loose, "Y":GameResult.Draw ,"Z":GameResult.Win }
    bot_actions = {"A": Action.Rock, "B":Action.Paper ,"C":Action.Scissors }
    plan = [(bot_actions[bot_str], player_must[player_str]) for (bot_str, player_str) in line_yielder(file_name)]
    rounds = [ action_to_get_result(result_wanted, opponent_action) for (opponent_action, result_wanted) in plan ]
    scoring = [ final_score(action,result) for (action,result) in rounds]
    
    return sum(scoring)


if __name__ == '__main__':
    file_name, answer = "dummy.txt",12
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the dummy!")
    file_name, answer = "puzzle.txt",13071
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the puzzle!")