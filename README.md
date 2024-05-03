# L06E01: Coin flip statistics

Vytvořte modul `coin_flip_statistics.py`, který vytvoří tři vlákna, které budou počítat do sdílené proměnné výsledky hodu mincí (náhodná hodnota z 0 nebo 1 pomocí balíčku `random`). Další vlákno pak bude každou sekundu vypisovat aktuální procentuální zastoupení obou možných výsledků, viz. výstup níže.

Vzhledem k tomu, že samotná paralelizace nejde otestovat, tak k úkolu nejsou testy.

```python
Flipper 0 flips coin 10000000-times.Flipper 1 flips coin 10000000-times.

Flipper 2 flips coin 10000000-times.
Flipped head 50.017% and Tail 49.983% times.
Flipped head 50.011% and Tail 49.989% times.
Flipped head 49.995% and Tail 50.005% times.
Flipped head 49.98% and Tail 50.02% times.
Flipped head 49.988% and Tail 50.012% times.
Flipped head 49.984% and Tail 50.016% times.
Flipped head 49.983% and Tail 50.017% times.
Flipped head 49.989% and Tail 50.011% times.
Flipped head 49.99% and Tail 50.01% times.
Flipped head 49.985% and Tail 50.015% times.
Flipper 0 ended.
Flipper 2 ended.
Flipped head 49.989% and Tail 50.011% times.
Flipper 1 ended.
Printer ended.
```
