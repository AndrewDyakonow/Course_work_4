from app.processing.class_json_processing import JsonProcessing
from app_interface.form import drow_form


def main():
    a = JsonProcessing()
    a.create_file()
    drow_form()


if __name__ == '__main__':
    main()
