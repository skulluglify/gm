#! /usr/bin/env python3


def to_bin(i: int, n: int = 8) -> str:

    b: str;
    b = bin(i).replace("0b", "");

    b = "0" * ( n - len(b) ) + b;

    return b;

def to_bin_rtl(i: int, n: int = 23) -> str:

    b: str;
    b = bin(i).replace("0b", "");

    b += "0" * ( n - len(b) );

    return b;

def to_complement(v: int, n: int = 8) -> str:

    # 8
    # i: int;
    b: str;

    v = ((2 ** n) - 1) ^ v;

    b = to_bin(v);

    print("inverse:", b);

    return to_bin(int(b, 2) + 1);

def enfp(sign: int, mantissa: int, exponent: int) -> str:

    s: str;
    c: str;
    e: str;
    m: str;
    s = "1" if (0 > sign) else "0";

    print("sign", s);

    if (0 > exponent):

        c = to_complement(exponent * -1);
        print("complement:", c);
        exponent = int(c, 2) + 127;
    else:
        exponent = exponent + 127;

    exponent = 255 & exponent;
    
    e = to_bin(exponent);

    print("exponent:", e);

    m = to_bin_rtl(mantissa);
    print("mantissa:", m);

    return s + e + m;

def mantissa_to_decimal(b: str) -> float:

    x: int;
    v: float;
    x = 2;
    v = 0;

    for i in range(23):

        if b[i] == "1":

            v += 1 / x;
        
        x += x;
    
    return v + 1;

def defp(b: str) -> float:

    i: int;

    sign: int;
    exponent: int;
    mantissa: int;

    i = int(b, 2); # 32 bit

    sign = i >> 31;
    sign = -1 if sign else 1;
    exponent = 255 & (i >> 23);
    exponent = exponent - 127;
    mantissa = mantissa_to_decimal(b[9:32]);

    print("sign:", sign);
    print("exponent:", exponent);
    print("mantissa:", mantissa);

    return (sign * mantissa) * (2 ** exponent);

def mantissa_to_bin(i: float) -> str:

    c: int;
    x: int;
    v: float;
    s: str;

    c = 0;
    x = 2;
    v = i;
    s = "";

    while c < 23:

        m: float;
        m = 1 / x;

        if v == 0: break;

        if m <= v:

            v = v - m;
            s += "1";

        else:
            s += "0";

        x += x;
        c += 1;


    return s + "0" * (23 - len(s));

def dec2fp(i : float) -> str:

    c: int;
    x: int;

    c = 0;
    x = 1;

    sign: int;
    exponent: int;
    mantissa: int;

    sign = 0;

    if (0 > i):

        sign = 1;
        i = abs(i);

    while (x * 2) < i:

        x += x;
        c += 1;

    exponent = c + 127;

    mantissa = i / x;
    mantissa = mantissa - 1; # .25 > 0100000

    return str(sign) + to_bin(exponent) + mantissa_to_bin(mantissa);

def hex2fp(s: str) -> int:

    c: str;
    t: str;
    t = "";

    for c in s:

        t += to_bin(int(c, 16), 4);

    t = t + "0" * (32 - len(t));

    print("fp32:", t);

    return defp(t);

def fp2hex(v: float) -> str:

    s: str;
    t: str;

    s = dec2fp(v);
    t = "";

    for i in range(0, 32, 4):

        t += hex(int(s[i:i+4], 2)).replace("0x", "").upper();

    return t;

if str(__name__).upper() in ["__MAIN__"]:

    print("=" * 12);

    print("fp32:", enfp(-1, 0b1010001, 0b10100));
    
    print("=" * 12);
    
    print("fp32:", enfp(1, 0b101000, -0b10100));

    print("=" * 12);
    
    print("dec", defp("01000001001000000000000000000000"));

    print("=" * 12);
    
    print("dec", defp(dec2fp(10)));

    print("=" * 12);
    
    print(hex2fp("40A00"));
    
    print("=" * 12);
    
    print(hex2fp("40400"));
    
    print("=" * 12);
    
    print(hex2fp("40B00"));
    
    print("=" * 12);
    
    print(hex2fp("41200"));

    print("=" * 12);
    
    print(fp2hex(defp("01000001001000000000000000000000")));
    
    print("=" * 12);
    
    print(fp2hex(5.5));
    
