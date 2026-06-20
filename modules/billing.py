def hitung_tagihan(kwh, tarif):
    subtotal = kwh * tarif
    ppn = subtotal * 0.11
    total = subtotal + ppn

    return subtotal, ppn, total