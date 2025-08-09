from pyfiglet import Figlet


def create_logo(text: str, font: str = 'big') -> str:
    f = Figlet(font=font)
    return f.renderText(text)


if __name__ == '__main__':
    logo = create_logo(
        text='Avi Zaguri',
        font='big',
        # font='slant',
        # font='standard',
    )
    print(logo)
