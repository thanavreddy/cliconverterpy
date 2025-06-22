import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--c2f', type=float, help='Convert Celsius to Fahrenheit')
    group.add_argument('--f2c', type=float, help='Convert Fahrenheit to Celsius')

    args = parser.parse_args()

    try:
        if args.c2f is not None:
            result = celsius_to_fahrenheit(args.c2f)
            print(f"{args.c2f}°C is equivalent to {result:.2f}°F")
        elif args.f2c is not None:
            result = fahrenheit_to_celsius(args.f2c)
            print(f"{args.f2c}°F is equivalent to {result:.2f}°C")
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")

if __name__ =="__main__":
    main()
    