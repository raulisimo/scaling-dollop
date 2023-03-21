import serial


class DeviceController:
    def __init__(self, serial_port, baud_rate=9600):
        self.serial_port = serial_port
        self.baud_rate = baud_rate

    def connect(self):
        """Open a serial port connection to the microcontroller."""
        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to serial port: {e}")

    def disconnect(self):
        """Close the serial port connection to the microcontroller."""
        try:
            self.ser.close()
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to disconnect from serial port: {e}")

    def program_digital_outputs(self, active_devices):
        """
        Convert the active devices into a digital, serial data stream and send it to the microcontroller
        to program the digital outputs of the Sub-Control Module.
        """
        # Convert the active devices into a binary string of length 32
        binary_string = ''.join('1' if device in active_devices else '0' for device in range(32))

        # Convert the binary string into 4 bytes (32 bits) in little-endian order
        data_bytes = bytearray(int(binary_string[i:i+8], 2) for i in range(0, 32, 8))

        # Send the data bytes to the microcontroller via the serial port
        try:
            for i in range(4):
                command = f"DOP_{i}_{data_bytes[i]:01b}"
                self.ser.write(command.encode())
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to write data to serial port: {e}")


controller = DeviceController(serial_port="COM1")
controller.connect()
controller.program_digital_outputs(active_devices=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])
controller.disconnect()
