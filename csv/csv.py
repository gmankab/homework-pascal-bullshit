from inspect import cleandoc
import sys


try:
    sys.path.append('D:/dev/python-libs/pandas-1.3.5')
    import pandas as pd
except ImportError:
    import os
    os.system(f'{sys.executable} -m pip install pandas')
    import pandas as pd


# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false


df = pd.read_csv(
    'marks.csv',
    encoding='windows-1251',
    names = ['name', 'surname', 'alg', 'rus', 'phys', 'history'],
)


def aver(subject):
    return sum(list(df[subject])) / len(list(df[subject]))


print(
    cleandoc(
        f'''
        Задание а:
            Средний балл по алгебре: {aver('alg')}
            Средний балл по русскому языку: {aver('rus')}
            Средний балл по физике: {aver('phys')}
            Средний балл по истории: {aver('history')}
        '''
    )
)


df["sum"] = df[['alg', 'rus', 'phys', 'history']].sum(axis=1)
maximal = df['sum'].max()

print(
    cleandoc(
        f'''
        Задание б:
            Максимальная сумма баллов: {maximal}
        '''
    )
)

df = df.loc[df['sum'] == maximal]
df['fillnm'] = df.agg(lambda x: f"{x['name']} {x['surname']}", axis=1)

print(
    cleandoc(
        f'''
        Задание в:
            {df}
        '''
    )
)
