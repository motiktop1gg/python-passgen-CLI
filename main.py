import generator as gen
import argparse

memorable_mode_name = "Memorable mode"
notrepeat_mode_name = "Not repeat mode"

parser = argparse.ArgumentParser()
parser.add_argument("length", type=int, help="Length of each password", default=None, nargs="?")
parser.add_argument("count", type=int, help="Number of passwords", default=None, nargs="?")
parser.add_argument("-m", type=str, default=False, required=False, help="Adds easy-to-remember words to the password(s).")
parser.add_argument("-n", type=str, default=False, required=False, help="Disabling repeats in the password(s).")
args = parser.parse_args()

def is_true(mode, mode_name):
    if str(mode).lower() == "true":
        print(f"{mode_name} enabled")
        return True
    else:
        print(f"{mode_name} disabled")
        return False

def limits(param, max, min, message):
    if param <= max and param > min: pass
    else:
        print(message)
        exit()

if __name__ == "__main__":
    if args.length is not None and args.count is not None:
        memorable_mode = is_true(args.m, memorable_mode_name)
        notrepeat_mode = is_true(args.n, notrepeat_mode_name)
        if memorable_mode and notrepeat_mode:
            print("You can't using both of modes")
            exit()
        gen.gen_pass(args.length, args.count, memorable_mode, notrepeat_mode)
        exit()
    else:
        try:
            length = int(input("Enter the length of a password: "))
            length_message = "Your password length is too small or too large!"
            limits(length, 512, 2, length_message)

            count = int(input("Enter a count of passwords: "))
            count_message = "You are trying to generate too many or zero passwords!"
            limits(count, 256, 0, count_message)

            memorable_mode = str(input("Enable memorable mode? (True/False): "))
            memorable_mode = is_true(memorable_mode, memorable_mode_name)

            notrepeat_mode = str(input("Enable not repeat mode? (max length is 43) (True/False): "))
            notrepeat_mode = is_true(notrepeat_mode, notrepeat_mode_name)
            if memorable_mode and notrepeat_mode:
                print("You can't using both of modes")
                exit()

        except ValueError:
            print("Your input is not a number!")
            exit()

        gen.gen_pass(length, count, memorable_mode, notrepeat_mode)