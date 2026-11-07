# -*- coding: utf-8 -*-
"""Complete Part Four chapters data (Chapters 13 to 23)"""
from edition.content.part4_data import PART4_CHAPTERS
from edition.content.part4b_data import PART4B_CHAPTERS
from edition.content.part4c_data import PART4C_CHAPTERS

# PART4_CHAPTERS has ch 13, 14, 15, 16
# PART4B_CHAPTERS has ch 17, 18, 19, 20
# PART4C_CHAPTERS has ch 21, 22, 23, 24
ALL_PART4_AND_CODA = PART4_CHAPTERS + PART4B_CHAPTERS + PART4C_CHAPTERS
print(f"Total chapters in Part 4 + Coda: {len(ALL_PART4_AND_CODA)}")
