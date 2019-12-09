def retrieve_genre(emotion):
    if emotion == 'sad':
        return 'Thriller'
    elif emotion == 'tried':
        return 'Comedy'
    elif emotion == 'happy':
        return 'Animation'
    elif emotion == 'romantic':
        return 'Romance'
    elif emotion == 'angry':
        return 'Action'
    elif emotion == 'sick':
        return 'War'
    elif emotion == 'lonely-midnight':
        return 'Mystery'
    else:
        return 'Crime'
