class Device:
    def turn_on(self):
        print('The device was turned on')


class Radio(Device):
    pass


class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')


class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')


device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvSet = TvSet()

for element in (device, radio, portableRadio, tvSet):
    element.turn_on()
