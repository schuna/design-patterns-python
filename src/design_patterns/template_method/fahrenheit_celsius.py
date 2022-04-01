import sys


def main():
    done = False

    while not done:
        print("Input Fahrenheit:")
        fahrenheit = number_from_input_stream()
        if fahrenheit is None:
            done = True
        else:
            celsius = 5.0 / 9.0 * (fahrenheit - 32)
            print(f"{fahrenheit:.2f}℉ = {celsius:.2f}℃")

    print("Fahrenheit to Celsius Finished!")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def number_from_input_stream():
    parsed_number = [float(s) for s in sys.stdin.readline().split() if is_number(s)]
    if len(parsed_number) == 1:
        return parsed_number[0]
    else:
        return None


if __name__ == '__main__':
    main()
