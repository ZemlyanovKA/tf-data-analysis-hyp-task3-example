import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 527952713 # Ваш chat ID, не меняйте название переменной

def solution(control_group: np.array,
             test_group: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.09
    # Рассчитываем t-статистику и p-значение
    t_stat, p_value = ttest_ind(control_group, test_group, equal_var=False)  # Используем Welch's t-test
    
    # Сравниваем p-значение с уровнем значимости
    if p_value < alpha:
        return True  # Отклоняем нулевую гипотезу
    else:
        return False  # Не отклоняем нулевую гипотезу
