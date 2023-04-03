import pandas as pd
import numpy as np


chat_id = 201321241 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = np.log(x-3)
    return x.mean() # Ваш ответ
