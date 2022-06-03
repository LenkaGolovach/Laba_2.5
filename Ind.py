#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = tuple(map(int, input("Введите стоимость - ").split()))
    B = tuple(map(int, input("Введите мощность - ").split()))
    for id, val in enumerate(B):
        if val <= 80:
            print("Автомобиль, мощность которого не превышает 80 л.с. Его цена - ",
                  A[id], " его мощность в л.с. - ", B[id])
