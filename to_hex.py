def to_hex(n):
    hex_num = ""
    if ((n >= 0) & (n < 256)):
        if (n == 0):
            hex_num = "0"
        while (n != 0):
            rem = n % 16 
            match rem:
                case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                    hex_num += str(rem)
                case 10:
                    hex_num += "a"
                case 11:
                    hex_num += "b"
                case 12:
                    hex_num += "c"
                case 13:
                    hex_num += "d"
                case 14:
                    hex_num += "e"
                case 15:
                    hex_num += "f"
            n = n // 16
        hex_num = hex_num[::-1]
        print(hex_num)
        return(hex_num)
def hex_code(red, green, blue):
    hex_result = "#"
    red_hex = to_hex(red)
    if len(red_hex) == 1:
        red_hex = '0' + red_hex
    green_hex = to_hex(green)
    if len(green_hex) == 1:
        green_hex = '0' + green_hex
    blue_hex = to_hex(blue)
    if len(blue_hex) == 1:
        blue_hex = '0' + blue_hex
    hex_result = hex_result + red_hex + green_hex + blue_hex
    print(hex_result)
hex_code(0,0,0)
