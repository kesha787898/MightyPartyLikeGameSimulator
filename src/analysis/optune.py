import optuna
from src import config
from src.play.Game import AbstractGame


def objective(trial):
    config.mag_hp = trial.suggest_int('mag_hp', 1, 50)
    config.mag_base_attack_power = trial.suggest_int('mag_base_attack_power', 1, 50)
    config.priest_hp = trial.suggest_int('priest_hp', 1, 50)
    config.priest_base_attack_power = trial.suggest_int('priest_base_attack_power', 1, 50)
    config.archer_hp = trial.suggest_int('archer_hp', 1, 50)
    config.archer_base_attack_power = trial.suggest_int('archer_base_attack_power', 1, 50)
    config.warrior_hp = trial.suggest_int('warrior_hp', 1, 50)
    config.warrior_base_attack_power = trial.suggest_int('warrior_base_attack_power', 1, 50)
    config.knight_hp = trial.suggest_int('knight_hp', 1, 50)
    config.knight_base_attack_power = trial.suggest_int('knight_base_attack_power', 1, 50)
    config.druid_hp = trial.suggest_int('druid_hp', 1, 50)
    config.druid_base_attack_power = trial.suggest_int('druid_base_attack_power', 1, 50)
    config.hp_first = 100
    config.hp_second = config.hp_first
    results = AbstractGame().play_games(3000)
    winners = []
    hps0 = []
    hps1 = []
    for winner, hp0, hp1 in results:
        winners.append(winner)
        hps0.append(hp0)
        hps1.append(hp1)
    return abs((sum(winners) / len(winners)) - 0.5)


study = optuna.create_study()
study.optimize(objective, n_trials=1000)

print(study.best_params)
