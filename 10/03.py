def func(x='shout'):
    def shout_func(say='hello'):
        return f'{say.upper()}!'

    def whisper_func(say='hello'):
        return f'{say.lower()}...'

    if x == 'shout':
        return shout_func
    else:
        return whisper_func


print(func('vlad')('IGOR'))
