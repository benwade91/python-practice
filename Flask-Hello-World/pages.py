home = '<html><body><h1>Guess a number between 0 and 9!</h1><h2>place your guess at the end of the url!</h2><iframe src="https://giphy.com/embed/l378khQxt68syiWJy" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-illustration-retro-l378khQxt68syiWJy"></a></p></body></html>'


def too_high(number):
    return f'<html><body><h1>{number} is too high!</h1><iframe src="https://giphy.com/embed/GT9BB2Zm4VnI4" width="480" height="240" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/half-baked-jim-breuer-excited-GT9BB2Zm4VnI4"></a></p></body></html>'


def too_low(number):
    return f'<html><body><h1>{number} is too low!</h1><iframe src="https://giphy.com/embed/IevhwxTcTgNlaaim73" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gsimedia-lowrider-gsi-chevytruck-IevhwxTcTgNlaaim73"></a></p></body></html>'


def correct():
    return '<html><body><h1>Thats it!</h1><iframe src="https://giphy.com/embed/o75ajIFH0QnQC3nCeD" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/theoffice-o75ajIFH0QnQC3nCeD"></a></p></body></html>'