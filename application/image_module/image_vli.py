
MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOW_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS:
        return True
    return False


if __name__ == '__main__':
    print(allowed_file('hello.png.jpeg'))