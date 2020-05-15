import os
from collections import Counter
import guitarpro
import msgpack
import numpy as np
import tab_files as tf

batch_count = 2
maxBeats = 8
batch_length = 100000

def duration(val):
    l = [2 ** i for i in range(7)]
    min = 1000
    out = 0
    for i in l:
        if abs(val - i) < min:
            min = abs(val - i)
            out = i
    return out


def enters(val):
    l = [i + 1 for i in range(13)]
    min = 1000
    out = 0
    for i in l:
        if abs(val - i) < min:
            min = abs(val - i)
            out = i
    return out


def defineKey(tab):
    keys = [
        [0, 2, 4, 5, 7, 9, 11],  # C
        [0, 2, 3, 5, 7, 8, 10],  # Cm
        [1, 3, 5, 6, 8, 10, 0],  # C#
        [1, 3, 4, 6, 8, 9, 11],  # C#m
        [2, 4, 6, 7, 9, 11, 1],  # D
        [2, 4, 5, 7, 9, 10, 0],  # Dm
        [3, 5, 7, 8, 10, 0, 2],  # D#
        [3, 5, 6, 8, 10, 11, 1],  # D#m
        [4, 6, 8, 9, 11, 1, 3],  # E
        [4, 6, 7, 9, 11, 0, 2],  # Em
        [5, 7, 9, 10, 0, 2, 4],  # F
        [5, 7, 8, 10, 0, 1, 3],  # Fm
        [6, 8, 10, 11, 1, 3, 4],  # F#
        [6, 8, 9, 11, 1, 2, 4],  # F#m
        [7, 9, 11, 0, 2, 4, 6],  # G
        [7, 9, 10, 0, 2, 3, 5],  # Gm
        [8, 10, 0, 1, 3, 5, 7],  # G#
        [8, 10, 11, 1, 3, 4, 6],  # G#m
        [9, 11, 1, 2, 4, 6, 8],  # A
        [9, 11, 0, 2, 4, 5, 7],  # Am
        [10, 0, 2, 3, 5, 7, 9],  # A#
        [10, 0, 1, 3, 5, 6, 8],  # A#m
        [11, 1, 3, 4, 6, 8, 10],  # B
        [11, 1, 2, 4, 6, 7, 9],  # Bm
    ]

    c = Counter()
    for t in tab.guitarTracks:
        for m in t.measures:
            for b in m.beats:
                if len(b.notes) > 0:
                    c[b.notes[len(b.notes) - 1].value % 12] += 1

    major = 0
    minor = 0
    for i, j in zip(keys[c.most_common(1)[0][0] * 2], keys[c.most_common(1)[0][0] * 2 + 1]):
        major += c[i]
        minor += c[j]
    # print(major, minor)
    if major >= minor:
        mm = 0
    else:
        mm = 1

    return c.most_common(1)[0][0], mm


def correctNote(note, key, mm):
    key = int(key)
    mm = int(mm)
    keys = [
        [0, 2, 4, 5, 7, 9, 11],  # C
        [0, 2, 3, 5, 7, 8, 10],  # Cm
        [1, 3, 5, 6, 8, 10, 0],  # C#
        [1, 3, 4, 6, 8, 9, 11],  # C#m
        [2, 4, 6, 7, 9, 11, 1],  # D
        [2, 4, 5, 7, 9, 10, 0],  # Dm
        [3, 5, 7, 8, 10, 0, 2],  # D#
        [3, 5, 6, 8, 10, 11, 1],  # D#m
        [4, 6, 8, 9, 11, 1, 3],  # E
        [4, 6, 7, 9, 11, 0, 2],  # Em
        [5, 7, 9, 10, 0, 2, 4],  # F
        [5, 7, 8, 10, 0, 1, 3],  # Fm
        [6, 8, 10, 11, 1, 3, 4],  # F#
        [6, 8, 9, 11, 1, 2, 4],  # F#m
        [7, 9, 11, 0, 2, 4, 6],  # G
        [7, 9, 10, 0, 2, 3, 5],  # Gm
        [8, 10, 0, 1, 3, 5, 7],  # G#
        [8, 10, 11, 1, 3, 4, 6],  # G#m
        [9, 11, 1, 2, 4, 6, 8],  # A
        [9, 11, 0, 2, 4, 5, 7],  # Am
        [10, 0, 2, 3, 5, 7, 9],  # A#
        [10, 0, 1, 3, 5, 6, 8],  # A#m
        [11, 1, 3, 4, 6, 8, 10],  # B
        [11, 1, 2, 4, 6, 7, 9],  # Bm
    ]
    min = 12
    ans = -1
    for i, j in zip(keys[key * 2 + mm], range(len(keys[key * 2 + mm]))):
        if abs(i - note) < min:
            min = abs(i - note)
            ans = i
    #return note
    return ans


def returnTestData(track, path):
    x = np.zeros((1000, maxBeats, 6), dtype=float)
    i = -1
    g = track
    tab = tf.Tab(path)
    key, mm = defineKey(tab)
    for gm in g.measures:
        i += 1
        if len(gm.beats) <= maxBeats:
            j = 0
            for gb in gm.beats:
                if len(gb.notes) > 0:
                    x[i][j][0] = 1
                    x[i][j][1] = len(gb.notes)
                    x[i][j][2] = (gb.notes[len(gb.notes) - 1].value % 12) / 12
                else:
                    x[i][j][0] = 0
                    x[i][j][1] = 0
                    x[i][j][2] = 0
                x[i][j][3] = 1 / gb.duration
                x[i][j][4] = key / 12
                x[i][j][5] = mm
                j += 1

    return x, 28, key, mm


def addTrack(base_track, y, name, tab, first_string, key, mm):
    print('start saving')
    # 'FICHIER GUITAR PRO v5.00'
    strings = [15 + first_string, 10 + first_string, 5 + first_string, first_string]

    y = y.tolist()
    tab.tracks.append(guitarpro.Track(tab))
    num = len(tab.tracks) - 1

    tab.tracks[num].number = num + 1
    tab.tracks[num].name = name
    tab.tracks[num].isPercussionTrack = False

    tab.tracks[num].channel.volume = 120
    tab.tracks[num].channel.balance = 64

    tab.tracks[num].strings = []
    for i, j in zip(strings, range(len(strings))):
        tab.tracks[num].strings.append(guitarpro.models.GuitarString(j + 1, i))

    tab.tracks[num].measures = []
    m = -1
    for measure in y:
        measureHeader = guitarpro.models.MeasureHeader()
        tab.tracks[num].measures.append(guitarpro.Measure(tab.tracks[num], measureHeader))
        m += 1
        if m > len(base_track.measures) - 1:
            break
        tab.tracks[num].measures[m].timeSignature.numerator = base_track.measures[m].timeSignature.numerator
        tab.tracks[num].measures[m].timeSignature.denominator.value = base_track.measures[
            m].timeSignature.denominator.value
        tab.tracks[num].measures[m].voices = [guitarpro.Voice(tab.tracks[num].measures[m])]
        b = -1
        takt = tab.tracks[num].measures[m].timeSignature.numerator / tab.tracks[num].measures[
            m].timeSignature.denominator.value
        takti = 0
        for beat in measure:
            if beat[2] >= 0.03125 and takti + 1 / duration(1 / beat[2]) <= takt:
                takti += 1 / duration(1 / beat[2])
                tab.tracks[num].measures[m].voices[0].beats.append(
                    guitarpro.Beat(tab.tracks[num].measures[m].voices[0]))
                b += 1

                tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.rest
                if beat[0] > 0.5:
                    tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.normal
                    tab.tracks[num].measures[m].voices[0].beats[b].notes.append(
                        guitarpro.Note(tab.tracks[num].measures[m].voices[0].beats[b]))

                    string = 3
                    for k in strings:
                        val = 36 + correctNote(beat[1] * 12, key, mm) - strings[string]
                        if val > 25:
                            string -= 1
                        else:
                            break

                    tab.tracks[num].measures[m].voices[0].beats[b].notes[0].value = val
                    tab.tracks[num].measures[m].voices[0].beats[b].notes[0].string = string + 1
                    tab.tracks[num].measures[m].voices[0].beats[b].notes[0].velocity = 127
                    tab.tracks[num].measures[m].voices[0].beats[b].notes[0].type = guitarpro.NoteType.normal

                tab.tracks[num].measures[m].voices[0].beats[b].duration.value = duration(1 / beat[2])
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDoubleDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.enters = 1
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.times = 1
