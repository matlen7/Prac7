from car import Car
def main():
    bus = Car(180)
    bus.drive(30)
    limo = Car(fuel=100)
    limo.drive(-20)
    limo.drive(115)
    print("limo fuel =", limo.fuel)
    print("limo odo =", limo.odometer)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
main()